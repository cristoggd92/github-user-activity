import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos: {response.status_code}")
        return None
        