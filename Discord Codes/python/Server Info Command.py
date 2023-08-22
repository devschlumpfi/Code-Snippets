import discord
from discord.ext import commands
from discord import app_commands


class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Zeigt Infos über den Server.")
    async def serverinfo(self, ctx: discord.Interaction):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        guild = ctx.guild
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        embed = discord.Embed(
            title=f"{name} Server Information",
            description=f'**Beschreibung vom Servers**\n {description}',
            color=discord.Color.blue()
        )
        embed.add_field(name='Owner', value=f'{ctx.guild.owner.mention}\n**ID:**({ctx.guild.owner_id})')
        embed.add_field(name="🆔 Server ID", value=id, inline=True)
        embed.add_field(name="👥 Mitglieder", value=memberCount, inline=True)
        embed.add_field(name='🤖 Bots', value=f'{sum(member.bot for member in ctx.guild.members)}')
        embed.add_field(name='👥 User', value=f'{sum(not member.bot for member in ctx.guild.members)}')
        embed.add_field(name="💬 Channel", value=f"{channels}", inline=True)
        embed.add_field(name='📆 Servererstellung', value=f'<t:{int(ctx.guild.created_at.timestamp())}:R>', inline=False)
        embed.add_field(name='🗂 Kategorien', value=f"{categories}", inline=True)
        embed.add_field(name='Rollen', value=str(role_count), inline=False)
        embed.add_field(name='✅ Verifizierungslevel', value=str(ctx.guild.verification_level), inline=False)
        embed.add_field(name='✨ Boosts', value=f'{str(ctx.guild.premium_subscription_count)}')
        embed.add_field(name='🥇 Boostlevel', value=f'{ctx.guild.premium_tier}')
        embed.add_field(name="```Status```", value=f"**🟢Online:** {statuses[0]}\n**🟠Abwesend:** {statuses[1]}"
                                                   f"\n**🔴Bitte nicht stören:** {statuses[2]}\n**⚪Offline:** "
                                                   f"{statuses[3]}", inline=True)
        embed.add_field(name='Emojis', value=str(emoji_count), inline=True)
        embed.add_field(name='Regelnkanal',
                        value=ctx.guild.rules_channel.mention if ctx.guild.rules_channel else '~~nicht gegeben~~')
        embed.add_field(name="Community Update Kanal",
                        value=ctx.guild.public_updates_channel if ctx.guild.public_updates_channel else "~~nicht gegeben~~")
        embed.add_field(name='AFK CHANNEL',
                        value=str(ctx.guild.afk_channel.mention if ctx.guild.afk_channel else '~~nicht gegeben~~'),
                        inline=True)
        embed.add_field(name='AFK Timeout in sek.', value=str(ctx.guild.afk_timeout), inline=True)
        embed.add_field(name="Threads", value=f"{len(guild.threads) if guild.threads else 0}")
        await ctx.response.send_message(embed=embed, view=serverinfob(ctx))


async def setup(bot):
    await bot.add_cog(serverinfo(bot))


