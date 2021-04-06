import discord
import json
from discord.ext import commands
from discord.voice_client import VoiceClient


class Cog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        """
         Events Begin!
        """

    @commands.Cog.listener()
    async def on_member_join(self, member: str):
        channel = self.bot.get_channel(774271460608966707)
        await channel.send(f'Willkommen {member}!\n')
        """
        Commands Begin!
        """

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=int(amount))


def setup(bot):
    bot.add_cog(Cog(bot))
