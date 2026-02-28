from flask import Flask
app=Flask(__name__)

@app.route("/")

def home():
    return "SentinLX is running"

if __name__ == "__main __":
    app.run(debug=True)