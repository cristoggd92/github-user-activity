import requests
import sys
from utils import fetch_github_activity

def main(username):
    if not username:
        print("Por favor, proporciona un nombre de usuario de Github")
        return
    
    activity = fetch_github_activity(username)
    if activity:
        print(f"Actividad reciete de {username}:")
        for event in activity:
            print(f" - {event['type']} en {event['repo']['name']}")
        else:
            print(f"No se pudo obtener la actividad para el usuario {username}")
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python mian.pu <nombre de usuario de Github>")
    else:
        main(sys.argv[1])