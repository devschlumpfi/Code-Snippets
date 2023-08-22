import discord
from discord.utils import basic_autocomplete
from discord.commands import slash_command, Option
from discord.ext import commands


async def unban_autocomplete(ctx: discord.AutocompleteContext):
    x = await ctx.interaction.guild.bans().flatten()
    x = [f'{y.user}' for y in x]
    return x

class UnbanCommand(commands.Cog):

    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(name="unban", description="")
    @discord.default_permissions(ban_members=True)
    async def _unban(self, ctx: discord.ApplicationContext, member: Option(str, autocomplete=basic_autocomplete(unban_autocomplete))):
        async for ban in ctx.guild.bans():
            if f'{ban.user}' == f'{member}':
                await ctx.guild.unban(ban.user)
                return await ctx.respond(f"Unbanned {ban.user}")

            else:
                continue

        return await ctx.respond("User cant be found")


def setup(bot: discord.Bot):
    bot.add_cog(UnbanCommand(bot))