import discord

from typing import Union
from discord.ext import commands
from discord.voice_client import VoiceClient


class SoundCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def join(self, ctx: commands.Context, *, destination: Union[discord.VoiceChannel, discord.Member] = None):
        destination = destination or ctx.author
        if isinstance(destination, discord.Member):
            if destination.voice and destination.voice.channel:
                destination = destination.voice.channel
            else:
                return await ctx.send("Channel Joined")
        voice = ctx.guild.voice_client
        if voice:
            await voice.move_to(destination)
        else:
            await destination.connect(reconnect=True)
        await ctx.send(f'Verbunden mit {destination.name}')

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot):
    bot.add_cog(SoundCog(bot))