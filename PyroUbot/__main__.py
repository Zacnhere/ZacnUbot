import asyncio

from pyrogram import idle
from PyroUbot import *


async def main():
    await bot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=10)
            await ubot_.join_chat("ZacnnSupport")
            await ubot_.join_chat("TraderSignaltrading")
        except asyncio.TimeoutError:
            print(f"Timeout: Ubot {int(_ubot['name'])} terjadi timeout!")
        except Exception:
            await remove_ubot(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            print(f"Exception: Ubot {int(_ubot['name'])} terjadi kesalahan dan berhasil di hapus!")
    await asyncio.gather(
        loadPlugins(),
        installPeer(),
        expiredUserbots(),
        idle()
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
