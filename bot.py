import discord
import os

from discord.ext import commands
from PyBot.util import get_prefix

bot = commands.Bot(command_prefix=get_prefix, help_command=None)


@bot.event
async def on_ready():
    print("PyBot ist Bereit!")


@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping! {bot.latency}')


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
    await context.send("help ist noch nicht erstellt worden....sorry!")


bot.run(os.environ['DISCORD_TOKEN'])
