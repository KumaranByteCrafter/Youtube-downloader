
# YT Downloader

## Introduction
YT Downloader is a versatile tool designed to download videos from YouTube. It comes in two flavors: a command-line interface (CLI) version for those who prefer terminal-based interactions, and a graphical user interface (GUI) version for users who prefer graphical applications. The tool is built using Python and leverages the `pytube` library for downloading videos.

## Requirements
- Python 3.x
- `pytube` library

## Installation
To use YT Downloader, you need to install the required Python libraries. You can install these using pip:

```bash
pip install pytube
```

## Usage

### CLI Version
To use the CLI version, run the `yt_downloader_cli.py` script from the command line. You can download videos by providing the YouTube URL and specifying the download path. The CLI also supports downloading only the audio of the video.

```bash
python yt_downloader_cli.py <YouTube URL> <Download Path> [--audio-only]
```

### GUI Version
To use the GUI version, execute the `yt_downloader_gui.py` script. The GUI provides an easy-to-use interface for entering the YouTube URL, choosing the download path, and selecting between video and audio download.

```bash
python yt_downloader_gui.py
```

## Features
- Download videos in good resolution automatically.
- Option to download only the audio of the video.
- Progress indicator for download status (GUI version).
- Simple and user-friendly interface for the GUI version.
- Efficient and fast downloading using threading (CLI & GUI).

## Contributions
Contributions to YT Downloader are welcome! If you'd like to contribute, feel free to fork the repository and submit a pull request with your changes. We are open to new features, bug fixes, and any improvements.
