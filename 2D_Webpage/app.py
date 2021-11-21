from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/task1")
def task1():
    return render_template("task1.html")

@app.route("/task2")
def task2():
    return render_template("task2.html")

@app.route("/task3")
def task3():
    return render_template("task3.html")   


if __name__ == "__main__":
    app.run(debug=True)

