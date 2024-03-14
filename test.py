from pydantic import BaseModel
from pprint import pprint

game_dict = [
    {
        "id": 1,
        "title": "Hit the Code",
        "publisher": "MCGames",
        "description": "Quick start to learn coding!",
        "rating": 3,
        "published_date": 2024
    },
    {
        "id": 2,
        "title": "TEKKEN 8",
        "publisher": "Bandai Namco",
        "description": "Gorgeous impact with MS story",
        "rating": 5,
        "published_date": 2024
    },
    {
        "id": 3,
        "title": "KartRider: Drift",
        "publisher": "Nexon",
        "description": "Exciting Race, you never experience",
        "rating": 5,
        "published_date": 2023
    },
    {
        "id": 4,
        "title": "Lost Ark",
        "publisher": "SmileGate",
        "description": "Trash Game",
        "rating": 2,
        "published_date": 2018
    },
    {
        "id": 5,
        "title": "StarCraft",
        "publisher": "Blizard",
        "description": "The Greatest game of All Time",
        "rating": 5,
        "published_date": 1998
    },
    {
        "id": 6,
        "title": "StarCraft 2",
        "publisher": "Blizard",
        "description": "Unlucky StarCraft",
        "rating": 3,
        "published_date": 2010
    },
    {
        "id": 7,
        "title": "MS Story",
        "publisher": "Nexon",
        "description": "A gemble where no one wins",
        "rating": 1,
        "published_date": 2003
    },
    {
        "id": 8,
        "title": "Growing AI",
        "publisher": "MalrangCow",
        "description": "All developed by 1 person, the hottest developer in these days",
        "rating": 5,
        "published_date": 2024
    },
    {
        "id": 9,
        "title": "Crazy Arcade",
        "publisher": "Nexon",
        "description": "Bubble pop!",
        "rating": 4,
        "published_date": 2001
    }
]

# pprint(game_dict)

# 모델 인스턴스를 먼저 생성해주어야 한다.
class Game(BaseModel):
    id: int
    title: str
    publisher: str
    description: str
    rating: int
    published_date: int

# transform list to Game object(instance)
games = [Game(**game) for game in game_dict]

# print model instance transformed from the list
# for game in games:
#     # pprint(game.json()) # the 'json' method is deprecated; use 'mode_dump_json' instead
#     pprint(game.model_dump_json())
for game in games:
    # pprint(game.dict()) # the 'dict' method is deprecated; use 'mode_dump' instead
    pprint(game.model_dump())
# print(**game_dict.model_dump()) # AttributeError: 'list' object has no attribute 'model_dump'
# print(**game_dict) # TypeError: print() argument after ** must be a mapping, not list