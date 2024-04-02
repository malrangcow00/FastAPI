from fastapi import APIRouter

import models
from DataBase.app.core.database import engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)