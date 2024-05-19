import discord
from discord import app_commands, Interaction, Message, utils
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Ensure this intent is enabled for fetching messages
bot = commands.Bot(command_prefix='$', intents=intents)
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


@bot.event
async def on_message(ctx:Message):
        # we do not want the bot to reply to itself
        if ctx.author.bot:
            return
        
        if ctx.content.startswith('$nerd'):
            if ctx.reference != None:
                message = await fetch_message_in_channel(ctx.channel,ctx.reference.message_id)
                # webhook = await message.channel.create_webhook(name="gay")

                # ret = await webhook.send("🤓 ☝️",username=ctx.author.name,avatar_url=ctx.author.avatar.url,wait=True)
                await message.reply("🤓 ☝️", mention_author=False)
                await ctx.delete()
            else:
                await ctx.reply('Hello!', mention_author=True)
        
        if ctx.content.__contains__('twitter.com') and not ctx.content.__contains__('fxtwitter'):
            webhook = await ctx.channel.create_webhook(name="gayest")
            reply = ctx.content.replace("twitter","fxtwitter")
            await webhook.send(reply,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

        if ctx.content.__contains__('x.com') and not ctx.content.__contains__('fxtwitter'):
            webhook = await ctx.channel.create_webhook(name="gayest")
            reply = ctx.content.replace("x","fxtwitter")
            await webhook.send(reply,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

        if ctx.content.__contains__('instagram.com') and not ctx.content.__contains__('ddinstagram'):
            webhook = await ctx.channel.create_webhook(name="gayer")
            reply = ctx.content.replace("instagram","ddinstagram")
            await webhook.send(reply,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

bot.run(TOKEN)
