import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def button(ctx):
    button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Click Me!")

    await ctx.send("Click the button below:", view=discord.ui.View().add_item(button))

@bot.event
async def on_button_click(interaction):
    if interaction.custom_id == "button":
        await interaction.response.send_message("Button clicked!")

bot.run('YOUR_BOT_TOKEN')
