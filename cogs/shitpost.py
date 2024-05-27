import discord
from discord import app_commands, Interaction, Message, utils, Webhook
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import random

from helpers.webhook import get_or_create_webhook
class Shitpost(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.webhooks_cache = {}

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return

        if ctx.content.__contains__('twitter.com') and not ctx.content.__contains__('fxtwitter'):
            webhook = await get_or_create_webhook(ctx.channel, self.webhooks_cache, self.bot)
            reply = ctx.content.replace("twitter","fxtwitter")
            await webhook.send(reply,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

        if ctx.content.__contains__('x.com') and not ctx.content.__contains__('fxtwitter'):
            webhook = await get_or_create_webhook(ctx.channel, self.webhooks_cache, self.bot)
            reply = ctx.content.replace("x","fxtwitter")
            await webhook.send(reply,username=ctx.author.nick,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

        if ctx.content.__contains__('instagram.com') and not ctx.content.__contains__('ddinstagram'):
            webhook = await get_or_create_webhook(ctx.channel, self.webhooks_cache, self.bot)
            reply = ctx.content.replace("instagram","ddinstagram")
            await webhook.send(reply,username=ctx.author.name,avatar_url=ctx.author.avatar.url)
            await ctx.delete()

async def setup(bot):
    await bot.add_cog(Shitpost(bot))