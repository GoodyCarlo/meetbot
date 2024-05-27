from discord import Webhook
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