import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def selectmenu(ctx):
    select1 = discord.ui.Select(
        placeholder='Select option 1',
        options=[
            discord.SelectOption(label='Option A', value='optionA'),
            discord.SelectOption(label='Option B', value='optionB')
        ]
    )

    select2 = discord.ui.Select(
        placeholder='Select option 2',
        options=[
            discord.SelectOption(label='Option X', value='optionX'),
            discord.SelectOption(label='Option Y', value='optionY')
        ]
    )

    await ctx.send('Please select an option from each menu:', view=discord.ui.View().add_item(select1).add_item(select2))

@bot.event
async def on_select_option(interaction):
    selected_value = interaction.data['values'][0]

    if interaction.component.id == 'select1':
        if selected_value == 'optionA':
            await interaction.response.send_message('You selected Option A from select menu 1.')
        elif selected_value == 'optionB':
            await interaction.response.send_message('You selected Option B from select menu 1.')
    elif interaction.component.id == 'select2':
        if selected_value == 'optionX':
            await interaction.response.send_message('You selected Option X from select menu 2.')
        elif selected_value == 'optionY':
            await interaction.response.send_message('You selected Option Y from select menu 2.')

bot.run('YOUR_BOT_TOKEN')
