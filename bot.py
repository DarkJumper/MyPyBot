import os
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
from itertools import cycle

bot = Bot(command_prefix="!", case_insensitive=True, help_command=None)
status = cycle(["Command gesucht? !help", "Kann ich dir helfen? !help", "Das bin ich!Github"])


@tasks.loop(seconds=10)
async def change_status(self):
    await self.bot.change_presence(status=discord.Game(next(status)))


@bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])