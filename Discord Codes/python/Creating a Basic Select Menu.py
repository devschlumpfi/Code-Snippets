import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def selectmenu(ctx):
    select = discord.ui.Select(
        placeholder='Select an option',
        options=[
            discord.SelectOption(label='Option 1', value='option1'),
            discord.SelectOption(label='Option 2', value='option2')
        ]
    )

    await ctx.send('Please select an option:', view=select)

@bot.event
async def on_select_option(interaction):
    selected_value = interaction.data['values'][0]

    if selected_value == 'option1':
        await interaction.response.send_message('You selected Option 1.')
    elif selected_value == 'option2':
        await interaction.response.send_message('You selected Option 2.')

bot.run('YOUR_BOT_TOKEN')
