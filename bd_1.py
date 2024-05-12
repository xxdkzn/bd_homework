from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Publisher, Book, Shop, Stock, Sale

# Создание соединения с базой данных
engine = create_engine('postgresql://username:your_password@localhost:5432/db_name')

# Создание сессии для работы с моделями
Session = sessionmaker(bind=engine)
session = Session()