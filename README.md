# YouTube Video Utility

## Introduction
This Python utility provides functionality to interact with YouTube videos using the `pytube` library. It allows you to retrieve video information, list available streams, and download videos in the highest resolution available.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Get Video Information](#get-video-information)
  - [List Available Streams](#list-available-streams)
  - [Download Video](#download-video)
- [Features](#features)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Installation
To use this utility, you need to have Python installed along with the `pytube` library.

1. Install Python: [Python Downloads](https://www.python.org/downloads/)
2. Install `pytube`:
   ```bash
   pip install pytube
   ```

## Usage

### Get Video Information
This function retrieves various information about a YouTube video, including title, description, views, rating, length, author, publish date, keywords, and thumbnail URL.

```python
from pytube import YouTube

def get_video_info(video_url):
    video = YouTube(video_url)
    video_info = {
        "title": video.title,
        "description": video.description,
        "views": video.views,
        "rating": video.rating,
        "length": video.length,
        "author": video.author,
        "publish_date": video.publish_date,
        "keywords": video.keywords,
        "thumbnail_url": video.thumbnail_url,
    }
    return video_info
```

### List Available Streams
This function lists all available progressive streams for a YouTube video, including the itag, resolution, mime type, and file size.

```python
from pytube import YouTube

def list_available_streams(video_url):
    video = YouTube(video_url)
    streams = video.streams.filter(progressive=True)
    available_streams = [
        {
            "itag": stream.itag,
            "resolution": stream.resolution,
            "mime_type": stream.mime_type,
            "filesize": stream.filesize,
        } for stream in streams
    ]
    return available_streams
```

### Download Video
This function downloads the YouTube video in the highest resolution available to a specified output path.

```python
from pytube import YouTube

def download_video(video_url, output_path='.'):
    video = YouTube(video_url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path)
    return f"Video downloaded to {output_path}"
```

## Features
- Retrieve detailed information about a YouTube video.
- List all available progressive streams for a video.
- Download a YouTube video in the highest resolution available.

## Dependencies
- `pytube`: A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

Install dependencies using pip:
```bash
pip install pytube
```

## Examples

### Example Usage
Here's an example of how to use the utility:

```python
if __name__ == '__main__':
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Get video info
    video_info = get_video_info(video_url)
    print("Video Info:", video_info)

    # List available streams
    streams = list_available_streams(video_url)
    print("Available Streams:", streams)

    # Download video
    download_message = download_video(video_url, output_path='.')
    print(download_message)
```

## Contributors
- [Your Name](https://github.com/yourprofile)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.