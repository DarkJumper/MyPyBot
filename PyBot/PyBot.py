import os

from discord.ext.commands import Bot


def run_bot():

    bot = Bot(command_prefix="!", case_insensitive=True, help_command=None)

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