from fastapi import FastAPI
from src.app.points.routers import router


app = FastAPI()

app.include_router(router)
