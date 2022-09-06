from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from db import models
from db.database import engine
from routers import userRouter,postRouter,commentRoute
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI();
app.include_router(userRouter.router)
app.include_router(postRouter.router)
app.include_router(authentication.router)
app.include_router(commentRoute.router)
@app.get("/")
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)

origins = ['http://localhost:3000'];
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=['*'],
    allow_headers = ['*'],
    allow_methods=['*']
)
app.mount('/images', StaticFiles(directory='images'), name='images')
