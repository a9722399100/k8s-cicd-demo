from flask import Flask
app = Flask(__name__)

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/")
def index():
    return "Hello from CI/CD Demo!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
