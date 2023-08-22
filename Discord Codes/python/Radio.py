############################################
# Discord Radio Bot
# Author: @InvalidJoker
# Version: 1.0
# Diese Nachricht darf nicht entfernt werden!
############################################
from discord.ext import tasks
import discord
import asyncio

CHANNEL = 1052660703267393567

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL)
    
    await channel.connect()
    channel.guild.voice_client.play(discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio16.mp3"))
    check_music.start()
    auto_restart.start()
    print("The Radio is online!")
    
@tasks.loop(seconds=60)
async def check_music():
    channel = bot.get_channel(CHANNEL)
    
    if channel.guild.voice_client is None:
        await channel.connect()
        channel.guild.voice_client.play(discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio16.mp3"))
        
    if channel.guild.voice_client.is_playing() == False:
        channel.guild.voice_client.play(discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio16.mp3"))

@tasks.loop(hours=24)
async def auto_restart():
    channel = bot.get_channel(CHANNEL)
    
    if channel.guild.voice_client:
        check_music.stop()
        await channel.guild.voice_client.disconnect()
        asyncio.sleep(5)
        await channel.connect()
        channel.guild.voice_client.play(discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio16.mp3"))
        check_music.start()  
        
bot.run("TOKEN")