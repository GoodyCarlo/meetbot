from discord import Message
from discord.ext import commands


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