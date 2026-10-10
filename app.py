from flask import Flask, render_template, request

app = Flask(__name__)

# Global list to store calculation strings in memory
HISTORY_LOG = []

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    error_message = ""
    
    if request.method == "POST":
        try:
            num1_raw = request.form.get("num1")
            num2_raw = request.form.get("num2")
            operation = request.form.get("operation")
            
            if not num1_raw or not num2_raw:
                error_message = "Error: All input fields must be filled out."
            else:
                num1 = float(num1_raw)
                num2 = float(num2_raw)
                
                # Math Processing
                if operation == "add":
                    result = num1 + num2
                    op_sign = "+"
                elif operation == "subtract":
                    result = num1 - num2
                    op_sign = "-"
                elif operation == "multiply":
                    result = num1 * num2
                    op_sign = "×"
                elif operation == "divide":
                    if num2 == 0:
                        error_message = "Error: Cannot divide by zero!"
                    else:
                        result = num1 / num2
                        op_sign = "÷"
                
                # If calculation succeeded, save it into our memory log array
                if not error_message:
                    log_entry = f"{num1} {op_sign} {num2} = {result}"
                    # Insert at the beginning so the newest calculation is on top
                    HISTORY_LOG.insert(0, log_entry)
                        
        except ValueError:
            error_message = "Error: Please input valid numbers only."
            
    # Send both the single result and the full history list to our web page
    return render_template("index.html", result=result, error=error_message, history=HISTORY_LOG)

if __name__ == "__main__":
    app.run(debug=True)