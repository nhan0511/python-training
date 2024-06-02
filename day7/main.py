import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://vnexpress.net/")

a_tag = browser.find_element(By.XPATH, "/html/body/section[5]/div/div/div/article/h3/a")
print(a_tag.text)

link = browser.find_element(By.XPATH, "/html/body/section[2]/nav/ul/li[7]/a")
link.click()

pods = browser.find_elements(By.XPATH, "/html/body/section[6]/div/div[1]/div[2]/article")

for p in pods:
    title = p.find_element(By.XPATH, "h3/a")
    image = p.find_element(By.XPATH, "div[1]/a/picture/img")
    paragraph = p.find_element(By.XPATH, "p/a")
    print(title.text)
    print(paragraph.text)
    print(image.get_attribute("src"))


# time.sleep(5)
input()