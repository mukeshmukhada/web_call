import requests
import time

def call_website(url):
    try:
        response = requests.get(url)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}")

if __name__ == "__main__":
    url = "https://flask-test-2-38ul.onrender.com/"  # Change this to the website you want to call
    while True:
        call_website(url)
        time.sleep(10)
