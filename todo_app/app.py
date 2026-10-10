from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global list acting as our database memory array for tasks
TODO_LIST = []

@app.route("/", methods=["GET", "POST"])
def todo_home():
    if request.method == "POST":
        task_content = request.form.get("task")
        
        # Validation: Only add if the input box isn't empty string spaces
        if task_content and task_content.strip() != "":
            TODO_LIST.append(task_content.strip())
            
    return render_template("index.html", tasks=TODO_LIST)

@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    # Defensive programming: make sure index exists before popping
    if 0 <= task_index < len(TODO_LIST):
        TODO_LIST.pop(task_index)
    return redirect(url_for("todo_home"))

if __name__ == "__main__":
    app.run(debug=True)