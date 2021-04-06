import discord
import json
from discord.ext import commands


class BasicCmdCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send(f'Ping von PyBot!\nBeträgt {round(self.bot.latency,2)}ms')

    @commands.command()
    async def github(self, ctx):
        await ctx.send(f'Mein Code findest du hier\n-> https://github.com/DarkJumper/MyPyBot')

    @commands.command()
    async def help(self, ctx):
        with open("./json/help.json", "r") as f:
            json_help = json.load(f)
        cmd = str()
        for comand in json_help:
            cmd += f'{comand.ljust(8)} -{json_help[comand]}\n'
        await ctx.send(f'Folgende Commands stehen zur verfügung:\n```{cmd}```')


def setup(bot):
    bot.add_cog(BasicCmdCog(bot))