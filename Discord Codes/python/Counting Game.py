import discord
import asyncio
# nur nötig wenn connect hier in der selben datei ist
# import contextlib

from discord import InputTextStyle
from discord.ext.commands import MissingPermissions
from discord.ext import commands, tasks
from discord.ui import Button, View, Modal, InputText
from discord.commands import Option, slash_command, SlashCommandGroup

# from utils.funcs import get_config
# from utils.funcs import connect
# from utils.funcs import get_database_tables

### {list(get_database_tables())[5]} das ist "counting"
# connect ist:
# @contextlib.asynccontextmanager
# async def connect():
#     conn = await aiomysql.connect(
#         host=get_config("mysql")["host"],
#         user=get_config("mysql")["user"],
#         password=get_config("mysql")["password"],
#         db=get_config("mysql")["database"],
#         autocommit=True
#     )
#     async with conn.cursor() as cur:
#         yield conn, cur
#     conn.close()
# 
# Datenbank structure
# "guild_id": "BIGINT",
# "counting_channel_id": "BIGINT",
# "score": "BIGINT",
# "highscore": "BIGINT",
# "last_user": "BIGINT",
# "fail_role": "BIGINT",
# "only_numbers": "BOOLEAN"


class counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    counting_cmd = SlashCommandGroup(name="counting", description="All counting commands", guild_only=True)

    @counting_cmd.command()
    async def setchannel(self, ctx, channel: Option(discord.abc.GuildChannel, "Choose a Welcome Channel")):
        async with connect() as (conn, cur):
            await cur.execute(f"SELECT counting_channel_id FROM {list(get_database_tables())[5]} WHERE guild_id = {ctx.guild.id}")
            result_channel = await cur.fetchone()
            if not result_channel:
                await cur.execute(f"INSERT INTO `counting`(`guild_id`, `counting_channel_id`, `score`, `highscore`, `last_user`, `only_numbers`) VALUES ('{ctx.guild.id}','{channel.id}','1','0','0','0')")
            else:
                await cur.execute(f"UPDATE `counting` SET `counting_channel_id`='{channel.id}' WHERE guild_id = {ctx.guild.id}")
            return await ctx.respond(f"Der Counting-Channel wurde auf {channel.mention} Gesetzt", ephemeral=True)

    @counting_cmd.command()
    async def next(self, ctx):
        async with connect() as (conn, cur):
            await cur.execute(f"SELECT counting_channel_id FROM {list(get_database_tables())[5]} WHERE guild_id = {ctx.guild.id}")
            result_channel = await cur.fetchone()
            if not result_channel:
                return await ctx.respond(f"Nutze vorher /counting setchannel", ephemeral=True)
            await cur.execute(f"SELECT score FROM {list(get_database_tables())[5]} WHERE guild_id = {ctx.guild.id}")
            next_int = await cur.fetchone()
            await cur.execute(f"SELECT last_user FROM {list(get_database_tables())[5]} WHERE guild_id = {ctx.guild.id}")
            next_user = await cur.fetchone()
            if next_user[0] == 0:
                return await ctx.respond(f"Die nächste Zahl ist {next_int[0]}!", ephemeral=True)
            else:
                return await ctx.respond(f"Die nächste Zahl ist {next_int[0]} und der User <@{next_user[0]}> darf nicht als nächstes Zählen!", ephemeral=True)

    @commands.Cog.listener()
    async def on_message(self, message):
        async with connect() as (conn, cur):
            if message.author.bot:
                return
            await cur.execute(f"SELECT counting_channel_id FROM {list(get_database_tables())[5]} WHERE guild_id = {message.guild.id}")
            result_channel = await cur.fetchone()
            if not result_channel:
                return
            if message.channel.id == result_channel[0]:
                if message.author.bot:
                    return
                await cur.execute(f"SELECT only_numbers FROM {list(get_database_tables())[5]} WHERE guild_id = {message.guild.id}")
                num = await cur.fetchone()
                if num:
                    if not message.content.isnumeric():
                        await asyncio.sleep(2)
                        return await message.delete()
                if not message.content.isnumeric():
                    return
                await cur.execute(f"SELECT last_user FROM {list(get_database_tables())[5]} WHERE guild_id = {message.guild.id}")
                last_user = await cur.fetchone()
                if message.author.id == int(last_user[0]):
                    await cur.execute(f"UPDATE {list(get_database_tables())[5]} SET score = %s, last_user = %s WHERE guild_id = %s", ("1", "0", message.guild.id))
                    await message.add_reaction("❌")
                    channel = self.bot.get_channel(result_channel[0])
                    if channel:
                        return await message.channel.send(F"{message.author.mention} hat die Reihe unterbrochen, da er versucht hat 2 mal hinter einander zu Zählen")
                else:
                    await cur.execute(f"SELECT score FROM {list(get_database_tables())[5]} WHERE guild_id = {message.guild.id}")
                    score_result = await cur.fetchone()
                    if message.content == str(score_result[0]):
                        count = score_result[0] + 1
                        await cur.execute(f"UPDATE {list(get_database_tables())[5]} SET score = %s, last_user = %s WHERE guild_id = %s", (count, message.author.id, message.guild.id))
                        if score_result[0] < count:
                            await cur.execute(f"UPDATE {list(get_database_tables())[5]} SET highscore = %s WHERE guild_id = %s", (message.content, message.guild.id))
                        return await message.add_reaction("✅")
                    else:
                        await cur.execute(f"UPDATE {list(get_database_tables())[5]} SET score = %s, last_user = %s WHERE guild_id = %s", ("1", "0", message.guild.id))
                        return await message.add_reaction("❌")
            else:
                return

def setup(bot):
    bot.add_cog(counting(bot))