from database import Base
from sqlalchemy import Column, Integer, String, Boolean

# model name should be PascalCase
class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    priority = Column(Integer, index=True, default=3)
    status = Column(Boolean, index=True, default=False)

class TodoList(Base):
    __tablename__ = 'todo_list'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(Boolean, index=True)