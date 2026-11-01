from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # Super secret admin panel that nobody can get access to
    return render_template("admin.html")


app.run(host="0.0.0.0", port=8081)