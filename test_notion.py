import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)

try:
    response = notion.databases.retrieve(database_id=DATABASE_ID)
    title = response["title"][0]["plain_text"]
    print("Titre de la base :", title)
except Exception as e:
    print("Erreur lors de la récupération de la base :", e)
