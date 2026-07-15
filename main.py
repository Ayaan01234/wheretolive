from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.exc import OperationalError
from database import engine
from routers import cities, auth, rankings, ai, comparisons

app = FastAPI(title="WhereToLive API")
@app.on_event("startup")
def on_startup():
  
  try:
    SQLModel.metadata.create_all(engine)
    print("Database Connected Successfully!")
  except OperationalError as e:
   print("Database Connection Failed:", e)


app.include_router(cities.router)
app.include_router(auth.router)
app.include_router(rankings.router)
app.include_router(ai.router)
app.include_router(comparisons.router)