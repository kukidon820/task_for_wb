from sqlalchemy import Column, Integer, String, Float
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Float)
    reviews = Column(Integer)