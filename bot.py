import os

from typing import Iterable
from discord import Message, Intents
from discord.ext.commands import Bot

from PyBot.util import get_prefix


async def fetch_prefix(_, msg: Message) -> Iterable[str]:
    prefix = [await get_prefix()]
    if msg.guild is None:
        prefix.append("")
    return prefix


bot = Bot(command_prefix=fetch_prefix, case_insensitive=True, help_command=None, intents=(Intents.all()))


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
