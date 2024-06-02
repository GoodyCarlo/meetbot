from discord import Message
from discord.ext import commands


class Ulol(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx:Message):

        if ctx.author.bot:
            return
        
        if ctx.content.startswith('$ulol'):
            if ctx.reference is not None:
                referenced_message = await ctx.channel.fetch_message(ctx.reference.message_id)
                await ctx.delete()
                await referenced_message.reply("😄☝️", mention_author=False)
            else:
                await ctx.reply("😄☝️", mention_author=True)

async def setup(bot):
    await bot.add_cog(Ulol(bot))