import asyncio
from functools import partial
from yt_dlp import YoutubeDL

async def run_sync(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, partial(func, *args, **kwargs))

async def YoutubeDownload(url, as_video=False):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": "cookies.txt",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])" if as_video else "bestaudio[ext=m4a]",
    }

    data_ytp = (
        "<b>💡 ɪɴꜰᴏʀᴍᴀsɪ {}</b>\n\n"
        "<b>🏷 ɴᴀᴍᴀ:</b> {}\n"
        "<b>🧭 ᴅᴜʀᴀsɪ:</b> {}\n"
        "<b>👀 ᴅɪʟɪʜᴀᴛ:</b> {}\n"
        "<b>📢 ᴄʜᴀɴɴᴇʟ:</b> {}\n"
        "<b>🔗 ᴛᴀᴜᴛᴀɴ:</b> <a href={}>ʏᴏᴜᴛᴜʙᴇ</a>\n\n"
        "<b>⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> {}"
    )

    try:
        ydl = YoutubeDL(ydl_opts)
        ytdl_data = await run_sync(ydl.extract_info, url, download=True)
        
        file_name = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"

        return file_name, title, url, duration, views, channel, thumb, data_ytp

    except Exception as e:
        return f"❌ Terjadi kesalahan saat mengunduh video: {str(e)}"
        
