import os
import requests
import socket

print("Checking Proxy Environment Variables:")
for key in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
    print(f"{key}: {os.environ.get(key)}")

print("\nResolving api.themoviedb.org:")
try:
    ip = socket.gethostbyname("api.themoviedb.org")
    print(f"Resolved to: {ip}")
except Exception as e:
    print(f"DNS Resolution Failed: {e}")

print("\nTesting Google.com (General HTTPS):")
try:
    response = requests.get("https://google.com", timeout=5)
    print(f"Google Status: {response.status_code}")
except Exception as e:
    print(f"Google Failed: {e}")
