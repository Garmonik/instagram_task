from fastapi import APIRouter, File, UploadFile, status
import asyncio
from typing import List
from selenium import webdriver

from dependencies import login, get_photos, post_photos
from main import driver

instagram_router = APIRouter()


@instagram_router.get("/login/instagram", status_code=status.HTTP_200_OK)
async def login_instagram(username: str, password: str) -> dict:
    my_driver = webdriver.Chrome()
    res = await asyncio.gather(login(my_driver, username, password), return_exceptions=True)
    return {"res": str(res)}


@instagram_router.get("/getPhotos/", status_code=status.HTTP_200_OK)
async def get_some_photos(loginusername: str, loginpassword: str, username: str, max_count: int) -> dict:
    my_driver = webdriver.Chrome()
    url = await asyncio.gather(get_photos(my_driver, loginusername, loginpassword, username, max_count), return_exceptions=True)
    driver.quit()
    if url:
        return {"postURL": url}
    else:
        return {"message": "Some error with login!!!"}


@instagram_router.post("/getPhotos/", status_code=status.HTTP_201_CREATED)
async def post_some_photos(loginusername: str, loginpassword: str, caption: str, photos: List[UploadFile] = File(...)) -> dict:
    my_driver = webdriver.Chrome()
    url = await asyncio.gather(post_photos(my_driver, loginusername, loginpassword, caption, photos), return_exceptions=True)
    driver.quit()
    if url:
        return {"postURL": url}
    else:
        return {"message": "Some error with login!!!"}