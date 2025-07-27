from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "12380656"))
    API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "gjvk")
    BASE_URL = getenv("BASE_URL", "fff").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://aman727587:aman@cluster0.uyhcsfm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002114619001").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "aman")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "aman")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
