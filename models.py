from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.publisher_id'))
    publisher = relationship("Publisher")

class Shop(Base):
    __tablename__ = 'shop'
    shop_id = Column(Integer, primary_key=True)
    name = Column(String)

class Stock(Base):
    __tablename__ = 'stock'
    stock_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.book_id'))
    shop_id = Column(Integer, ForeignKey('shop.shop_id'))
    count = Column(Integer)

class Sale(Base):
    __tablename__ = 'sale'
    sale_id = Column(Integer, primary_key=True)
    price = Column(Float)
    sale_date = Column(Date)
    stock_id = Column(Integer, ForeignKey('stock.stock_id'))
    count = Column(Integer)