from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    operation = request.form["operation"]
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
