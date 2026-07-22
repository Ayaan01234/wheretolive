from fastapi import FastAPI
from sqlmodel import SQLModel
from sqlalchemy.exc import OperationalError
from database import engine
from routers import cities, auth, rankings, ai, comparisons
from middlewares.logging_middleware import log_requests 



app = FastAPI(title="WhereToLive API")
app.include_router(cities.router)
app.include_router(auth.router)
app.include_router(rankings.router)
app.include_router(ai.router)

app.include_router(comparisons.router)

# Loggin Middlware
app.middleware('http')(log_requests)