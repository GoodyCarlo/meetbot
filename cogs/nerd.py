from discord import Message
from discord.ext import commands


class Nerd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # TODO: naixsu
    # use handle_command() when /alias is implemented
    # plan is `\alias $<alias> "<message>" "<message2>"`
    # `alias` is the desired command
    # `message` is the first message when $alias is called
    # `message2` is the second message when there is a reference
    async def handle_command(self, ctx: Message, reply_text: str, default_reply: str):
        if ctx.reference is not None:
            referenced_message = await ctx.channel.fetch_message(ctx.reference.message_id)
            await ctx.delete()
            await referenced_message.reply(reply_text, mention_author=False)
        else:
            await ctx.reply(default_reply, mention_author=True)

    @commands.Cog.listener()
    async def on_message(self, ctx: Message):
        if ctx.author.bot:
            return
        
        if ctx.content.startswith('$nerd'):
            await self.handle_command(ctx, "🤓☝️", "Nah!")
        
        if ctx.content.startswith('$ulol'):
            await self.handle_command(ctx, "😄☝️", "😄☝️")


async def setup(bot):
    await bot.add_cog(Nerd(bot))