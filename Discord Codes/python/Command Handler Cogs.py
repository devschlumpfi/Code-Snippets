import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

status = discord.Status.online
activity = discord.Activity(type=discord.ActivityType.playing, name=":O")


client = commands.Bot(
    intents=intents,
    status=status,
    activity=activity,
    command_prefix="-",
)




@client.event
async def on_ready():
    print(f"{client.user} Online")
    await client.tree.sync()

async def funktion():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(funktion())






load_dotenv()
client.run(os.getenv("TOKEN"))

#from lucky