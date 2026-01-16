import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "27297131"))
API_HASH = os.environ.get("API_HASH", "9fdd19cc4433056a425c9a042ffe8ba0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7734613248:AAEYaP0nIL8lH9OG2RviVUNFa9otspcZXc8")

CREDIT = os.environ.get("CREDIT", "𝗩𝗔𝗦𝗨𝗗𝗘𝗩")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "7514808135"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "8232691888").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = "https://t.me/+l186M_g6vWRhMjFl"
# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://i.ibb.co/v6Vr7HCt/1000003297.jpg").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}






