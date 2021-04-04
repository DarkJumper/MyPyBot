import discord
from discord import activity
from discord.ext import commands


class Cog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        """
         Events Begin!
        """

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("Hilfe wird Benötigt? !help"))
        print("PyBot ist Online!")
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
