   @tasks.loop(seconds=10)
    async def cdeletecommandclear(self):
        channel = self.bot.get_channel('CHANNEL_ID')
        messages = await channel.history(limit=200).flatten()
        for message in messages:
            if message.pinned:
                pass


            else:
                await message.delete()