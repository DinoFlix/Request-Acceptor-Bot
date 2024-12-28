from os import environ

API_ID = int(environ.get("API_ID", "21335208"))
API_HASH = environ.get("API_HASH", "4cb201499c03fe54f817617d27b336aa")
BOT_TOKEN = environ.get("BOT_TOKEN", "7709792728:AAGfZ0LpwDM3FAy1THeTUrP6Je-rWlGkrNE")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002354059393"))
ADMINS = int(environ.get("ADMINS", "1577166444"))
DB_URI = environ.get("DB_URI", "mongodb+srv://thomusoro9:thomus@cluster0.molki.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "thomusoro9")
