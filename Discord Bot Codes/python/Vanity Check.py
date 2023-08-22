#from Marcel

GUILD = 1234 # Server, auf dem der Bot die Rolle vergeben soll
STATUS_ROLE = 1234 # Rolle die vergeben werden soll, wenn der User den entsprechenden Status hat
STATUS_TEXT = "TEXT" # Status, den der User haben muss
LOG_CHANNEL = 1234 # In dem channel wird geloggt

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    vanity_task.start()

async def has_vanity(member: discord.Member):
    if not len(member.activities) == 0:
        for i in member.activities:
            if isinstance(i, discord.CustomActivity):
                if STATUS_TEXT in i.name or STATUS_TEXT == i.name:
                    return True

    else:
        return False


@tasks.loop(minutes=1)
async def vanity_task():
    await bot.wait_until_ready()

    guild: discord.Guild = bot.get_guild(GUILD)
    role = guild.get_role(STATUS_ROLE)
    log = bot.get_channel(LOG_CHANNEL)

    if guild.members:
        for member in guild.members:
            if member.bot:
                continue
            vanity = await has_vanity(member)
            if vanity:
                if not role in member.roles:
                    await member.add_roles(role, atomic=True)
                    embed = discord.Embed(
                        title="Vanity-Rolle hinzugefügt!",
                        description=f"{member.mention} hat die Vanity-Rolle {role.mention} erhalten.", 
                        color=discord.Color.green()
                        )
                    await log.send(embed=embed)

            else:
                if role in member.roles:
                    await member.remove_roles(role, atomic=True)
                    embed = discord.Embed(
                        title="Vanity-Rolle entfernt!",
                        description=f"{member.mention} hat die Vanity-Rolle {role.mention} entfernt bekommen.",
                        color=discord.Color.red()
                        )
                    await log.send(embed=embed)