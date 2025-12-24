import requests

print("Testing HTTP details...")
try:
    response = requests.get("http://api.themoviedb.org/3/movie/550?api_key=120e8ca156920dd61f4c98bc6628a2cb", timeout=10)
    print(f"Final Info:")
    print(f"Status: {response.status_code}")
    print(f"URL: {response.url}")
    print(f"History: {response.history}")
    print(f"Content excerpt: {response.text[:100]}")
except Exception as e:
    print(f"Failed: {e}")
