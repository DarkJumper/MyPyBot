class Settings:
    pass


class GlobalSettings(Settings):
    prefix = "!"


async def get_prefix() -> str:
    return GlobalSettings.prefix
