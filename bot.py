import os
import json
from sys import prefix
from discord.ext.commands import Bot

from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


def get_prefix(bot, message):
    with open("./json/utils.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


bot = Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)


@bot.event
async def on_guild_join(guild):
    with open("./json/utils.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '!'
    with open("./json/utils.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Ups! an dem Comand ist irgendwas falsch! Für Hilfe bentut !help")
    elif isinstance(error, CommandNotFound):
        await ctx.send(
            "Es wirkt so als ob das Command nicht verhanden ist.... \n du kannst mit !help dir alle Commands anzeigen lassen!"
            )


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])