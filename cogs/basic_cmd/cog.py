import discord
import json
from discord.ext import commands


class CmdCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send(f'Ping von PyBot!\nBeträgt {round(self.bot.latency,2)}ms')

    @commands.command()
    async def github(self, ctx):
        await ctx.send(f'Mein Code findest du hier\n-> https://github.com/DarkJumper/MyPyBot')

    @commands.command()
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=int(amount))

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def help(self, ctx):
        with open("./json/help.json", "r") as f:
            json_help = json.load(f)
        cmd = str()
        for comand in json_help:
            cmd += f'{comand.ljust(8)} -{json_help[comand]}\n'
        await ctx.send(f'Folgende Commands stehen zur verfügung:\n```{cmd}```')


def setup(bot):
    bot.add_cog(CmdCog(bot))