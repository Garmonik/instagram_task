from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, loginusername, loginpassword):
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        my_username = driver.find_element(By.NAME, "username")
        my_password = driver.find_element(By.NAME, "password")
        my_username.send_keys(loginusername)
        my_password.send_keys(loginpassword)
        my_password.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Не сейчас')]")))
        add_to_home_screen_button = driver.find_element_by_xpath("//button[contains(text(), 'Не сейчас')]")
        add_to_home_screen_button.click()
        cookies = driver.get_cookies()
        print("Вы успешно авторизовались на Instagram")
        return True
    except:
        print("Произошла ошибка!!!")
        return False


def get_photos(driver, loginusername, loginpassword, username, max_count):
    res = login(driver, loginusername, loginpassword)
    if res:
        driver.get(f'https://www.instagram.com/{username}/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        photos = driver.find_elements(By.CSS_SELECTOR, 'article img')
        links = [photo.get_attribute('src') for photo in photos[:max_count]]
        return links
    else:
        return False


def post_photos(driver, loginusername, loginpassword, caption, photos):
    res = login(driver, loginusername, loginpassword)
    if res:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Опубликовать')]")))
        publish_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Опубликовать')]")
        publish_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        for photo in photos:
            photo_input = driver.find_element(By.XPATH, "//input[@type='file']")
            photo_input.send_keys(photo.file)
        caption_input = driver.find_element(By.XPATH, "//textarea[@aria-label='Подпись']")
        caption_input.send_keys(caption)
        publish_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Опубликовать')]")
        publish_button.click()
        post_url = driver.current_url
        return post_url
    else:
        return False