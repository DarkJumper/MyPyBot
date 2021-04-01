@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping! {bot.latency}')