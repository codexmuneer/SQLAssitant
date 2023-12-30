from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy import text


from chatbot import askgpt
from faker import Faker  # Add this import for generating fake data

# Create a Faker instance for generating fake data
fake = Faker()


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class TradeBase(BaseModel):
    stock_symbol: str
    quantity: int
    price: float
    trade_date: str  # Adjust the type based on your date representation


class ChatBase(BaseModel):
    user_query: str
    gpt_response: str
    # created_at: str

class UserQueryBase(BaseModel):
    input: str  # Define the structure of the JSON payload

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Initialization route
@app.post("/init-db")
async def initialize_db():
    init_db()
    return {"message": "Database initialized and populated with sample data."}

def init_db():
    # Create tables
    models.Base.metadata.create_all(bind=engine)

    # Insert sample data
    with SessionLocal() as session:
        for _ in range(10):  # Insert 10 random records as an example
            trade_data = TradeBase(
                stock_symbol=fake.company_suffix(),
                quantity=fake.random_int(min=1, max=100),
                price=fake.random.uniform(1.0, 1000.0),
                trade_date=fake.date_this_decade().isoformat(),
            )
            trade = models.Trade(**trade_data.dict())  # Convert to dict and pass to Trade model
            session.add(trade)

        # Commit the changes
        session.commit()


# Route to receive prompt, generate SQL, and execute
@app.post("/process-prompt")
async def process_prompt(user_query:  UserQueryBase, db: Session = Depends(get_db)): 
    try:
        input_data = user_query.input
        response = askgpt(input_data)
        print(response)
        query = text(response)
        results = db.execute(query)
        result_data = results.fetchall()
        print(result_data)
        result_list = [{"price": row[0]} for row in result_data]

        # query = response.get("query", "")
        # if query != "":
        # # Execute SQL query
        #     results = db.execute(query)

        # else:
        #     results = "model failed to created SQL query"

        # Store the chat in the database
        db_chat = models.Chat(user_query=input_data, gpt_response=response)
        db.add(db_chat)
        db.commit()


        return result_list
    
    except Exception as e:
        db.rollback()  # Rollback changes in case of an exception
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()  # Close the session in the finally block
