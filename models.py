from sqlalchemy import Column, Integer, String, Float, Date , Text, DateTime, func
from database import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)  # Assuming a decimal number for price
    trade_date = Column(Date)



class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text)
    gpt_response = Column(Text)
    # created_at = Column(DateTime(timezone=True), server_default=func.now())