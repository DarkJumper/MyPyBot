import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="PyBot")


@client.event
async def on_ready():
    print("Bot ist Bereit!")


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! {client.latency}')

    
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)


    
client.add_command(test)
client.add_command(ping)
client.run(os.environ['DISCORD_TOKEN'])
