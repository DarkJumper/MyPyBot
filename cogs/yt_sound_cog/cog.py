import discord

from typing import Union
from discord.ext import commands
from discord.voice_client import VoiceClient


class SoundCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.bot.join_voice_channel(channel)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(SoundCog(bot))