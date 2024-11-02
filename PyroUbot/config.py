import os
import sys


MAX_BOT = int(os.getenv("MAX_BOT", "50"))

API_ID = int(os.getenv("API_ID", "8986091"))

API_HASH = os.getenv("API_HASH", "c568be6936fb9df2a9ac17cce099e748")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7572061181:AAF3uduO89gt40EsNwQ4hSnVPf-mmC2pMHY")

OWNER_ID = int(os.getenv("OWNER_ID", "1361379181"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002166782827").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY", "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://zacnmusic:zacnmusic@cluster0.jhgvg.mongodb.net/?retryWrites=true&w=majority&appName=ZACNHERE"
)
