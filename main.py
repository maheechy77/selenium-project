from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path="A:\projects\Python\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)

# driver.get("https://www.amazon.com")
# driver.get("https://www.g2a.com/cyberpunk-2077-gogcom-key-global-i10000156543001")
# driver.get("https://www.python.org/")
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://portal.aiub.edu/")


# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# dict = { "time":event_times[n]:"name":event_names[n] for n in len(event_times)}
# events={}
# for n in range(len(event_times)):
#     events[n]={
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
inputField1 = driver.find_element_by_id("username")
inputField1.send_keys("14-26849-2")
inputField2 = driver.find_element_by_id("password")
inputField2.send_keys("9922")

submit = driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/button')
submit.click()
# inputField = driver.find_element_by_css_selector(".form-group button")
# inputField = driver.find_element_by_css_selector("#articlecount a")
# inputField = driver.find_elements_by_css_selector(".inputField input")
# inputField = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/article/header/div/div[4]/div/div/div/div[2]/div[2]/div[1]/span[1]')
# inputField = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# print(inputField.get_attribute("class"))
# print(inputField.text)
# print(events)

driver.close()