from pytube import YouTube
from typing import Union


def download_youtube_video(url_video: str = None, reg: Union[str, int] = None, quality: str = "video/mp4") -> tuple | str:
    """
        Скачивает YouTube видео по ссылке.
        :param url_video:
        :param reg:
        :return:
    """

    obj_youtube: YouTube = YouTube(url=url_video)

    title_video = obj_youtube.title
    video_photo_icon_url = obj_youtube.thumbnail_url

    if reg:

        all_url_videos: list = obj_youtube.streams.filter(res=reg, mime_type=quality)


        # Download to directory 'videos'
        try:

            to_downalod = obj_youtube.streams.get_by_itag(all_url_videos[0].itag)
            to_downalod.download("videos")

        except IndexError as ie:

            return "Неправильные переданные данные"

        else:

            print("Success")

        finally:

            return "Completion"

    return title_video, video_photo_icon_url

print(download_youtube_video(url_video="https://www.youtube.com/watch?v=YSKWSSBjbRE", reg="1080p", quality="video/mp4"))
