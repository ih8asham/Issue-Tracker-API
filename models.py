from sqlalchemy import String, Integer, Column, Text
from database import Base 

class Issue(Base):
    __tablename__ = "issues" 
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String(200), nullable=False)
    description=Column(Text, nullable=False)
    category=Column(String(100), nullable=False)
    priority=Column(String(20), default="Medium")
    status=Column(String(30), default="Open") 
    
    
    
    