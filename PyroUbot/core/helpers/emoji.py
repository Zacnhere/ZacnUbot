from PyroUbot import *



class EMO:
    async def PING(client):
        emot_1 = await get_vars(client.me.id, "EMOJI_PING")
        emot_ping = emot_1 if emot_1 else "5852684155380304970"
        if client.me.is_premium:
            _pong = f"<emoji id={emot_ping}>🏓</emoji>"
        else:
            _pong = ""
        return _pong


    async def MENTION(client):
        emot_2 = await get_vars(client.me.id, "EMOJI_MENTION")
        emot_tion = emot_2 if emot_2 else "5852800639188341430"
        if client.me.is_premium:
            _men = f"<emoji id={emot_tion}>👑</emoji>"
        else:
            _men = ""
        return _men


    async def UBOT(client):
        emot_3 = await get_vars(client.me.id, "EMOJI_USERBOT")
        emot_xbot = emot_3 if emot_3 else "6147942523957415123"
        if client.me.is_premium:
            _ubt = f"<emoji id={emot_xbot}>🤖</emoji>"
        else:
            _ubt = ""
        return _ubt

    
    async def PROSES(client):
        emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
        emot_prs = emot_4 if emot_4 else "5974332403890523746"
        if client.me.is_premium:
            _prses = f"<emoji id={emot_prs}>⌛️</emoji>"
        else:
            _prses = ""
        return _prses

    
    async def BERHASIL(client):
        emot_5 = await get_vars(client.me.id, "EMOJI_BERHASIL")
        emot_brhsl = emot_5 if emot_5 else "5368601123047354971"
        if client.me.is_premium:
            _berhasil = f"<emoji id={emot_brhsl}>✅</emoji>"
        else:
            _berhasil = ""
        return _berhasil


    async def GAGAL(client):
        emot_6 = await get_vars(client.me.id, "EMOJI_GAGAL")
        emot_ggl = emot_6 if emot_6 else "5371003921026266964"
        if client.me.is_premium:
            _gagal = f"<emoji id={emot_ggl}>❌</emoji>"
        else:
            _gagal = ""
        return _gagal


    async def BROADCAST(client):
        emot_7 = await get_vars(client.me.id, "EMOJI_BROADCAST")
        emot_gcs = emot_7 if emot_7 else "5803284068606940190"
        if client.me.is_premium:
            _bc = f"<emoji id={emot_gcs}>📊</emoji>"
        else:
            _bc = ""
        return _bc


    async def BL_GROUP(client):
        emot_8 = await get_vars(client.me.id, "EMOJI_GROUP")
        emot_gc = emot_8 if emot_8 else "6026239398650056451"
        if client.me.is_premium:
            _grp = f"<emoji id={emot_gc}>🗂</emoji>"
        else:
            _grp = ""
        return _grp


    async def BL_KETERANGAN(client):
        emot_9 = await get_vars(client.me.id, "EMOJI_KETERANGAN")
        emot_ktrng = emot_9 if emot_9 else "5800739459397849952"
        if client.me.is_premium:
            _ktrn = f"<emoji id={emot_ktrng}>📝</emoji>"
        else:
            _ktrn = ""
        return _ktrn
     

    async def MENUNGGU(client):
        emot_10 = await get_vars(client.me.id, "EMOJI_MENUNGGU")
        emot_mng = emot_10 if emot_10 else "5368295871131695793"
        if client.me.is_premium:
            _ktr = f"<emoji id={emot_mng}>⏰</emoji>"
        else:
            _ktr = ""
        return _ktr


    async def PUTARAN(client):
        emot_11 = await get_vars(client.me.id, "EMOJI_PUTARAN")
        emot_ptr = emot_11 if emot_11 else "5361600266225326825"
        if client.me.is_premium:
            mmk = f"<emoji id={emot_ptr}>✈️</emoji>"
        else:
            mmk = ""
        return mmk

