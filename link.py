class Link:
    def __init__(self, url: str):
        self._url = url

    @property
    def url(self) -> str:
        return self._url
