import discord
from discord.ext import commands
import aiosqlite
import asyncio
import os

class JoinToCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.init_db()
        self.temp_channels = {}

    def init_db(self):
        async def create_voice_channels_table():
            async with aiosqlite.connect("voice_channels.db") as db:
                await db.execute("""
                    CREATE TABLE IF NOT EXISTS voice_channels (
                        user_id INTEGER PRIMARY KEY,
                        channel_id INTEGER NOT NULL
                    )
                """)
                await db.commit()
        
        self.bot.loop.create_task(create_voice_channels_table())
    



    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel and not before.channel and after.channel.id == 1141202340498645062: #HIER DIE CHANNEL ID VOM VOICE
            async with aiosqlite.connect("voice_channels.db") as db:
                cursor = await db.execute("SELECT * FROM voice_channels WHERE user_id = ?", (member.id,))
                channel_info = await cursor.fetchone()
                if not channel_info:
                    guild = member.guild
                    channel_name = f"{member.name}'s Channel"
                    category = guild.get_channel(1102689340557103215) # HIER DIE CATEGORIE ID 

                    if not category:
                        return print("Channel wurde nicht gefunden")

                    voice_channel = await guild.create_voice_channel(channel_name, category=category)
                    await member.move_to(voice_channel)

                    await db.execute("INSERT INTO voice_channels (user_id, channel_id) VALUES (?, ?)", (member.id, voice_channel.id))
                    await db.commit()
                    if before.channel and len(before.channel.members) == 0:
                        await before.channel.delete()

                    self.temp_channels[member.id] = voice_channel.id

                    view = discord.ui.View()
                    limit_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Limitieren", emoji="👥")
                    rename_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Rename", emoji="✏")
                    sperren_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Sperren", emoji="🔒")
                    entsperren_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Entsperren", emoji="🔓")
                    ban_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Bannen", emoji="🔨")
                    kick_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Kicken", emoji="⛔")
                    rechtevergeben_button = discord.ui.Button(style=discord.ButtonStyle.gray, label="Eigentum-Übertragen", emoji="👑")
                    delete_button = discord.ui.Button(style=discord.ButtonStyle.grey, label=f"{voice_channel.name} Löschen.", emoji="🧨")
                    # radio_button = discord.ui.Button(style=discord.ButtonStyle.grey, label=f"Beginne das Radio", emoji="🎶")
                    # stopradio_button = discord.ui.Button(style=discord.ButtonStyle.grey, label=f"Stoppe das Radio", emoji="💤")


                    async def call1(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                def check(message):
                                    return message.author == interaction.user and message.channel == interaction.channel

                            await interaction.response.send_message("Bitte gib die gewünschte Benutzerlimitierung für deinen Kanal ein:", ephemeral=True)
                            try:
                                response = await interaction.client.wait_for('message', check=check, timeout=30)
                                limit = int(response.content)
                                if 0 < limit <= 99:
                                    voice_channel = interaction.message.channel
                                    await voice_channel.edit(user_limit=limit)
                                    await interaction.followup.send(f"Benutzerlimit des Kanals auf {limit} gesetzt.", ephemeral=True)
                                    await asyncio.sleep(1)
                                    await response.delete()
                                else:
                                    await interaction.followup.send("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 99 ein.", ephemeral=True)
                            except asyncio.TimeoutError:
                                await interaction.followup.send("Zeitlimit überschritten. Bitte versuche es erneut.", ephemeral=True)
                            except ValueError:
                                await interaction.followup.send("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 99 ein.", ephemeral=True)


                    async def call2(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                def check(message):
                                    return message.author == interaction.user and message.channel == interaction.channel

                                await interaction.response.send_message("Bitte gib den neuen Namen für deinen Kanal ein:", ephemeral=True)
                                try:
                                    response = await interaction.client.wait_for('message', check=check, timeout=30)
                                    new_name = response.content
                                    voice_channel = interaction.message.channel
                                    await voice_channel.edit(name=new_name)
                                    await interaction.followup.send(f"Kanal erfolgreich in `{new_name}` umbenannt.", ephemeral=True)
                                    await asyncio.sleep(1)
                                    await response.delete()
                                except asyncio.TimeoutError:
                                    await interaction.followup.send("Zeitlimit überschritten. Bitte versuche es erneut.", ephemeral=True)
                    

                    async def call3(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                voice_channel = interaction.message.channel
                                await voice_channel.set_permissions(interaction.guild.default_role, view_channel=True, connect=False)
                                await interaction.response.send_message("Der Kanal wurde gesperrt.", ephemeral=True)
                    

                    async def call4(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                voice_channel = interaction.message.channel
                                await voice_channel.set_permissions(interaction.guild.default_role, connect=True)
                                await interaction.response.send_message("Der Kanal wurde entsperrt.", ephemeral=True)
                    

                    async def call5(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                await interaction.response.send_message("Bitte gib die ID des Benutzers an, den du bannen möchtest:", ephemeral=True)
                                try:
                                    response = await self.bot.wait_for('message', timeout=30)
                                    user_id = int(response.content)
                                    voice_channel = interaction.message.channel
                                    member = voice_channel.guild.get_member(user_id)
                                    if member:
                                        await member.move_to(None)
                                        await voice_channel.set_permissions(member, connect=False)
                                        await interaction.followup.send(f"{member.mention} wurde aus dem Kanal gebannt und gesperrt.", ephemeral=True)
                                        await asyncio.sleep(1)
                                        await response.delete()
                                    else:
                                        await interaction.followup.send("Benutzer nicht gefunden.", ephemeral=True)
                                except asyncio.TimeoutError:
                                    await interaction.followup.send("Zeitlimit überschritten. Bitte versuche es erneut.", ephemeral=True)



                    async def call6(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            else:
                                await interaction.response.send_message("Bitte gib die ID des Benutzers an, den du aus dem Kanal kicken möchtest:", ephemeral=True)
                                try:
                                    response = await self.bot.wait_for('message', timeout=30)
                                    user_id = int(response.content)
                                    voice_channel = interaction.message.channel
                                    member = voice_channel.guild.get_member(user_id)
                                    if member:
                                        await member.move_to(None)
                                        await interaction.followup.send(f"{member.mention} wurde aus dem Kanal gekickt.", ephemeral=True)
                                        await asyncio.sleep(3)
                                        await response.delete()
                                    else:
                                        await interaction.followup.send("Benutzer nicht gefunden.", ephemeral=True)
                                except asyncio.TimeoutError:
                                    await interaction.followup.send("Zeitlimit überschritten. Bitte versuche es erneut.", ephemeral=True)


                    async def call7(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()

                            if not channel_info:
                                await interaction.response.send_message("Der Voice Channel existiert nicht in der Datenbank.", ephemeral=True)
                                return

                            current_owner = interaction.guild.get_member(channel_info[0])
                            if current_owner is None:
                                await interaction.response.send_message("Der aktuelle Besitzer ist nicht mehr auf dem Server.", ephemeral=True)
                                return

                            if interaction.user.id == current_owner.id:
                                if current_owner.voice is None or current_owner.voice.channel != interaction.channel:
                                    await interaction.response.send_message("Du musst im gleichen Voice Channel wie der aktuelle Besitzer sein, um das Eigentum zu übertragen.", ephemeral=True)
                                    return

                                await interaction.response.send_message("Bitte gib die ID des Benutzers an, dem du das Eigentum übertragen möchtest:", ephemeral=True)
                                try:
                                    response = await self.bot.wait_for('message', timeout=30)
                                    new_owner_id = int(response.content)
                                    new_owner = interaction.guild.get_member(new_owner_id)
                                    if new_owner:
                                        await db.execute("UPDATE voice_channels SET user_id = ? WHERE channel_id = ?", (new_owner.id, channel_id))
                                        await db.commit()
                                        await interaction.followup.send(f"{new_owner.mention} ist jetzt der neue Besitzer des Kanals.", ephemeral=True)
                                        await asyncio.sleep(1)
                                        await response.delete()
                                    else:
                                        await interaction.followup.send("Benutzer nicht gefunden.", ephemeral=True)
                                except asyncio.TimeoutError:
                                    await interaction.followup.send("Zeitlimit überschritten. Bitte versuche es erneut.", ephemeral=True)
                                except ValueError:
                                    await interaction.followup.send("Ungültige Benutzer-ID. Bitte gib eine korrekte Benutzer-ID an.", ephemeral=True)
                            else:
                                if current_owner.voice is not None:
                                    await interaction.response.send_message("Der aktuelle Besitzer ist online im Voice Channel. Nur er kann das Eigentum übertragen.", ephemeral=True)
                                    return

                                await db.execute("UPDATE voice_channels SET user_id = ? WHERE channel_id = ?", (interaction.user.id, channel_id))
                                await db.commit()
                                await interaction.response.send_message(f"{interaction.user.mention} ist jetzt der neue Besitzer des Kanals.", ephemeral=True)




                    async def call8(interaction):
                        channel_id = interaction.message.channel.id
                        async with aiosqlite.connect("voice_channels.db") as db:
                            cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                            channel_info = await cursor.fetchone()
                            

                            if not channel_info or interaction.user.id != channel_info[0]:
                                await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                                return
                            
                            voice_channel = interaction.message.channel
                            await db.execute("DELETE FROM voice_channels WHERE channel_id = ?", (voice_channel.id,))
                            await db.commit()
                            await voice_channel.delete()
                            await asyncio.sleep(2)
                            await member.send("Dein Voice-Kanal wurde per Button gelöscht!")


                    # async def call9(interaction):
                    #     channel_id = interaction.message.channel.id
                    #     async with aiosqlite.connect("voice_channels.db") as db:
                    #         cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                    #         channel_info = await cursor.fetchone()

                    #         if not channel_info or interaction.user.id != channel_info[0]:
                    #             await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                    #             return

                    #         user_voice_state = interaction.guild.get_member(interaction.user.id).voice
                    #         if user_voice_state is None or user_voice_state.channel is None:
                    #             await interaction.response.send_message("Du musst einem Voice Channel beitreten!", ephemeral=True)
                    #             return

                    #         voice_channel = user_voice_state.channel

                    #         if not voice_channel.permissions_for(interaction.guild.me).connect:
                    #             await interaction.response.send_message("Ich habe keine Berechtigung deinem Channel beizutreten!", ephemeral=True)
                    #             return

                    #         if self.bot.voice_clients:
                    #             # Disconnect from any existing voice channel
                    #             for voice_client in self.bot.voice_clients:
                    #                 await voice_client.disconnect()

                    #         # Join the user's voice channel
                    #         voice_client = await voice_channel.connect()

                    #         # Play the radio stream
                    #         voice_client.play(discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio1.mp3"))

                    #         await interaction.response.send_message("Das Radio wurde gestartet")

                    # async def call10(interaction):
                    #     channel_id = interaction.message.channel.id
                    #     async with aiosqlite.connect("voice_channels.db") as db:
                    #         cursor = await db.execute("SELECT * FROM voice_channels WHERE channel_id = ?", (channel_id,))
                    #         channel_info = await cursor.fetchone()

                    #         if not channel_info or interaction.user.id != channel_info[0]:
                    #             await interaction.response.send_message("Du bist nicht der Besitzer des Channels.", ephemeral=True)
                    #             return

                    #         for voice_client in self.bot.voice_clients:
                    #             await voice_client.disconnect()

                    #         await interaction.response.send_message("Tschauu!!")


                    rename_button.callback = call2
                    limit_button.callback = call1
                    sperren_button.callback = call3
                    entsperren_button.callback = call4
                    ban_button.callback = call5
                    kick_button.callback = call6
                    rechtevergeben_button.callback = call7
                    delete_button.callback = call8
                    # radio_button.callback = call9
                    # stopradio_button.callback = call10
                    view.add_item(rename_button)
                    view.add_item(limit_button)
                    view.add_item(sperren_button)
                    view.add_item(entsperren_button)
                    view.add_item(ban_button)
                    view.add_item(kick_button)
                    view.add_item(rechtevergeben_button)
                    view.add_item(delete_button)
                    # view.add_item(radio_button)
                    # view.add_item(stopradio_button)
                    embed = discord.Embed(title="Neuer Voice Channel",
                                          description=f"Willkommen in deinem eigenen Voice Channel, {member.mention}!",
                                          color=discord.Color.purple())
                    embed.set_thumbnail(url=member.guild.icon)
                    embed.set_footer(text="Made by Bobbyontop. ©")
                    await voice_channel.send(content=f"{member.mention}", embed=embed, view=view)


        if before.channel and before.channel.id in self.temp_channels.values():
            if len(before.channel.members) == 0:
                await before.channel.delete()
                async with aiosqlite.connect("voice_channels.db") as db:
                    await db.execute("DELETE FROM voice_channels WHERE channel_id = ?", (before.channel.id,))
                    await db.commit()


def setup(bot):
    bot.add_cog(JoinToCreate(bot))

##From Bobby