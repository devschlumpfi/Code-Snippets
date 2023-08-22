import json
import discord
from colorama import *
from discord.commands import slash_command, Option
from discord.ext import commands, tasks
from pytube import Channel


class YoutubeNotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.checkforvideos.start()

    # Prüft alle 60 Sekunden die Videos
    @tasks.loop(seconds=60)
    async def checkforvideos(self):
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        print(Fore.RED + "---------------Prüfe YouTube-Daten!---------------")

        # Prüft die Daten in "youtubedata.json" und holt sich die Kanal-URL sowie die html der /videos Seite
        for youtube_channel in data:
            print(Fore.BLUE + f"----------Prüfe YouTube-Daten von {data[youtube_channel]['channel_name']}----------")
            channel = f"https://www.youtube.com/channel/{youtube_channel}"

            c = Channel(channel)
            try:
                latest_video_url = c.video_urls[0]
            except:
                continue

            # Prüft ob die url in "youtubedata.json" nicht die selbe ist wie die letzte Video url und ersetzt diese ggf.
            if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
                data[str(youtube_channel)]['latest_video_url'] = latest_video_url

                # dumping der Daten
                with open("youtubedata.json", "w") as f:
                    json.dump(data, f)

                # Nimmt die Channel ID und sendet die Daten
                discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
                discord_channel = self.bot.get_channel(int(discord_channel_id))
                msg = f"{data[str(youtube_channel)]['channel_name']} hat gerade ein Video hochgeladen: " \
                      f"{latest_video_url} "
                await discord_channel.send(msg)

    # SlashCommand erstellen um mehr YouTube Accounts hinzuzufügen
    @slash_command(description="Füge einen YouTuber zu den Benachrichtigungen hinzu!")
    @discord.default_permissions(administrator=True)
    @discord.guild_only()
    async def add_yt_notify(self, ctx, channel_id: str, *, channel_name: str, discord_channel_id: str):
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        data[str(channel_id)] = {}
        data[str(channel_id)]["channel_name"] = channel_name
        data[str(channel_id)]["latest_video_url"] = "none"
        data[str(channel_id)]["notifying_discord_channel"] = discord_channel_id

        with open("youtubedata.json", "w") as f:
            json.dump(data, f)

        await ctx.respond("Daten hinzugefügt!", ephemeral=True)

    # SlashCommand um Benachrichtigungen umzustellen
    @slash_command(description="Aktiviere oder Deaktiviere Benachrichtigungen")
    @discord.default_permissions(administrator=True)
    @discord.guild_only()
    async def yt_notify(
            self, ctx,
            status: Option(str, choices=["aktivieren", "deaktivieren"])
    ):
        if status == "aktivieren":
            self.checkforvideos.start()
        else:
            self.checkforvideos.stop()

        await ctx.respond("Status wurde geändert!", ephemeral=True)


def setup(bot):
    bot.add_cog(YoutubeNotify(bot))