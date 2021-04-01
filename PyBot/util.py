class GlobalSettings:
    prefix = "!"


async def get_prefix() -> str:
    return GlobalSettings.prefix
