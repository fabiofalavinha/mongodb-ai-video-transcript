class VideoProcessResult:
    def __init__(self, youtube_link, actions, search_query=None):
        self.youtube_link = youtube_link
        self.actions = actions
        self.search_query = search_query
