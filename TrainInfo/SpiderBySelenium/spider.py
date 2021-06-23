from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

path = "C:\\Users\\Admin\\PycharmProjects\\PortMapping\\venv\\Scripts\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options,executable_path=path)

def Traverse_html():
    driver.get("http://search.huochepiao.com/checi/D1")
    html = driver.page_source
    driver.quit()
    print(html)
    fileopen = open("C:\\Users\\Admin\\PycharmProjects\\info_trains\\TrainInfo\\test\\html.txt",'w',encoding='utf-8')
    fileopen.write(html)
    fileopen.close()

Traverse_html()