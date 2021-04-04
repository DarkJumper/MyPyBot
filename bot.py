import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
from itertools import cycle

from discord.ext.commands.errors import MissingRequiredArgument

bot = Bot(command_prefix="!", case_insensitive=True, help_command=None)


@bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Bitte gebe ein Richtigen Command an!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])