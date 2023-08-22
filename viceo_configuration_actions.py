class VideoConfigurationActions:
    def __init__(self):
        self._ai_enabled = False
        self._code_analysis_enabled = False
        self._openai_service = None

    def enable_ai(self, openai_service) -> 'VideoConfigurationActions':
        self._ai_enabled = True
        self._openai_service = openai_service
        return self

    def summarization(self) -> 'VideoConfigurationActions':
        return self

    def code_analysis(self) -> 'VideoConfigurationActions':
        self._code_analysis_enabled = True
        return self

    def build(self) -> 'VideoConfigurationActions':
        return self

    @property
    def ai_enabled(self) -> bool:
        return self._ai_enabled

    @property
    def code_analysis_enabled(self) -> bool:
        return self._code_analysis_enabled

    @property
    def openai_service(self):
        if not self._ai_enabled:
            raise ValueError("AI has not been enabled. Please enable AI before accessing the OpenAIService.")
        return self._openai_service
