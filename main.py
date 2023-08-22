import argparse
from VideoService import VideoService
from VideoConfigurationActions import VideoConfigurationActions
from MongoDbRepository import MongoDbRepository

from link_factory import LinkFactory


def main():
    parser = argparse.ArgumentParser(description='Process and transcribe YouTube videos.')
    parser.add_argument('--youtube', type=str, required=True, help='YouTube link for transcription.')
    parser.add_argument('--searchFor', type=str,
                        help='Text to search for in previously processed video transcriptions.')
    args = parser.parse_args()

    # Initializing objects
    linkFactory = LinkFactory()
    youtube_link = linkFactory.create_link(args.youtube)

    # Assuming you have a configuration file with database details
    repository = MongoDbRepository("mongodb_connection_string", "database_name", "collection_name")

    # Let's assume the OpenAIService is already initialized as openAiService
    video_actions = (VideoConfigurationActions()
                     .enableAI(openAiService)
                     .summarization()
                     .codeAnalysis()
                     .build())

    videoService = VideoService(repository)

    if not args.searchFor:
        result = videoService.generateTranscription(youtube_link, video_actions)
        # You can print the result or do something else with it
        print(result.transcription)  # Just a sample action

    else:
        search_results = repository.searchBy(args.searchFor)
        for r in search_results:
            # Printing video URL for each match
            print(r['videoUrl'])


if __name__ == '__main__':
    main()
