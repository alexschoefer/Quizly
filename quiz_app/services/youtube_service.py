import re
from urllib.parse import urlparse, parse_qs
import os
import yt_dlp
import uuid

def extract_youtube_video_id(url: str) -> str:
    """
    Extracts the YouTube video ID from a given URL.
    """
    if not url:
        raise ValueError("URL is missing")

    parsed = urlparse(url)
    hostname = parsed.hostname

    if hostname not in ["youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"]:
        raise ValueError("Invalid YouTube domain")

    # youtu.be/<id>
    if hostname == "youtu.be":
        video_id = parsed.path.lstrip("/")
        if len(video_id) == 11:
            return video_id

    # youtube.com/watch?v=<id>
    if parsed.path == "/watch":
        query = parse_qs(parsed.query)
        video_id = query.get("v", [None])[0]
        if video_id and len(video_id) == 11:
            return video_id

    # youtube.com/shorts/<id>
    if parsed.path.startswith("/shorts/"):
        video_id = parsed.path.split("/")[2]
        if len(video_id) == 11:
            return video_id

    raise ValueError("Invalid YouTube URL")

def build_canonical_youtube_url(video_id: str) -> str:
    """
    Constructs a canonical YouTube URL from a given video ID.
    """
    return f"https://www.youtube.com/watch?v={video_id}"

def normalize_youtube_url(url: str) -> str:
    """
    Normalizes a YouTube URL to a canonical format.
    """
    video_id = extract_youtube_video_id(url)
    return build_canonical_youtube_url(video_id)

def download_audio(url: str, output_dir: str = "tmp") -> str:
    """
    Downloads the audio from a YouTube video and saves it to the specified output directory.
    Returns the path to the downloaded audio file.
    """
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(id)s_{uuid.uuid4()}.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        "quiet": True,
        "noplaylist": True,
    }

    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info_dict)
            audio_file = os.path.splitext(audio_file)[0] + ".mp3"
        return audio_file
    except Exception as e:
        raise RuntimeError(f"Failed to download audio: {str(e)}")
