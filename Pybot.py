import discord
from discord.ext import commands
import os

pybot = commands.Bot(command_prefix="PyBot ", help_command=None)


@pybot.event
async def on_ready():
    print("PyBot ist Bereit!")


@pybot.command()
async def ping(ctx):
    await ctx.send(f'Ping! {pybot.latency}')


@pybot.command()
async def Hallo(ctx):
    await ctx.send(
        f'Hallo ich bin PyBot. \nFalls du hilfe Brauchen solltest kannst du mich einfach fragen mit "PyBot help" .'
        )


@pybot.command()
async def erschaffer(ctx):
    await ctx.send(f'Meinen Erschaffe kenne ich nicht Persönlich.... \n')


@pybot.command()
async def code(ctx):
    await ctx.send(f'Mein Code findest du hier auf [Github](https://github.com/DarkJumper/MyPyBot)!')


@pybot.command()
async def help(context):
    await context.send("help ist noch nicht erstellt worden....sorry!")


pybot.run(os.environ['DISCORD_TOKEN'])
