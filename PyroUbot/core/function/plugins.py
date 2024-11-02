import importlib

from PyroUbot import bot
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule
from PyroUbot.core.database import *



HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"PyroUbot.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🔥 TELAH BERHASIL DIAKTIFKAN! 🔥]")
    
    
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
