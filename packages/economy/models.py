from sqlalchemy import Column, Integer, ForeignKey, String
from packages.world_engine.engine import Base

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    seller_id = Column(String, ForeignKey('players.id'), nullable=False)
    buyer_id = Column(String, ForeignKey('players.id'), nullable=False)
    price = Column(Integer, nullable=False)
