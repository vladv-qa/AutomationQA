from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains



class HeaderUseCases(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome('\webdrivers\chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_click_logo(self):
        self.driver.get('https://www.airarabia.com/en/book-flight')
        logo = self.driver.find_element_by_class_name('aa-logo')
        logo.click()
        time.sleep(4)
        home_url = self.driver.current_url
        assert home_url == "https://www.airarabia.com/en"

    @classmethod
    def test_change_language(self):
        self.driver.get('https://www.airarabia.com/en')
        language_selector = self.driver.find_element_by_class_name('selected-language')
        language_selector.click()
        language_list_item = self.driver.find_element_by_xpath('//*[@id="user_languages"]/div/span/div/div[2]/ul/li[6]')
        language_list_item.click()
        time.sleep(4)
        url_de = self.driver.current_url
        assert url_de == 'https://www.airarabia.com/de'

    @classmethod
    def test_change_currency(self):
        self.driver.get('https://www.airarabia.com/en')
        currency = self.driver.find_element_by_class_name('selected')
        currency.click()
        new_currency = self.driver.find_element_by_xpath(
            '/html/body/header/div[1]/div/div[1]/div[2]/span/div/div[2]/ul/li[12] ')
        new_currency.click()
        time.sleep(2)
        currency_on_page = self.driver.find_element_by_xpath(
            '//*[@id="block-airarabia-general-hottest-flights"]/div/div/div[3]/div[1]/div/div[2]/p[1]/span[2]')
        assert currency_on_page.text == "GBP"

    @classmethod
    def test_change_location(self):
        self.driver.get('https://www.airarabia.com/en')
        location_selector = self.driver.find_element_by_name('flying-from')
        location_selector.click()
        time.sleep(2)
        choose_city = self.driver.find_element_by_link_text('Bangladesh')
        choose_city.click()
        time.sleep(2)
        choose_airport = self.driver.find_element_by_xpath(
            '/html/body/header/div[1]/div/div[1]/div[1]/div[1]/div[4]/ul/li[6]/a/span[1]')
        choose_airport.click()
        time.sleep(2)
        check = self.driver.find_element_by_xpath(
            '//*[@id="block-airarabia-general-hottest-flights"]/div/div/div[3]/div[1]/div/div[2]/h3/span[1]')
        assert check.text == "Chattogram to"

    @classmethod
    def test_menu_hover_state(self):
        self.driver.get('https://www.airarabia.com/en')
        time.sleep(2)
        element_to_hover = self.driver.find_element_by_class_name('attached-block')
        sub_menu_hover = self.driver.find_element_by_xpath('//*[@id="block-block-16"]/div/ul[1]/li[2]/a')
        hover = ActionChains(self.driver)
        hover.move_to_element(element_to_hover).move_to_element(sub_menu_hover).click()
        hover.perform()
        time.sleep(2)
        home_url = self.driver.current_url
        assert home_url == "https://www.airarabia.com/en/book-flight"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Vladislav/PycharmProjects/AA_Use_Cases/reports'))
