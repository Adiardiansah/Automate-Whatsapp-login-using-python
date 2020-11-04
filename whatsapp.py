from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverwait
from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import by

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver('D:/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverwait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Frien's Name"'

# Replace the below string with your own message
string = "Message sent using python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class=input"][@dir="auto"][@data-tab="1"]'
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + keys.ENTER)
    time.sleep(1)
