from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        # Get the input values from the web page form
        num1 = float(request.form.get("num1", 0))
        num2 = float(request.form.get("num2", 0))
        operation = request.form.get("operation")
        
        # Perform the basic calculation logic
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Error (Divide by zero)"
            
    return f"""
    <html>
        <body>
            <h2>Basic Python Calculator</h2>
            <form method="POST">
                <input type="number" name="num1" step="any" required>
                <select name="operation">
                    <option value="add">+</option>
                    <option value="subtract">-</option>
                    <option value="multiply">*</option>
                    <option value="divide">/</option>
                </select>
                <input type="number" name="num2" step="any" required>
                <button type="submit">=</button>
            </form>
            <h3>Result: {result}</h3>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
