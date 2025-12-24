import requests

print("Testing HTTP (non-S) connectivity to TMDB...")
try:
    # Try HTTP, it should redirect to HTTPS usually, but let's see if we get *any* response
    response = requests.get("http://api.themoviedb.org/3/movie/550?api_key=120e8ca156920dd61f4c98bc6628a2cb", timeout=10)
    print(f"HTTP Status: {response.status_code}")
except Exception as e:
    print(f"HTTP Failed: {e}")
