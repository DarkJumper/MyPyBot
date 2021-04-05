import discord
import json
from discord.ext import commands


class Cog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        """
         Events Begin!
        """

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("Command gesucht? !help"))
        print("PyBot ist jetzt Online!")
        """
        Commands Begin!
        """

    @commands.command(pass_context=True)
    async def ping(self, ctx, cmd: str):
        if cmd == "-user":
            await ctx.send(f'Ping von {ctx.message.author.mention}!\nBeträgt ')
        else:
            await ctx.send(f'Ping von PyBot!\nBeträgt {self.bot.latency}ms')

    @commands.command()
    async def Hallo(self, ctx):
        await ctx.send(
            f'Hallo ich bin PyBot. \nFalls du hilfe Brauchen solltest kannst du mich einfach fragen mit "PyBot help" .'
            )

    @commands.command()
    async def github(self, ctx):
        await ctx.send(f'Mein Code findest du hier\n-> https://github.com/DarkJumper/MyPyBot')

    @commands.command()
    async def help(self, ctx):
        with open("./json/help.json", "r") as f:
            json_help = json.load(f)
        cmd = ""
        for comand in json_help:
            cmd += f'{comand.rjust(15)}: {json_help[comand]}\n'
        await ctx.send(f'Folgende Commands stehen zur verfügung!\n```{cmd}```')

    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Cog(bot))
