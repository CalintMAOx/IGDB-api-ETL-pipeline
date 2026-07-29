from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(Integer)
    rating = Column(Float)
    number_of_ratings = Column(Integer)

    def __repr__(self) -> str:
        return f"Game(id={self.id}, name={self.name})"
