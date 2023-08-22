@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello, {message.author.mention}!')
