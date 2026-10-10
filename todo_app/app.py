from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# This helper function connects to our database file and creates the table if it doesn't exist
def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    # Create a table called 'tasks' with a tracking ID and text content column
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialize the database file on the hard drive immediately when the app starts
init_db()

@app.route("/", methods=["GET", "POST"])
def todo_home():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    if request.method == "POST":
        task_content = request.form.get("task")
        if task_content and task_content.strip() != "":
            # INSERT: Save the task text securely inside the database table file
            cursor.execute("INSERT INTO tasks (content) VALUES (?)", (task_content.strip(),))
            conn.commit()
            
    # SELECT: Fetch all saved tasks out of the database file rows
    cursor.execute("SELECT id, content FROM tasks")
    database_tasks = cursor.fetchall()
    conn.close()
    
    return render_template("index.html", tasks=database_tasks)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    # DELETE: Erase the specific row matching the target tracking ID number
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("todo_home"))

if __name__ == "__main__":
    app.run(debug=True)