@bot.event
async def on_message(message):
    if 'thumbs up' in message.content.lower():
        await message.add_reaction('👍')
