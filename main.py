import discord
import os
import asyncio

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Ready!")

async def main():
    async with bot:
        await bot.load_extension('cogs.bo')
        await bot.load_extension('cogs.nerd')
        await bot.load_extension('cogs.shitpost')
        await bot.start(TOKEN)

asyncio.run(main())