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

def download_video(video_url, output_path='.'):
    video = YouTube(video_url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path)
    return f"Video downloaded to {output_path}"

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



if __name__ == '__main__':
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Get video info
    video_info = get_video_info(video_url)
    print("Video Info:", video_info)


    # List available streams
    streams = list_available_streams(video_url)
    print("Available Streams:", streams)