import json
import os
from notion_client import Client

def load_env():
    from dotenv import load_dotenv
    load_dotenv()

def load_client_config():
    with open("config/clients.json") as f:
        return json.load(f)

def deploy_template(client_data):
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    # Simule la duplication d'un template
    print(f"Déploiement de l’espace pour {client_data['name']}... (simulation)")
    # Tu pourrais ici appeler une API Notion réelle pour dupliquer une page modèle

def main():
    load_env()
    clients = load_client_config()
    for client in clients:
        deploy_template(client)

if __name__ == "__main__":
    main()
