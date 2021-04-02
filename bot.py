import os

from typing import Iterable
from discord import Message
from discord.ext.commands import Bot

#from PyBot.util import get_prefix
""" async def fetch_prefix(_, msg: Message) -> Iterable[str]:
    prefix = [await get_prefix()]
    if msg.guild is None:
        prefix.append("")
    return prefix """

bot = Bot(command_prefix="!", case_insensitive=True, help_command=None)


@bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'Pybot.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'PyBot.{extension}')


for filename in os.listdir('./PyBot'):
    if filename.endswith('.py'):
        bot.load_extension(f'PyBot.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])