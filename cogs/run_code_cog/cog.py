import re

from aiohttp import ClientError
from discord import Embed
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import CommandError, UserInputError

from .api import Emkc, EmkcApiExcept

max_chars = 500

languages = ["c", "cpp", "bash", "kotlin", "python3"]


class CodeRunner(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def run(self, ctx, *, args: str):
        if not (match := re.fullmatch(r"((```)?)([a-zA-Z\d]+)\n(.+?)\1"), args, re.DOTALL):
            raise UserInputError
        *_, language, source = match.groups()
        await ctx.trigger_typing()
        try:
            result_api = await Emkc.run_code(language, source)
        except EmkcApiExcept as e_except:
            if e_except.error == "Supplied language is not supported by Piston":
                raise CommandError("Sprache wird nicht Unterstützt")
            raise CommandError(f"Es wurde ein Fehler während des Ausführens festgestellt {e_except.error}")
        except ClientError:
            raise CommandError(f"Es wurde ein Fehler während des Ausführens festgestellt!")
        output: str = result_api["output"]
        if len(output) > max_chars:
            newline = output.find("\n", max_chars, max_chars + 10)
            if newline == -1:
                newline == max_chars
            output = output[:newline] + "\n...."
        description = "```\n" + output.replace("`", "`\u200b") + "\n```"
        print(description)
        embed = Embed(title="Ausgabe!", description=description)
        embed.set_footer(text=f'Wurde Ausgeführt von {ctx.author} {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CodeRunner(bot))