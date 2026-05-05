import os
import sqlite3
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'lumina_finance_super_secret_key'

UPLOAD_FOLDER = 'uploads'
DB_FILE = 'expenses.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def mock_ai_categorize(description):
    """
    Simulates an AI categorization model using a smart keyword rules engine.
    """
    desc = str(description).lower()
    
    categories = {
        'Food & Dining': ['starbucks', 'mcdonalds', 'kfc', 'restaurant', 'cafe', 'swiggy', 'zomato', 'pizza', 'burger', 'subway', 'dining', 'food', 'grocery', 'supermarket', 'mart', 'bakery'],
        'Transportation': ['uber', 'lyft', 'ola', 'taxi', 'fuel', 'gas', 'shell', 'petrol', 'transit', 'metro', 'train', 'flight', 'airline', 'airways'],
        'Shopping': ['amazon', 'flipkart', 'myntra', 'walmart', 'target', 'apple', 'store', 'shop', 'mall', 'clothing', 'electronics'],
        'Entertainment': ['netflix', 'spotify', 'disney', 'hulu', 'prime video', 'movie', 'cinema', 'theater', 'gaming', 'steam', 'playstation', 'xbox'],
        'Utilities & Bills': ['electric', 'water', 'internet', 'broadband', 'phone', 'mobile', 'recharge', 'bill', 'utility', 'insurance'],
        'Health & Fitness': ['pharmacy', 'hospital', 'clinic', 'gym', 'fitness', 'health', 'medicare', 'apollo'],
        'Education': ['university', 'college', 'school', 'tuition', 'course', 'udemy', 'coursera', 'book', 'stationery']
    }
    
    for category, keywords in categories.items():
        if any(keyword in desc for keyword in keywords):
            return category
            
    return 'Other/Miscellaneous'

def process_csv(filepath):
    try:
        # Try reading with pandas
        df = pd.read_csv(filepath)
        
        # We need to map columns to: date, description, amount
        # Let's do some fuzzy matching for column names to make it robust
        col_mapping = {
            'date': None,
            'description': None,
            'amount': None
        }
        
        for col in df.columns:
            col_lower = col.lower()
            if not col_mapping['date'] and any(kw in col_lower for kw in ['date', 'time', 'on']):
                col_mapping['date'] = col
            elif not col_mapping['description'] and any(kw in col_lower for kw in ['desc', 'narrative', 'details', 'particulars', 'payee', 'merchant']):
                col_mapping['description'] = col
            elif not col_mapping['amount'] and any(kw in col_lower for kw in ['amount', 'price', 'cost', 'debit', 'withdrawal', 'value']):
                col_mapping['amount'] = col
                
        # If we couldn't find the columns, raise an error
        if not all(col_mapping.values()):
            raise ValueError(f"Could not automatically detect columns for Date, Description, and Amount in the CSV. Found columns: {list(df.columns)}")
            
        # Extract the relevant data
        processed_data = []
        for _, row in df.iterrows():
            date_val = str(row[col_mapping['date']])
            desc_val = str(row[col_mapping['description']])
            amount_val = row[col_mapping['amount']]
            
            # Clean up amount (remove currency symbols, commas if present)
            try:
                if isinstance(amount_val, str):
                    amount_val = float(amount_val.replace('$', '').replace('€', '').replace('₹', '').replace(',', '').strip())
                else:
                    amount_val = float(amount_val)
                    
                # We only want to track expenses (often represented as positive numbers in 'Debit' columns, or negative in 'Amount' columns)
                # Let's assume absolute value for simplicity in an expense tracker if it's a debit
                amount_val = abs(amount_val)
                
            except ValueError:
                continue # Skip rows with invalid amounts
                
            category = mock_ai_categorize(desc_val)
            
            processed_data.append({
                'date': date_val,
                'description': desc_val,
                'amount': amount_val,
                'category': category
            })
            
        # Insert into DB
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        for item in processed_data:
            c.execute('INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)',
                     (item['date'], item['description'], item['amount'], item['category']))
        conn.commit()
        conn.close()
        
        return True, f"Successfully processed {len(processed_data)} transactions."
    except Exception as e:
        return False, str(e)

@app.route('/')
def dashboard():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Get all expenses ordered by most recent first
    c.execute('SELECT * FROM expenses ORDER BY id DESC')
    expenses = [dict(row) for row in c.fetchall()]
    
    # Get summary data
    c.execute('SELECT category, SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC')
    category_summary = [dict(row) for row in c.fetchall()]
    
    total_spent = sum(row['total'] for row in category_summary)
    
    conn.close()
    
    return render_template('dashboard.html', expenses=expenses, category_summary=category_summary, total_spent=total_spent)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
        
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('dashboard'))
        
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the CSV
        success, message = process_csv(filepath)
        if success:
            flash(message, 'success')
        else:
            flash(f"Error processing CSV: {message}", 'error')
            
        return redirect(url_for('dashboard'))
    else:
        flash('Only CSV files are currently supported.', 'error')
        return redirect(url_for('dashboard'))
        
@app.route('/api/chart-data')
def chart_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = c.fetchall()
    conn.close()
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    
    return jsonify({
        'labels': labels,
        'values': values
    })

@app.route('/clear', methods=['POST'])
def clear_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM expenses')
    conn.commit()
    conn.close()
    flash('All data cleared successfully.', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
