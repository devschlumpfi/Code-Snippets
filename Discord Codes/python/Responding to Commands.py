@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f'Pong! Latency: {latency:.2f}ms')
