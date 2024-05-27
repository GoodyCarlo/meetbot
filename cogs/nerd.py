import discord
from discord import app_commands, Interaction, Message, utils, Webhook
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import random

from helpers.webhook import get_or_create_webhook
class Nerd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return
        
        if ctx.content.startswith('$nerd'):
            if ctx.reference is not None:
                referenced_message = await ctx.channel.fetch_ctx(ctx.reference.ctx_id)
                await referenced_message.reply("🤓 ☝️", mention_author=False)
                await ctx.delete()
            else:
                await ctx.reply('Nah!', mention_author=True)

async def setup(bot):
    await bot.add_cog(Nerd(bot))