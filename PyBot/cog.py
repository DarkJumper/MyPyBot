import discord
import sys

from discord.ext.commands import Cog as DiscordCog, Bot


class Cog(DiscordCog):
    bot: Bot

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


def load_cog(bot: Bot, *cogs: Cog):
    for cog in cogs:
        cog.bot = bot
        bot.add_cog(cog)
