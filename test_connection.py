import requests
import sys

api_key = "120e8ca156920dd61f4c98bc6628a2cb"
movie_id = 19995 # Avatar, usually reliable
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    print(f"Testing connection with User-Agent and verify=False...")
    response = requests.get(url, timeout=10, headers=headers, verify=False)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Response JSON key check:", list(response.json().keys())[:5])
    else:
        print("Failed request. Response text:")
        print(response.text[:200])
except Exception as e:
    print(f"EXCEPTION OCCURRED: {e}")
