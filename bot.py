import logging
from telegram.ext import ApplicationBuilder
import asyncio
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is active"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run_web)
    t.start()

TOKEN = "8998358080:AAF-Npc7oFHAqv1NwhAepnXfr1UNFnb4V5M"

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    print("Bot is running...")
    await application.run_polling()

if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
