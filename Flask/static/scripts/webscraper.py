from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.google.com/maps/'
browser = webdriver.Chrome('chromedriver.exe' ,chrome_options=chrome_options)
browser.get(url)


# WebDriverWait(browser, 10)
# try:
#     element = WebDriverWait(browser, 10).until(
#         browser.find_element(By.XPATH, '//*[@id="thumbnail"]').click()
#     )
# finally:
#     browser.quit()

# browser.implicitly_wait(15)
time.sleep(10) # to wait 10 seconds
# searchbox=browser.find_element(By.ID, 'search')
# searchbox.send_keys("Epic Time")

# searchicon = browser.find_element(By.ID, 'search-icon-legacy')
# searchicon.click()
searchbox = browser.find_element(By.ID, 'searchboxinput')
searchbox.click()
searchbox.send_keys('ร้านขายขยะใกล้ฉัน')
searchicon = browser.find_element(By.ID, 'searchbox-searchbutton')
searchicon.click()

# actions = ActionChains(browser)
# actions.click(viewvideo).perform


