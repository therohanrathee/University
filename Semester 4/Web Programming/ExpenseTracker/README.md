# 📊 Lumina Finance - AI Expense Tracker

## 👨‍🎓 Student Details

* **Name:** Rohan Rathee
* **Roll Number:** 2401010144
* **Course:** Web Programming
* **Branch:** B.Tech CSE Core

---

This repository contains the source code for **Lumina Finance**, a modern, AI-powered expense tracking web application. The project was built using Python (Flask) for the backend and Vanilla HTML/CSS/JS for the frontend, featuring a beautiful glassmorphism aesthetic.

## 📂 Project Structure

```bash
app.py               # Main Flask application file and API routes
requirements.txt     # Python dependencies for the project
templates/           # HTML files
  ├── base.html      # Base layout template
  └── dashboard.html # Main dashboard view
static/              # Static assets
  ├── style.css      # Vanilla CSS styling with glassmorphism
  └── script.js      # Client-side JavaScript for file upload & Chart.js
```

## 🧠 Concepts Covered

* **Backend Web Development:** Using Flask to handle routes, file uploads, and server-side logic.
* **Database Management:** Integrating SQLite3 to persistently store parsed transaction data.
* **Data Processing:** Utilizing the Pandas library to dynamically parse and clean CSV bank statements.
* **Algorithm Design:** Building a smart keyword-based categorization engine to mock an AI classification model.
* **Frontend UI/UX:** Designing a responsive dashboard using Vanilla CSS, Glassmorphism, CSS Grid/Flexbox, and dynamic chart rendering with Chart.js.

## ⚙️ Requirements

* Python 3.x
* Flask (`pip install Flask`)
* Pandas (`pip install pandas`)
* Werkzeug (`pip install Werkzeug`)

## ▶️ How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the project directory:

```bash
cd ExpenseTracker
```

3. (Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
# venv\Scripts\activate  # On Windows
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the Flask development server:

```bash
python app.py
```

6. Open your browser and go to `http://127.0.0.1:5000`.

## 📊 Features

* **Smart File Upload:** Drag and drop your bank statement (CSV format). The application uses Pandas to intelligently detect the date, description, and amount columns.
* **Auto-Categorization Engine:** The system automatically categorizes transactions into distinct categories (e.g., Food & Dining, Transportation, Shopping, Utilities) based on a smart rules engine.
* **Interactive Analytics:** Visualizes your spending data using interactive charts and summary cards.
* **Dark Mode & Glassmorphism:** Features a highly polished, responsive dark theme.

## 📌 Note

* A `sample_bank_statement.csv` is included in the repository so you can test the file upload functionality immediately.
* Designed and built entirely as a solo university project.

---

⭐ *Prepared as Part of Academic Coursework*
