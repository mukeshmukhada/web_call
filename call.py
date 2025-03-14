from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)
url = "https://flask-test-2-38ul.onrender.com/logs"  # Change this to the website you want to call

def call_website():
    while True:
        try:
            response = requests.get(url)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}")
        time.sleep(60)

@app.route('/')
def home():
    return jsonify({"message": "Website caller is running"})

if __name__ == "__main__":
    thread = threading.Thread(target=call_website, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5000)
