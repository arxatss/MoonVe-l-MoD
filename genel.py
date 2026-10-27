from threading import Thread
import os
import discord
from discord.ext import commands
from flask import Flask

# --- Render Uptime için Flask Sunucusu ---
app = Flask('')

@app.route('/')
def home():
    return 'Bot aktif ve çalışıyor!'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- Temel Bot Yapısı ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} başarıyla giriş yaptı ve aktif!')

# --- Botu Çalıştırma ---
keep_alive()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
