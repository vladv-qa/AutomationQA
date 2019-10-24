from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

currency_on_the_page_xpath = '//*[@id="block-airarabia-general-hottest-flights"]/div/div/div[3]/div[1]/div/div[2]/p[1]/span[2]'


class CurrencySelector(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome('\webdrivers\chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_currency_selector(self):
        driver = self.driver
        driver.get('https://www.airarabia.com/en')
        # currency_selector_list = driver.find_element_by_class_name('currency-list')
        # li_tag_list = currency_selector_list.find_elements_by_tag_name('li')
        li_tag_list = ['AED', 'AMD', 'AZN', 'BDT', 'BHD', 'CHF', 'CNY', 'CZK', 'DKK', 'EGP', 'EUR', 'GBP', 'GEL', 'INR',
                       'IRR', 'JOD',
                       'KGS', 'KWD', 'KZT', 'LKR', 'MAD', 'MYR', 'NPR', 'OMR', 'PKR', 'QAR', 'RUB', 'SAR', 'SDG', 'SEK',
                       'TND', 'TRY',
                       'UAH', 'USD', 'YER']
        count = 1
        for item in li_tag_list:
            currency_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                "/html/body/header/div[1]/div/div[1]/div[2]/span/span")))
            currency_selector.click()
            # driver.find_element_by_xpath('/html/body/header/div[1]/div/div[1]/div[2]/span/span').click()
            driver.find_element_by_xpath(
                f'/html/body/header/div[1]/div/div[1]/div[2]/span/div/div[2]/ul/li[{count}]').click()
            time.sleep(1)
            currency_on_page = driver.find_element_by_xpath(currency_on_the_page_xpath)
            if item != currency_on_page.text:
                # print(f'Currrency selected: {item} is equal Currency on the page: {currency_on_page.text}')
                print(f'Currrency selected: {item} is NOT equal to the currency on the page: {currency_on_page.text}')
            count += 1


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
