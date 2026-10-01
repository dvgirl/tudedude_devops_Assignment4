from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def home():
    return "Git & GitHub Assignment"
@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Flask",
        "status": "success"
    })
if __name__ == "__main__":
    app.run(debug=True)
