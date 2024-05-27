import discord
from discord import app_commands, Interaction, Message, utils, Webhook
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import random

from helpers.webhook import get_or_create_webhook
class Bo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.webhooks_cache = {}

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return

        if ctx.content.__contains__('$bo') and not ctx.content.__contains__('`$bo`'):
            # Sends a random bo angle to wherever `$bo` was sent
            replies = ['Bo Ang', 'Bo Logo', 'Bo Lok', 'Bo Gok']
            random_reply = random.choice(replies)
            content = ctx.content.replace("$bo", random_reply)
            webhook = await get_or_create_webhook(ctx.channel, self.webhooks_cache, self.bot)
            await ctx.delete()
            await webhook.send(content,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            # await ctx.channel.send(content=content)

async def setup(bot):
    await bot.add_cog(Bo(bot))