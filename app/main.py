from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import tasks
from fastapi.staticfiles import StaticFiles

#creates all tables in the database if they don't exist already
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Include the tasks router
print("including router...")
app.include_router(tasks.router)
print("done")

@app.get("/health")
def health_check():
    return {"status": "ok"}