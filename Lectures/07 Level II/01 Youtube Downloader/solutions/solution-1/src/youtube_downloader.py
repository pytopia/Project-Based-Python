import argparse

from pytube import YouTube
from tqdm import tqdm


def download_video(url, quality, output_path):
    """
    Downloads a YouTube video at the specified quality and output path.

    :param url: The URL of the YouTube video to download.
    :param quality: The desired video quality (e.g., '720p', '1080p', 'highest').
    :param output_path: The directory path to save the downloaded video.
    """
    try:
        yt = YouTube(url)

        # If user wants the highest resolution, use 'get_highest_resolution' filter
        if quality == 'highest':
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        else:
            video_stream = yt.streams.filter(progressive=True, res=quality, file_extension='mp4').first()

        if video_stream is None:
            print(f"No streams found with the specified quality: {quality}")
            return

        # Initialize tqdm progress bar
        pbar = tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc=yt.title)

        def on_progress(stream, chunk, bytes_remaining):
            """
            Updates the progress bar during the download.

            :param stream: Stream being downloaded.
            :param chunk: Chunk of data being downloaded.
            :param bytes_remaining: Number of bytes remaining to be downloaded.
            """
            current = stream.filesize - bytes_remaining
            pbar.update(current - pbar.n)  # update pbar with the downloaded bytes

        yt.register_on_progress_callback(on_progress)

        # Download the video
        video_stream.download(output_path)

        # Close the progress bar after the download is complete
        pbar.close()
        print(f"\nDownloaded '{yt.title}' successfully to: {output_path}")

    except Exception as e:
        print("An error occurred:", e)
        pbar.close()  # Ensure the progress bar is closed in case of error
        return


def main():
    parser = argparse.ArgumentParser(description='Download a YouTube video at a specified quality and output path.')

    parser.add_argument('url', help='The YouTube URL to download')
    parser.add_argument(
        '-q', '--quality',
        help='The desired video quality (e.g., 720p, 1080p, highest)',
        default='highest',
        type=str
    )
    parser.add_argument('-o', '--output_path', help='The output directory to save the video', default='.', type=str)

    args = parser.parse_args()

    download_video(args.url, args.quality, args.output_path)


if __name__ == "__main__":
    main()
