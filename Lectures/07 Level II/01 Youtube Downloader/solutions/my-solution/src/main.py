import argparse
from pathlib import Path

from pytube import YouTube
from tqdm import tqdm
from pytube.exceptions import VideoUnavailable


class YouTubeDownloader:
    def __init__(self, url, output_path=None, quality=None):
        self.url = url
        self.output_path = output_path or Path.cwd()
        self.quality = quality or 'highest'
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete,
        )

    def download(self):
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print('Video is unavailable')
            return

        if self.quality == 'highest':
            stream = self.yt.streams.filter(
                progressive=True, file_extension='mp4'
            ).get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True,
                file_extension='mp4',
                res=self.quality
            ).first()

        self.pbar = tqdm(
            desc='Downloading ...',
            total=stream.filesize,
            unit='B',
            unit_scale=True,
        )

        stream.download(self.output_path)

    def on_progress(self, stream, chunk, bytes_remaining):
        current = stream.filesize - bytes_remaining
        self.pbar.update(current - self.pbar.n)

    def on_complete(self, stream, file_path):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='YouTube Downloader'
    )
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-q', '--quality', help='Video quality', default='highest')
    parser.add_argument('-o', '--output_path', help='Output path', default=None)

    args = parser.parse_args()

    YouTubeDownloader(
        url=args.url,
        quality=args.quality,
        output_path=args.output_path,
    ).download()
