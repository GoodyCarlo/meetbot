from discord import Message
from discord.ext import commands
from helpers.webhook import send_webhook_message


class Shitpost(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.webhooks_cache = {}
        self.link_replacements = {
            'twitter.com': 'fxtwitter.com',
            'x.com': 'fxtwitter.com',
            'instagram.com': 'ddinstagram.com'
        }

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return
        
        content = ctx.content
        reply = None
        
        for original, replacement in self.link_replacements.items():
            if original in content and replacement not in content:
                reply = content.replace(original, replacement)
                break
        
        if reply is None:
            return
        
        await send_webhook_message(
            bot=self.bot, message=ctx, 
            content=reply, 
            webhooks_cache=self.webhooks_cache
        )

async def setup(bot):
    await bot.add_cog(Shitpost(bot))