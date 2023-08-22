from langchain.document_loaders import YoutubeLoader

from viceo_configuration_actions import VideoConfigurationActions
from video_transcript import VideoTranscript
from video_transcription_result import VideoTranscriptResult
from youtube_link import YouTubeLink


class VideoService:
    def generate_transcription(self, link: YouTubeLink, video_actions: VideoConfigurationActions) -> VideoTranscriptResult:
        print(f"Loading YouTube video [{link.url}]...")

        # Load video transcript from YouTube
        loader = YoutubeLoader.from_youtube_url(link.url, add_video_info=True)
        result = loader.load()

        # Extract video metadata and transcript
        video_transcription = VideoTranscript()
        for document in result:
            video_transcription.metadata = document.metadata
            video_transcription.transcript = document.page_content

        # If AI is enabled, process the transcript
        if video_actions.ai_enabled:
            openai_service = video_actions.openai_service
            try:
                print(f"Summarizing YouTube video transcript [{link.url}]...")
                summarized_response = openai_service.prompt_chat_completion(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant who has access to a video transcript. "
                                       "Use this information to provide detailed and context-rich explanations."
                        },
                        {
                            "role": "user",
                            "content": f"Here is the transcript of a video that I would like you to analyze and explain. "
                                       f"Provide a summary of the key points and an analysis of the main themes presented "
                                       f"in the video using the below context? Context: {video_transcription.transcript}"
                        }
                    ]
                )
                video_transcription.summary = summarized_response.strip()
            except Exception as ex:
                print(f"Error summarizing YouTube video transcript [{link.url}]: {ex}")
                video_transcription.summary = f"Error summarizing YouTube video transcript [{link.url}]: {ex}"

        # If code analysis is enabled, analyze the code (dummy logic as real logic wasn't provided)
        if video_actions.code_analysis_enabled:
            video_transcription.code_analysis = "Sample code analysis result."

        # Return result
        return VideoTranscriptResult(video_transcription)