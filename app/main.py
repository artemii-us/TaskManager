import uvicorn
from controller.task_controller import router as task_router
from database.base import Base
from database.session import engine
from fastapi import FastAPI

app = FastAPI()
app.include_router(task_router)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
