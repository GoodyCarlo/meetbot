import discord
from discord import app_commands, Interaction, Message, utils, Webhook
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import random

from helpers.webhook import send_webhook_message
class Shitpost(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.webhooks_cache = {}
        self.link_replacements = {
            'twitter.com': 'fxtwitter',
            'x.com': 'fxtwitter',
            'instagram.com': 'ddinstagram'
        }

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return
        
        content = ctx.content
        
        for original, replacement in self.replacements.items():
            if original in content and replacement not in content:
                reply = content.replace(original, replacement)
                break

        await send_webhook_message(
            bot=self.bot, message=ctx, 
            content=reply, 
            webhooks_cache=self.webhooks_cache
        )

async def setup(bot):
    await bot.add_cog(Shitpost(bot))