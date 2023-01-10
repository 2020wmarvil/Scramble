import discord
from discord.ext import commands
from discord.ext.commands import Bot

from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('.env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')

print(BOT_TOKEN)