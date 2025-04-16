from flask import Flask, request, redirect, url_for, render_template
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Your database connection details
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="contact_db"# Replace with your DB name
        user="postgres",
        password="5432"  # Use your actual password
    )

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO contact_form (name, email, subject, message)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (name, email, subject, message))
        conn.commit()
        cur.close()
        conn.close()
        return "Message sent successfully!"  # You can redirect or render a thank-you page here
    except Exception as e:
        return f"An error occurred: {e}"
