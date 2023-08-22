@bot.command()
async def embed(ctx):
    embed = discord.Embed(
        title='Embed Example',
        description='This is an example of an embed message.',
        color=discord.Color.blue()
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
