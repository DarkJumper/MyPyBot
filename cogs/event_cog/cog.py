from discord.ext import commands


class EventCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: str):
        channel = self.bot.get_channel(774271460608966707)
        await channel.send(f'Willkommen {member}!\n')


def setup(bot):
    bot.add_cog(EventCog(bot))