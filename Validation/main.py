from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

# Pydantics is the python library that is used for data modeling, data parsing and has efficient error handling.
# Pydantics is commonly used as a resource for data validation and how to handle data coming to FastAPI app

app = FastAPI()


# Define Object "Game"
class Game:
    id: int
    title: str
    publisher: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, publisher, description, rating, published_date):
        self.id = id
        self.title = title
        self.publisher = publisher
        self.description = description
        self.rating = rating
        self.published_date = published_date


# handle game info request from user
class GameRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    publisher: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6) # between 1 and 5 (greater than -1 and less than 6)
    published_date: int = Field(gt=1990, lt=2031)

    # example schema for swagger
    class Config:
        # pydantic v1 : schema_extra
        json_schema_extra = {
            'example': {
                # id is optional
                'title': 'A new game',
                'publisher': 'MalrangCow',
                'description': 'A new description of a game',
                'rating': 5,
                'published_date': 2024
            }
        }


Games = [
    Game(1, 'Hit the Code', 'MCGames', 'Quick start to learn coding!', 3, 2024),
    Game(2, 'TEKKEN 8', 'Bandai Namco', 'Gorgeous impact with MS story', 5, 2024),
    Game(3, 'KartRider: Drift', 'Nexon', 'Exciting Race, you never experience', 5, 2023),
    Game(4, 'Lost Ark', 'SmileGate', 'Trash Game', 2, 2018),
    Game(5, 'StarCraft', 'Blizard', 'The Greatest game of All Time', 5, 1998),
    Game(6, 'StarCraft 2', 'Blizard', 'Unlucky StarCraft', 3, 2010),
    Game(7, 'MS Story', 'Nexon', 'A gemble where no one wins', 1, 2003),
    Game(8, 'Growing AI', 'MalrangCow', 'All developed by 1 person, the hottest developer in these days', 5, 2024)
]


@app.get("/games", status_code=status.HTTP_200_OK)
async def read_all_games():
    return Games


# validate the input parameter (gt=0: greater than 0)
# add status code to the response
@app.get("/games/{game_id}", status_code=status.HTTP_200_OK)
async def read_game(game_id: int = Path(gt=0)):
    for game in Games:
        if game.id == game_id:
            return game
    raise HTTPException(status_code=404, detail='Item not found')


@app.get("/games/", status_code=status.HTTP_200_OK)
async def read_game_by_rating(game_rating: int = Query(gt=-1, lt=6)):
    games_to_return = []
    for game in Games:
        if game.rating == game_rating:
            games_to_return.append(game)
    return games_to_return


# if you want to make the parameter optional
# @app.get("/games", status_code=status.HTTP_200_OK)
# async def read_game_by_rating(game_rating: Optional[int] = Query(default=None, gt=0, lt=6)):
#     if game_rating is None:
#         return Games
#     games_to_return = []
#     for game in Games:
#         if game.rating == game_rating:
#             games_to_return.append(game)
#     return games_to_return


@app.get("/games/publish/", status_code=status.HTTP_200_OK)
async def read_games_by_publish_date(published_date: int = Query(gt=1990, lt=2031)):
    games_to_return = []
    for game in Games:
        if game.published_date == published_date:
            games_to_return.append(game)
    return games_to_return


# @app.post("/create-game", status_code=status.HTTP_201_CREATED)
# async def create_game(game_request: GameRequest):
#     new_game = game_request.model_dump()
#     if new_game['id'] is None:
#         new_game['id'] = 1 if len(Games) == 0 else Games[-1].id + 1
#     new_game = Game(**game_dict)
#     Games.append(new_game)
#     return new_game


# should define model instance first to use pydantic
# model_dump: transform model instance to dictionary (the 'dict' method is deprecated)
# model_dump_json: transform model instance to json (the 'json' method is deprecated)
@app.post("/create-game", status_code=status.HTTP_201_CREATED)
async def create_game(game_request: GameRequest):
    new_game = Game(**game_request.model_dump())
    Games.append(find_game_id(new_game))


# to prevent duplicate id
def find_game_id(game: Game):
    if game.id is None:
        # start from 1 if there is no game
        game.id = 1 if len(Games) == 0 else Games[-1].id + 1
    return game


@app.put("/games/update_game", status_code=status.HTTP_204_NO_CONTENT)
async def update_game(game: GameRequest):
    game_changed = False
    for i in range(len(Games)):
        if Games[i].id == game.id:
            Games[i] = game
            game_changed = True
    if not game_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/games/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: int = Path(gt=0)):
    game_changed = False
    for i in range(len(Games)):
        if Games[i].id == game_id:
            Games.pop(i)
            game_changed = True
            break
    if not game_changed:
        # raise an HTTPException
        raise HTTPException(status_code=404, detail='Item not found')
