import os
import json
import discord

from discord.ext.commands import Bot
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

from PyBot.cog import load_cogs
from cogs.libary import *


def get_prefix(bot, message):
    with open("./json/utils.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


bot = Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Command gesucht? !help"))
    print("PyBot ist jetzt Online!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Ups! an dem Comand ist irgendwas falsch! Für Hilfe bentut !help")
    elif isinstance(error, CommandNotFound):
        await ctx.send(
            "Es wirkt so als ob das Command nicht verhanden ist.... \n du kannst mit !help dir alle Commands anzeigen lassen!"
            )


load_cogs(bot, BasicCmdCog(), CodeRunner())

bot.run(os.environ['DISCORD_TOKEN'])