class serverinfob(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__(timeout=None)

    @discord.ui.button(label="🏠 Home", style=discord.ButtonStyle.red)
    async def serverinfo2(self, ctx, button:discord.ui.Button):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
        guild = ctx.guild
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        total_member_count = 0
        # Iterate over the voice channels
        for voice_channel in ctx.guild.voice_channels:
            # Sum the number of members connected in each voice channel
            total_member_count += len(voice_channel.members)
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        embed = discord.Embed(
            title=name + " Server Information",
            description=f'**Beschreibung vom Servers**\n {description if description else" "}',
            color=discord.Color.blue()
        )
        if guild.banner:
            embed.set_image(url=guild.banner.url)
        embed.add_field(name='Owner', value=f'{ctx.guild.owner.mention}\n**ID:**({ctx.guild.owner_id})')
        embed.add_field(name="🆔 Server ID", value=id, inline=True)
        embed.add_field(name='Shard ID', value=ctx.guild.shard_id if ctx.guild.shard_id else "~~nicht gegeben~~")
        embed.add_field(name="👥 Mitglieder", value=memberCount, inline=True)
        embed.add_field(name='🤖 Bots', value=f'{sum(member.bot for member in ctx.guild.members)}')
        embed.add_field(name='👥 User', value=f'{sum(not member.bot for member in ctx.guild.members)}')
        embed.add_field(name='😢Inaktive User', value=await ctx.guild.estimate_pruned_members(days=7))
        embed.add_field(name="💬 Channel", value=channels, inline=True)
        embed.add_field(name="Forums",value=len(guild.forums) if guild.forums else "0")
        embed.add_field(name="Stage Channel", value=guild.stage_channels if guild.stage_channels else "0")
        embed.add_field(name='📆 Servererstellung', value=f'<t:{int(ctx.guild.created_at.timestamp())}:R>', inline=False)
        embed.add_field(name='🗂 Kategorien', value=categories, inline=True)
        embed.add_field(name='Rollen', value=str(role_count), inline=False)
        embed.add_field(name='✅ Verifizierungslevel', value=str(ctx.guild.verification_level), inline=False)
        embed.add_field(name='✨ Boosts', value=f'{str(ctx.guild.premium_subscription_count)}')
        embed.add_field(name='🥇 Boostlevel', value=f'{ctx.guild.premium_tier}')
        embed.add_field(name="```Status```", value=f"**🟢Online:** {statuses[0]}\n**🟠Abwesend:** {statuses[1]}"
                                                f"\n**🔴Bitte nicht stören:** {statuses[2]}\n**⚪Offline:** "
                                                f"{statuses[3]}", inline=True)
        embed.add_field(name='Emojis', value=str(emoji_count), inline=True)
        embed.add_field(name='Regelnkanal',
                        value=ctx.guild.rules_channel.mention if ctx.guild.rules_channel else '~~nicht gegeben~~')
        embed.add_field(name="Community Update Kanal", value=ctx.guild.public_updates_channel if ctx.guild.public_updates_channel else "~~nicht gegeben~~")
        embed.add_field(name="System-Kanal",value=guild.system_channel.mention)
        embed.add_field(name='AFK CHANNEL',
                        value=str(ctx.guild.afk_channel.mention if ctx.guild.afk_channel else '~~nicht gegeben~~'),
                        inline=True)
        embed.add_field(name="User im Sprachkanal",value=f'**Aktive Sprachkanäle**\nMomentan sind {total_member_count} Mitglieder in Sprachkanälen.')    
        embed.add_field(name='AFK Timeout in sek.', value=str(ctx.guild.afk_timeout), inline=True)
        embed.add_field(name='Bitrate', value=(ctx.guild.bitrate_limit if ctx.guild.bitrate_limit else 'keines'),
                        inline=True)
        embed.add_field(name="Vanity URL", value=ctx.guild.vanity_url_code if ctx.guild.vanity_url_code else "~~nicht gegeben~~")
        embed.add_field(name="Threads",value=guild.threads if guild.threads else 0)
        if guild.features:
            embed.add_field(name="Server features",value="✅"+"\n✅".join(guild.features) or "Nothing")
        embed.set_footer(text=f'Angefragt von {ctx.user.name} • {ctx.user.id}')
        await ctx.response.edit_message(embed=embed)

    @discord.ui.button(label="Serverprofil", style=discord.ButtonStyle.green)
    async def icon(self, ctx, button:discord.ui.Button):
        embed = discord.Embed(title=f"Das ist das Servericon von {ctx.guild}")
        embed.set_image(url=ctx.guild.icon)
        await ctx.response.edit_message(embed=embed)

    @discord.ui.button(label="Server emojis", style=discord.ButtonStyle.blurple)
    async def serveremoji(self, ctx, button:discord.ui.Button):
        embed = discord.Embed()
        embed = discord.Embed(title=f"{ctx.guild}`s Serveremojis",
        description=(",".join([str(emojis) for emojis in ctx.guild.emojis])),
        color=discord.Color.blue())
        await ctx.response.edit_message(embed=embed)

    @discord.ui.button(label="Server rollen", style=discord.ButtonStyle.blurple)
    async def serverrollen(self, ctx, button:discord.ui.Button):
        embed = discord.Embed(title=f"{ctx.guild}`s Serverrollen",
                                      description=("".join([str(r.mention) for r in ctx.guild.roles])))
        color=discord.Color.blue()
        await ctx.response.edit_message(embed=embed)

    @discord.ui.button(label="Serverbanner", style=discord.ButtonStyle.green)
    async def serverbanner(self, ctx, button:discord.ui.Button):
        if ctx.guild.banner is None:
            embed = discord.Embed(title=f"{ctx.guild}`s Banner", description="Der Server besitzt kein Serverbanner")
            await ctx.response.edit_message(embed=embed)
        else:
            embed = discord.Embed(title=f"{ctx.guild}`s Banner")
            embed.set_image(url=ctx.guild.banner)
            await ctx.response.edit_message(embed=embed)


##From Lucky