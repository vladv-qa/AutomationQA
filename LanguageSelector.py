from selenium import webdriver
import time
from Screenshot import Screenshot_Clipping
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome('\webdrivers\chromedriver')
driver.implicitly_wait(10)
driver.maximize_window()

ac = ActionChains(driver=driver)

driver.get('https://www.airarabia.com/en')
driver.find_element_by_class_name('agree-button').click()

#  get language list length
ul = driver.find_element_by_class_name('text-left.language-list')
list = ul.find_elements_by_tag_name('li')
language_list_length = len(list)

for count in range(1, language_list_length + 1):
    driver.find_element_by_xpath('//*[@id="user_languages"]/div/span').click()
    driver.find_element_by_xpath(f'//*[@id="user_languages"]/div/span/div/div[2]/ul/li[{count}]').click()
    time.sleep(1)
    driver.execute_script("document.getElementById('search_tabs').style.position = 'static';")
    name = driver.find_element_by_xpath(f'//*[@id="user_languages"]/div/span/div/div[2]/ul/li[{count}]')
    lan_name = name.get_attribute('data-title')
    full_screen = ob.full_Screenshot(driver=driver, save_path='C:/Users/Vladislav/PycharmProjects/AA_Use_Cases/images',
                                     image_name=f'{lan_name}.png')
    ac.send_keys(Keys.HOME)
    ac.perform()
    time.sleep(1)

driver.close()

#
# driver.execute_script("document.getElementById('search_tabs').style.position = 'unset';")
# time.sleep(1)
