import os

from helper.youtube_api_manual import youtube, api_key
from googleapiclient.discovery import build


def get_service():
    return youtube


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_id)

    @staticmethod
    def get_service():
        return build('youtube', 'v3', developerKey=api_key)
