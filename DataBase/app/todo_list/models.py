from DataBase.app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean

# model name should be PascalCase
# mysql models must be defined length of string
class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50))
    priority = Column(Integer, index=True, default=3)
    done = Column(Boolean, index=True, default=False)
