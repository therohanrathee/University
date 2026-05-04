from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Expense {self.description}>'

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        category = request.form.get('category')
        
        if not description or not amount or not category:
            flash('All fields are required!', 'error')
            return redirect(url_for('add_expense'))
        
        try:
            amount = float(amount)
            if amount <= 0:
                flash('Amount must be greater than 0!', 'error')
                return redirect(url_for('add_expense'))
            
            expense = Expense(description=description, amount=amount, category=category)
            db.session.add(expense)
            db.session.commit()
            flash('Expense added successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid amount entered!', 'error')
            return redirect(url_for('add_expense'))
    
    return render_template('add_expense.html')

@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/category/<category>')
def category_expenses(category):
    expenses = Expense.query.filter_by(category=category).order_by(Expense.date.desc()).all()
    total = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total=total, category=category)

if __name__ == '__main__':
    app.run(debug=True)