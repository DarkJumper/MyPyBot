class HelpRunner:

    language_support = [
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

    async def languages(self) -> str:
        lang = ', '.join(f'`{language}`' for language in self.language_support)
        return await "Folgende Sprachen stehen zur verfügung:\n" + lang

    async def get_help(self) -> str:
        formating = """!run ```language\n
        your code\n
        ```
        """
        return await formating
