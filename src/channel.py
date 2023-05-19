import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.service = Channel.get_service()
        self.channel = self.service.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.get_channel_info()
        print(f"id канала: {channel_info['id']}")
        print(f"Название канала: {channel_info['title']}")
        print(f"Описание канала: {channel_info['description']}")
        print(f"количество видео: {channel_info['video_count']}")
        print(f"количество просмотров: {channel_info['views_count']}")
        print(f"Количество подписчиков: {channel_info['subscriberCount']}")
        print(f"ссылка на канал: {channel_info['url']}")

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self):
        return self.__channel_id

    def to_json(self, filename):
        channel_dict = {"id": self.channel_id,
                        "title": self.title,
                        "video_count": self.video_count,
                        "url": self.url,
                        "description": self.description,
                        "subscriberCount": self.subscriberCount,
                        "views_count": self.views_count
                        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(channel_dict, f, indent=2, ensure_ascii=False)


