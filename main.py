import asyncio
from typing import List
import uvicorn
from fastapi import FastAPI, File, UploadFile
from selenium import webdriver
from dependencies import login, get_photos, post_photos
from routers.instagram import instagram_router

app = FastAPI()
driver = webdriver.Chrome()

app.include_router(instagram_router, prefix='')


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)