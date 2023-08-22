import discord
from discord.ext import commands


intents = discord.Intents.default()

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the bot
bot.run('YOUR_BOT_TOKEN')
