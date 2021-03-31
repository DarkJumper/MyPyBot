import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="PyBot ")


@client.event
async def on_ready():
    print("Bot ist Bereit!")


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! {client.latency}')


@client.command()
async def Hallo(ctx):
    await ctx.send(f'Hallo ich bin PyBot. \n Falls du hilfe Brauchen solltest kannst du mich einfach fragen mit "PyBot help" .')
    
    
    
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)


    
client.run(os.environ['DISCORD_TOKEN'])
