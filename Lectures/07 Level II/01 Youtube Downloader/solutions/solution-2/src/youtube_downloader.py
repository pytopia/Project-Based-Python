import argparse

## Because of a bug in pytube, we can use pytubefix instead
# from pytube import YouTube
# from pytube.exceptions import VideoUnavailable
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable
from tqdm import tqdm


class YouTubeDownloader:
    def __init__(self, url, quality="highest", output_path="."):
        self.url = url
        self.quality = quality
        self.output_path = output_path
        self.yt = YouTube(
            url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete,
        )
        self.pbar = None

    def download(self):
        try:
            # If user wants the highest resolution, use 'get_highest_resolution' filter
            if self.quality == "highest":
                video_stream = self.yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).get_highest_resolution()
            else:
                video_stream = self.yt.streams.filter(
                    progressive=True, res=self.quality, file_extension="mp4"
                ).first()

            if video_stream is None:
                available_qualities = [
                    str(stream.resolution)
                    for stream in self.yt.streams.filter(
                        progressive=True, file_extension="mp4"
                    )
                ]
                print(f"No streams found with the specified quality: {self.quality}")
                print(f"Title: {self.yt.title}")
                print(f"Available qualities: {available_qualities}")
                return

            # Initialize tqdm progress bar
            self.pbar = tqdm(
                total=video_stream.filesize,
                unit="B",
                unit_scale=True,
                desc=self.yt.title,
            )

            # Download the video
            video_stream.download(self.output_path)

        except VideoUnavailable as e:
            print("An error occurred:", e)
            if self.pbar:
                self.pbar.close()  # Ensure the progress bar is closed in case of error

    def on_progress(self, stream, chunk, bytes_remaining):
        """
        Updates the progress bar during the download.

        :param stream: Stream being downloaded.
        :param chunk: Chunk of data being downloaded.
        :param bytes_remaining: Number of bytes remaining to be downloaded.
        """
        current = stream.filesize - bytes_remaining
        self.pbar.update(current - self.pbar.n)  # update pbar with the downloaded bytes

    def on_complete(self, stream, file_path):
        """
        Completes the progress bar and prints the download completion message.

        :param stream: Stream that has been downloaded.
        :param file_path: The file path of the downloaded video.
        """
        self.pbar.close()
        print(f"\nDownloaded '{self.yt.title}' successfully to: {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Download a YouTube video at a specified quality and output path."
    )

    parser.add_argument("url", help="The YouTube URL to download")
    parser.add_argument(
        "-q",
        "--quality",
        help="The desired video quality (e.g., 720p, 1080p, highest)",
        default="highest",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output_path",
        help="The output directory to save the video",
        default=".",
        type=str,
    )

    args = parser.parse_args()

    downloader = YouTubeDownloader(args.url, args.quality, args.output_path)
    downloader.download()


if __name__ == "__main__":
    main()
