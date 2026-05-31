from sqlalchemy import Column, String
from packages.world_engine.engine import Base

class Territory(Base):
    __tablename__ = 'territories'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(String, nullable=True) # Player or Guild
