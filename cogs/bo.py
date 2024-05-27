import random

from discord import Message
from discord.ext import commands
from helpers.webhook import send_webhook_message


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
            
            await send_webhook_message(
                bot=self.bot, message=ctx, 
                content=content, 
                webhooks_cache=self.webhooks_cache
            )

async def setup(bot):
    await bot.add_cog(Bo(bot))