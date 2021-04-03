import os

from discord.ext.commands import Bot

bot = Bot(command_prefix="!", case_insensitive=True, help_command=None)


@bot.command()
async def load(ctx, extension):
    bot.unload_extension(f'PyBot.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'PyBot.{extension}')


for filename in os.listdir('./PyBot'):
    if filename.endswith('.py'):
        bot.load_extension(f'PyBot.{filename[:-3]}')

bot.run(os.environ['DISCORD_TOKEN'])