import argparse

from mongodb_repository import MongoDbRepository
from openai_service import OpenAIService
from search_service import MongoDBSearchService
from video_service import VideoService
from video_service_facade import VideoServiceFacade


def main():
    parser = argparse.ArgumentParser(description='Process and transcribe YouTube videos.')
    parser.add_argument(
        '--prompt',
        type=str,
        required=True,
        help='Prompt a YouTube question with the link. You can include in '
             'the question what do you want to know about the video')
    args = parser.parse_args()

    mongoDbRepository = MongoDbRepository("mongodb_connection_string", "database_name", "collection_name")
    openAiService = OpenAIService()
    searchService = MongoDBSearchService("collection_name", openAiService)
    videoService = VideoService()

    facade = VideoServiceFacade(openAiService, videoService, searchService, mongoDbRepository)

    videoProcessResult = facade.processVideo(args.prompt)

    if videoProcessResult.search_query:
        similarities = facade.performSearch(videoProcessResult)
        print("Search Results:", similarities)
    else:
        print("Video request was processed: ", videoProcessResult)


if __name__ == '__main__':
    main()
