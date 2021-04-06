from aiohttp import ClientSession


class EmkcApiExcept(BaseException):

    @property
    def error(self) -> str:
        return self.args[0]["message"]


class Emkc:
    url = "https://emkc.org/api/v1/piston/execute"

    @staticmethod
    async def code_runner(language: str, src: str) -> dict:
        async with ClientSession() as session, session.post(
            Emkc.url, json={
                "language": language,
                "source": src
                }
            ) as response:
            if response.status != 200:
                raise EmkcApiExcept(await response.json())
            return await response.json()