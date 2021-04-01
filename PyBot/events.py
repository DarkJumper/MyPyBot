from discord.ext.commands import Bot


class Events:

    @staticmethod
    async def on_ready(_):
        print("PyBot ist Bereit in Class")