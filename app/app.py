from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

from flask import Flask, request

@app.route("/fetch")
def fetch():
    import requests
    url = request.args.get("url", "").strip()
    if not url:
        return "Provide a url parameter.\n", 400
    try:
        r = requests.get(url, timeout=5)
        return r.text[:4096], 200, {"Content-Type": "text/plain"}
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}\n", 502

app.run(host="0.0.0.0", port=8080)