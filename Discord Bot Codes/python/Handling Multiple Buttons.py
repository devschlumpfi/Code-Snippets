import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def buttons(ctx):
    button1 = discord.ui.Button(style=discord.ButtonStyle.primary, label="Button 1", custom_id="button1")
    button2 = discord.ui.Button(style=discord.ButtonStyle.secondary, label="Button 2", custom_id="button2")

    await ctx.send("Click the buttons below:", view=discord.ui.View().add_item(button1).add_item(button2))

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == "button1":
        await interaction.response.send_message("Button 1 clicked!")
    elif interaction.custom_id == "button2":
        await interaction.response.send_message("Button 2 clicked!")

bot.run('YOUR_BOT_TOKEN')
