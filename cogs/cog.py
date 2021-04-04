import discord
from discord.ext import commands, tasks
from itertools import cycle


class Cog(commands.Cog):
    status = cycle(["Command gesucht? !help", "Kann ich dir helfen? !help", "Das bin ich!Github"])

    def __init__(self, bot) -> None:
        self.bot = bot

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(status=discord.Game(next(self.status)))
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping! {self.bot.latency}')

    @commands.command()
    async def Hallo(self, ctx):
        await ctx.send(
            f'Hallo ich bin PyBot. \nFalls du hilfe Brauchen solltest kannst du mich einfach fragen mit "PyBot help" .'
            )

    @commands.command()
    async def Github(self, ctx):
        await ctx.send(f'Mein Code findest du hier\n-> https://github.com/DarkJumper/MyPyBot')

    @commands.command()
    async def help(self, context):
        await context.send("help ist noch nicht erstellt worden....sorry!")


def setup(bot):
    bot.add_cog(Cog(bot))
