import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(" ✅  - Der Clear Command wurde geladen.")
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.respond(f"› Du hast keine Berechtigungen um diesen Befehl auszuführen.", ephemeral=True)
            return

        await ctx.respond(f"Es ist ein Fehler aufgetreten: {error}", ephemeral=True)
        raise error
        
        
        
    @slash_command(description='› Lösche eine bestimmte Anzahl an Nachrichten.')
    @commands.has_permissions(manage_messages=True)
    @discord.guild_only()
    async def clear(self, ctx,
                    amount: Option(int, "› Die Anzahl der Nachrichten, die du löschen möchtest:", required=True)):
        await ctx.channel.purge(limit=amount)
        await ctx.respond(f"› Es wurden erfolgreich **{amount}** Nachrichten gelöscht.", delete_after=3)

def setup(bot):
    bot.add_cog(Clear(bot))