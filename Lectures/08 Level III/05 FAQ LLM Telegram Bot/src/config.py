import os

ADMINS_USERNAME = [
    username.strip().lower() for username in os.getenv("ADMINS_USERNAME", "").split(",")
]
APPROVED_CHATS = [chat.strip().lower() for chat in os.getenv("APPROVED_CHATS", "").split(",")]
