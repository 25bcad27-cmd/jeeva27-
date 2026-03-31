from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            college TEXT,
            event TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Register user
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    college = request.form["college"]
    event = request.form["event"]

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO registrations (name, email, phone, college, event) VALUES (?, ?, ?, ?, ?)",
        (name, email, phone, college, event)
    )
    conn.commit()
    conn.close()

    return redirect("/")

# View all registrations
@app.route("/view")
def view():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM registrations").fetchall()
    conn.close()
    return render_template("view.html", users=users)

# Run for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
