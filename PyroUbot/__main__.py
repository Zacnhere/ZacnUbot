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
            await ubot_.join_chat("storekueren")
        except asyncio.TimeoutError:
            await remove_ubot(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            print(f"[𝗜𝗡𝗙𝗢]: {int(_ubot['name'])} 𝗧𝗜𝗗𝗔𝗞 𝗗𝗔𝗣𝗔𝗧 𝗠𝗘𝗥𝗘𝗦𝗣𝗢𝗡")
        except Exception:
            await remove_ubot(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            print(f"[𝗜𝗡𝗙𝗢]: {int(_ubot['name'])} 𝗕𝗘𝗥𝗛𝗔𝗦𝗜𝗟 𝗗𝗜𝗛𝗔𝗣𝗨𝗦")
    await bash("rm -rf *session*")
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
