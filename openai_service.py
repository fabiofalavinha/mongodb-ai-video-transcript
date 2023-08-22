import openai as openai


class OpenAIService:
    CHAT_MODEL = "gpt-3.5-turbo"
    SEARCH_ENGINE = "text-embedding-ada-002"

    def __init__(self) -> None:
        self.__model = self.CHAT_MODEL
        openai.api_key = "openai.key"
        openai.api_type = "openai.api.type"
        openai.api_base = "openai.api.base"
        openai.api_version = "openai.api.version"

    def getOpenAIBase(self) -> str:
        return openai.api_base

    def getOpenAIType(self) -> str:
        return openai.api_type

    def getOpenAIKey(self) -> str:
        return openai.api_key

    def getOpenAIVersion(self) -> str:
        return openai.api_version

    def promptChatCompletion(self, messages: []) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.__model,
                engine=self.__model,
                messages=messages
            )
            return response.choices[0].message["content"]
        except Exception as ex:
            raise Exception(f"Error creating a chat completion prompt using [{messages}]: {ex}")
