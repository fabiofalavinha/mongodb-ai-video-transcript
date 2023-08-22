from link import Link
from youtube_link import YouTubeLink


class LinkFactory:
    @staticmethod
    def create_link(url: str) -> Link:
        if "youtube.com" in url:
            return YouTubeLink(url)
        else:
            raise ValueError(f"Unsupported URL: {url}")
