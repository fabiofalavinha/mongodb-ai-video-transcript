import json

from viceo_configuration_actions import VideoConfigurationActions
from video_process_result import VideoProcessResult


class VideoServiceFacade:
    def __init__(self, openai_service, video_service, search_service, mongo_repository):
        self.openai_service = openai_service
        self.video_service = video_service
        self.search_service = search_service
        self.mongo_repository = mongo_repository

    def processVideo(self, user_prompt):
        # Step 1: Process the prompt with OpenAIService using the ChatCompletion API
        system_message = "You are a helpful assistant who can interpret YouTube links and suggest actions. " \
                         "When the user refers to summarization output the 'Summarize' action in the 'Actions' json array." \
                         "When the user refers to code analysis output the 'Code Analysis' action int he 'Actions' json array." \
                         "The output should be a JSON structure with the fields: YouTubeLink: string and Actions: [array of string - 'Summarize', 'Code Analysis']." \
                         "The default option in the 'Actions' json array always will be 'GenerateTranscript' as the first option."
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ]

        ai_response = self.openai_service.promptChatCompletion(messages=messages)
        ai_result = json.loads(ai_response)  # Assuming that promptChatCompletion returns a JSON-formatted string

        # Step 2: Extract the YouTubeLink and Actions from AI's answer
        youtube_link = ai_result.get('YouTubeLink', None)
        actions = ai_result.get('Actions', [])

        # Step 3: Perform actions using VideoService
        config_actions = VideoConfigurationActions()
        if 'Summarize' in actions:
            config_actions.enable_ai(self.openai_service).summarization()
        if 'CodeAnalysis' in actions:
            config_actions.code_analysis()

        # Add the step to store summary as embeddings into MongoDB
        videoTranscriptResult = self.video_service.generateTranscription(youtube_link, config_actions.build())
        videoTranscript = videoTranscriptResult.video_transcription
        videoDocument = self.mongo_repository.insertOne(videoTranscript)
        videoSummaryEmbeddings = self.search_service.createEmbedding(videoTranscript.summary)
        self.mongo_repository.storeEmbedding(video_id=videoDocument["_id"], embedding=videoSummaryEmbeddings)

        # Step 4: Construct the result
        search_query = ai_result.get('SearchFor', None)
        process_result = VideoProcessResult(youtube_link, actions, search_query)

        return process_result

    def performSearch(self, video_process_result):
        # Assuming searchBy returns an array of similarities
        similarities = self.search_service.searchBy(video_process_result.search_query)
        return similarities
