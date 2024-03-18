import click
import yt_dlp


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "-N",
    "--concurrent-fragments",
    default=1,
    type=int,
    help="Number of fragments of a dash/hlsnative video that should be downloaded concurrently",
)
def video(urls, concurrent_fragments):
    """
    Download youtube videos audio
    """
    opts = {
        "writethumbnail": True,
        "outtmpl": "[%(upload_date>%Y-%m-%d)s] %(title)s.%(ext)s",
        "ignoreerrors": True,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "continuedl": True,
        "windowsfilenames": True,
        "concurrent_fragment_downloads": concurrent_fragments,
        "postprocessors": [
            {"key": "FFmpegMetadata", "add_metadata": "True"},
            {"key": "EmbedThumbnail"},
        ],
    }

    yt = yt_dlp.YoutubeDL(opts)

    yt.download(urls)


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "-N",
    "--concurrent-fragments",
    default=1,
    type=int,
    help="Number of fragments of a dash/hlsnative video that should be downloaded concurrently",
)
def audio(urls, concurrent_fragments):
    """
    Download youtube videos audio
    """
    opts = {
        "writethumbnail": True,
        "outtmpl": "%(title)s.%(ext)s",
        "ignoreerrors": True,
        "format": "bestaudio/best",
        "continuedl": True,
        "windowsfilenames": True,
        "concurrent_fragment_downloads": concurrent_fragments,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata", "add_metadata": "True"},
            {"key": "EmbedThumbnail"},
        ],
    }

    yt = yt_dlp.YoutubeDL(opts)

    yt.download(urls)


@click.command()
@click.argument(
    "url",
    type=str,
)  # Channel url, Example: 'https://www.youtube.com/@USER'
@click.option(
    "-v",
    "--videos",
    is_flag=True,
    show_default=True,
    default=False,
    help="Download all videos",
)
@click.option(
    "-s",
    "--shorts",
    is_flag=True,
    show_default=True,
    default=False,
    help="Download all shorts",
)
@click.option(
    "-a",
    "--audio",
    is_flag=True,
    show_default=True,
    default=False,
    help="Download all videos/shorts as mp3 files",
)
@click.option(
    "-N",
    "--concurrent-fragments",
    default=1,
    type=int,
    help="Number of fragments of a dash/hlsnative video that should be downloaded concurrently",
)
def channel(url, videos, shorts, audio, concurrent_fragments):
    """
    Download all youtube videos from channel
    save video id to ids.json and check if video is already downloaded
    """
    opts = {
        "writethumbnail": True,
        "outtmpl": "[%(upload_date>%Y-%m-%d)s] %(title)s.%(ext)s",
        "ignoreerrors": True,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "continuedl": True,
        "windowsfilenames": True,
        "concurrent_fragment_downloads": concurrent_fragments,
        "download_archive": "archive.log",
        "postprocessors": [
            {"key": "FFmpegMetadata", "add_metadata": "True"},
            {"key": "EmbedThumbnail"},
        ],
    }

    if audio:
        opts["outtmpl"] = "%(title)s.%(ext)s"
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata", "add_metadata": "True"},
            {"key": "EmbedThumbnail"},
        ]

    yt = yt_dlp.YoutubeDL(opts)

    if url.endswith("/"):
        url = url[:-1]

    if url.endswith("/videos"):
        url = url.replace("/videos", "")
    elif url.endswith("/shorts"):
        url = url.replace("/shorts", "")

    if videos:
        url += "/videos"
    elif shorts:
        url += "/shorts"
    else:
        click.echo("ERROR: Please specify what to download!")
        exit(1)

    yt.download(url)


@click.group()
def main_cli():
    ...


main_cli.add_command(video)
main_cli.add_command(audio)
main_cli.add_command(channel)


if __name__ == "__main__":
    main_cli()
