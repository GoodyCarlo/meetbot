import discord
from discord import app_commands, Interaction
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Ensure this intent is enabled for fetching messages
bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree  # Use the bot's command tree


async def fetch_message_in_channel(channel: discord.TextChannel, message_id: int) -> discord.Message:
    try:
        message = await channel.fetch_message(message_id)
        return message
    except (discord.NotFound, discord.Forbidden):
        return None

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1181092923564109934))
    print("Ready!")

@tree.command(
    name="nerd",
    description="fucking nerd",
    guild=discord.Object(id=1181092923564109934)
)
@app_commands.describe(msg="The ID of the message to reply to")
async def first_command(interaction: Interaction, msg: str = None):
    await interaction.response.defer(ephemeral=True)
    
    if msg:
        try:
            message_id = int(msg)
            message = await fetch_message_in_channel(interaction.channel, message_id)
            if message:
                await message.reply("🤓 ☝️")
                await interaction.followup.send(f"Replied to the message with ID {message_id}.", ephemeral=True)
            else:
                await interaction.followup.send("Message not found.", ephemeral=True)
        except ValueError:
            await interaction.followup.send("Invalid message ID.", ephemeral=True)
    else:
        await interaction.followup.send("🤓 ☝️", ephemeral=True)

bot.run(TOKEN)
