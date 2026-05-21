from fastapi import FastAPI, Request
from database import Base, engine
from fastapi.templating import Jinja2Templates
from routers.lead_router import router as lead_router
Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(lead_router)
