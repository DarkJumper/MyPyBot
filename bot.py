import os
import json
import discord

from discord.ext.commands import Bot
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

from cogs.basic_cmd import basic_cmd


def get_prefix(bot, message):
    with open("./json/utils.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


initial_extensions = ['basic_cmd']

bot = Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)

if __name__ == '__main__':
    for extensions in initial_extensions:
        bot.load_extension(extensions)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Command gesucht? !help"))
    print("PyBot ist jetzt Online!")


""" @bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}') """


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Ups! an dem Comand ist irgendwas falsch! Für Hilfe bentut !help")
    elif isinstance(error, CommandNotFound):
        await ctx.send(
            "Es wirkt so als ob das Command nicht verhanden ist.... \n du kannst mit !help dir alle Commands anzeigen lassen!"
            )


bot.run(os.environ['DISCORD_TOKEN'])