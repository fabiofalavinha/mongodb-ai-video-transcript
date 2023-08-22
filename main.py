import argparse

from link_factory import LinkFactory
from mongodb_repository import MongoDbRepository
from openai_service import OpenAIService
from search_service import MongoDBSearchService
from viceo_configuration_actions import VideoConfigurationActions
from video_service import VideoService


def main():
    parser = argparse.ArgumentParser(description='Process and transcribe YouTube videos.')
    parser.add_argument('--youtube', type=str, required=True, help='YouTube link for transcription.')
    parser.add_argument('--searchFor', type=str, help='Text to search for in previously processed video transcriptions.')
    args = parser.parse_args()

    linkFactory = LinkFactory()
    youtube_link = linkFactory.create_link(args.youtube)

    repository = MongoDbRepository("mongodb_connection_string", "database_name", "collection_name")
    openAiService = OpenAIService()
    searchService = MongoDBSearchService("collection_name", openAiService)

    video_actions = (VideoConfigurationActions()
                     .enable_ai(openAiService)
                     .summarization()
                     .code_analysis()
                     .build())
    videoService = VideoService()

    if not args.searchFor:
        result = videoService.generate_transcription(youtube_link, video_actions)
        videoTranscript = result.video_transcription
        print(videoTranscript)

        videoDocument = repository.insertOne(videoTranscript)
        videoSummaryEmbeddings = searchService.createEmbedding(videoTranscript.summary)
        repository.storeEmbedding(video_id=videoDocument["_id"], embedding=videoSummaryEmbeddings)
    else:
        search_results = searchService.searchBy(args.searchFor)
        for r in search_results:
            print(r['videoUrl'])


if __name__ == '__main__':
    main()
