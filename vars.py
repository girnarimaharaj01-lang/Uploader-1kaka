#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29777466"))
API_HASH = environ.get("API_HASH", "a04b3df726520026f207079aec2f9879")
BOT_TOKEN = environ.get("BOT_TOKEN", "8346695576:AAErSTkMH1Jcb-yK0nE2gKCuSorGg0OhQMI")

OWNER = int(environ.get("OWNER", "8399557684"))
CREDIT = environ.get("CREDIT", "(⁠*⁠sitaram⁠*⁠) ❣️")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8399557684').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8399557684').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set













