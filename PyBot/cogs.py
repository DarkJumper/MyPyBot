from discord.ext import commands


class Cog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @staticmethod
    def setup(bot):
        bot.add_cog(Cog(bot))

    # Event
    @commands.Cog.listener()
    async def on_read(self):
        print("Bot ist Online!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping! {self.bot.latency}')


""" @bot.event
async def on_ready():
    print("PyBot ist Bereit!1")


@bot.command()
async def Hallo(ctx):
    await ctx.send(
        f'Hallo ich bin PyBot. \nFalls du hilfe Brauchen solltest kannst du mich einfach fragen mit "PyBot help" .'
        )


@bot.command()
async def erschaffer(ctx):
    await ctx.send(f'Meinen Erschaffe kenne ich nicht Persönlich.... \n')


@bot.command()
async def code(ctx):
    await ctx.send(f'Mein Code findest du hier\n-> https://github.com/DarkJumper/MyPyBot')


@bot.command()
async def help(context):
    await context.send("help ist noch nicht erstellt worden....sorry!") """