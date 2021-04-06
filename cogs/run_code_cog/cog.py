from os import stat
import re

from aiohttp import ClientError
from discord import Embed
from discord.ext import commands
from discord.ext.commands import CommandError, UserInputError

from .api import Emkc, EmkcApiExcept

max_chars = 2000
languages = [
    "awk",
    "bash",
    "brainfuck",
    "c",
    "cpp",
    "clojure",
    "crystal",
    "csharp",
    "d",
    "dash",
    "deno",
    "elixir",
    "emacs",
    "elisp",
    "go",
    "haskell",
    "java",
    "jelly",
    "julia",
    "kotlin",
    "lisp",
    "lolcode",
    "lua",
    "nasm",
    "nasm64",
    "nim",
    "node",
    "osabie",
    "paradoc",
    "perl",
    "php",
    "python2",
    "python3",
    "ruby",
    "rust",
    "scala",
    "swift",
    "typescript",
    "zig",
    ]


def supporteted_language():
    string = str()
    string += ', '.join(f'{language}' for language in languages)
    return string


class CodeRunner(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def run(self, ctx, *, args: str) -> str:
        if args == "help":
            embed = Embed(
                title="Hilfe für Code Runner!", description="```python\n!run ```language\nyour code\n```" + "\n```"
                )
            embed.set_footer(text="Folgende Sprachen stehen zur verfügung:\n" + supporteted_language())
            await ctx.send(embed=embed)
            return
        if not (match := re.fullmatch(r"((```)?)([a-zA-Z\d]+)\n(.+?)\1", args, re.DOTALL)):
            await ctx.send(args)
            raise UserInputError
        *_, language, source = match.groups()
        try:
            result_api = await Emkc.code_runner(language, source)
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
        embed = Embed(title="Ausgabe!", description=description)
        embed.set_footer(text=f'Wurde Ausgeführt von {ctx.author} {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CodeRunner(bot))