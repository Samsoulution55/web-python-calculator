from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    error_message = "" # Added to track issues safely
    
    if request.method == "POST":
        try:
            # 1. Capture and convert raw text input safely
            num1_raw = request.form.get("num1")
            num2_raw = request.form.get("num2")
            operation = request.form.get("operation")
            
            # 2. Defensive check: Did the user leave fields blank?
            if not num1_raw or not num2_raw:
                error_message = "Error: All input fields must be filled out."
            else:
                num1 = float(num1_raw)
                num2 = float(num2_raw)
                
                # 3. Process calculations with custom validation rule loops
                if operation == "add":
                    result = num1 + num2
                elif operation == "subtract":
                    result = num1 - num2
                elif operation == "multiply":
                    result = num1 * num2
                elif operation == "divide":
                    if num2 == 0:
                        error_message = "Error: Cannot divide by zero!"
                    else:
                        result = num1 / num2
                        
        except ValueError:
            # Catch instances where inputs aren't valid numeric decimal values
            error_message = "Error: Please input valid numbers only."
            
    return render_template("index.html", result=result, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)