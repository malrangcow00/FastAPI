from fastapi import FastAPI
from app.todo_list.main import router as todo_list_router

app = FastAPI()

app.include_router(todo_list_router, prefix="/todo_list")