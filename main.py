from fastapi import FastAPI
from core.config import settings


app = FastAPI(title=settings.PORJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
   return {"detail": "Hello word"}