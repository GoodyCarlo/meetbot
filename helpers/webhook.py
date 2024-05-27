from discord import Webhook, Message


async def get_or_create_webhook(channel, webhooks_cache, bot):
    # Check if the webhook is already cached
    if channel.id in webhooks_cache:
        return webhooks_cache[channel.id]

    # Get existing webhooks in the channel
    webhooks = await channel.webhooks()
    webhook:Webhook
    
    for webhook in webhooks:
        if webhook.name == "webhook_replacer" and webhook.user == bot:
            webhooks_cache[channel.id] = webhook
            return webhook

    # Create a new webhook if none found
    webhook = await channel.create_webhook(name="webhook_replacer")
    webhooks_cache[channel.id] = webhook
    
    return webhook

async def send_webhook_message(bot, message: Message, content: str, webhooks_cache: dict):
    """Generic function to send a webhook message

    Args:
        bot (discord.ext.commands.bot.Bot): Discord bot.
        message (Message): The original message that sent the command.
        content (str): The reply of the bot.
        webhooks_cache (dict): Dictionary of channel information.
    """
    
    webhook = await get_or_create_webhook(message.channel, webhooks_cache, bot)
    
    await message.delete()
    await webhook.send(content, username=message.author.name, avatar_url=message.author.avatar.url)
