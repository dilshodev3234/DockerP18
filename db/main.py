from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column
import os
from dotenv import load_dotenv
from sqlalchemy import engine
from sqlalchemy.orm import Session, declarative_base

load_dotenv()


class Config:
    DB_NAME = os.getenv("DB_NAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = engine.create_engine(Config().DB_URL)
session = Session(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    chat_id: Mapped[int] = mapped_column(__type_pos=BIGINT, primary_key=True)
    fullname: Mapped[str] = mapped_column(nullable=True)


