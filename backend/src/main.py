from fastapi import FastAPI
from src.api.tokens import router as tokens_router

app = FastAPI()

app.include_router(tokens_router, prefix="/api")
