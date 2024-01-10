<img src="./images/banner.png" width="800">

# YouTube Downloader

Welcome to the YouTube Downloader Project! In this project, you will develop a Python application that allows users to download YouTube videos for offline viewing. Your mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the `pytube` library, user input handling, and feedback mechanisms such as a download progress bar.

Users should be able to run YouTube Downloader from the command line or used as a module in other Python scripts. Here are the basic steps to use the tool:

```sh
python youtube_downloader.py <youtube-url> <video-quality> <output-directory>
```
You can also use argparse to parse the command line arguments. The following is an example of how to use argparse to parse the command line arguments:

```sh
python youtube_downloader.py --url <youtube-url> --quality <video-quality> --output <output-directory>
```

And the video(s) will be downloaded to the specified output directory.

## Learning Objectives

By completing this project, you will:

- Learn to use the `pytube` library to interact with YouTube content.
- Understand how to filter and select video streams based on parameters like resolution and file extension.
- Create a command-line interface (CLI) for user interaction.
- Implement a progress bar to show download progress.
- Practice exception handling for a robust application.
- Manage file input/output in Python.

## Features

- **Command Line Interface (CLI)**: A simple CLI for easy interaction with the downloader. This is the primary interface through which users will interact with your application.
- **Graphical User Interface (GUI)**: As an advanced feature, consider developing a GUI using a library like `streamlit` for a more user-friendly experience. This is optional but can greatly enhance usability.
- **Download Progress Bar**: Incorporate real-time feedback on the download progress so users can see how much of the video has been downloaded.
- **Configurable Settings**: Allow users to set default download folders, preferred video quality, and other settings to customize their experience.
- **Playlist Downloading**: Another advanced feature is to enable users to download entire playlists in addition to individual videos.
- **Audio Extraction**: Give users the option to download only the audio track of a video in MP3 format.
- **Error Handling**: Gracefully handle common errors, such as invalid URLs or network issues.

## How to Use the `pytube` Library

You are encouraged to use the `pytube` library for this project, which is a Python library for interfacing with YouTube content. It allows you to query for metadata about videos, streams, and playlists; as well as download video and audio streams.

To learn more about `pytube`, you can explore the official documentation and this [repo](https://github.com/pytube/pytube/tree/master). It will guide you through the process of using `pytube` and help you implement the required features for the project.

Good luck with your project, and enjoy the process of creating your own YouTube Downloader!

## How Do YouTube Downloaders Work? [Optional]
YouTube downloaders work by extracting the video stream from YouTube and allowing you to save it to your device. While YouTube itself does not provide a download button for all videos (except for some that can be downloaded within the YouTube mobile app for offline viewing), third-party tools are able to bypass this by using various methods. Here's a simplified explanation of how they generally work:

- Retrieving Video Information: When you input a YouTube video URL into a downloader, the tool sends a request to YouTube servers pretending to be a client requesting video playback. It retrieves the page data that contains information about the video stream.

- Extracting the Stream URL: YouTube streams video using adaptive bitrate streaming techniques like MPEG-DASH or HLS (HTTP Live Streaming). The downloader parses the information to find the direct URLs to the video and audio streams, which are typically segmented into small chunks to adapt to different bandwidths and devices.

- Combining Video and Audio: In some cases, video and audio are streamed separately to optimize for various network conditions. The downloader might need to download both streams and combine them into a single file. This is often done with the help of additional software like FFmpeg.

- Initiating the Download: Once the downloader has the correct stream URLs, it can begin downloading the video and audio chunks. Even if the video is streamed in small pieces, the downloader will piece together these segments to form a complete video file.

- Conversion (if necessary): If the user wants the video in a different format than what YouTube provides, the downloader can convert the video into the desired format, like MP4, MP3, AVI, etc.

- Saving to the Device: After the video is downloaded and possibly converted, the file is saved to the user's device where it can be played back without needing an internet connection.

It's important to note that using third-party tools to download YouTube videos may violate YouTube's terms of service, which could result in the downloader tool being blocked or legal action against the service provider. Additionally, downloading copyrighted content without permission is illegal in many jurisdictions, and could result in legal consequences for the user as well.