from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = "YT_API_KEY"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.service = Channel.get_service()
        self.channel = self.service.channels().list(id=self.channel_id, part='snippet,statistics').execute()


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)
