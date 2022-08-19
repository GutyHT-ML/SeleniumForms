import asyncio
import json
import sys
import time
import traceback
import unittest

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con

index = 0


class FormTest(unittest.TestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Edge()

    def test_1(self):
        file = open('info.json')
        data: dict = json.load(file)
        print("data ", data)
        settings: dict = data['settings'][index]
        url: str = settings['url']
        print("url ", url)
        driver: webdriver = webdriver.Edge()

        # Acceder a la aplicación web

        driver.get(url)

        try:
            for i in settings['items']:
                # print(i['tag'], i['xpath'], sep=' - ')
                self.evaluate_item(i, driver)
        except Exception:
            print('Error')
            # ex, val, tb = sys.exc_info()
            # traceback.print_exception(ex, val, tb)

    def evaluate_item(self, item: dict, web_driver: webdriver):
        if 'abs_xpath' in item:
            xpath = item['abs_xpath']
        else:
            if 'tag' in item:
                tag = item['tag']
            else:
                tag = '*'
            xpath = '//' + tag + item['xpath']
        wait = WebDriverWait(web_driver, 3)
        element: WebElement = wait.until(exp_con.presence_of_element_located(
            (By.XPATH, xpath)
        ))
        # print(element.tag_name, xpath)
        if item['action'] == 'text':
            try:
                element.send_keys(item['input'])
            except ElementNotInteractableException:
                self.driver.execute_script('arguments[0].value = "' + item['input'] + '"', element)
        elif item['action'] == 'check':
            if item['input']:
                try:
                    element.click()
                except ElementNotInteractableException or ElementClickInterceptedException:
                    self.driver.execute_script('arguments[0].click()', element)
        elif item['action'] == 'select':
            # print(type(item['input']))
            if type(item['input']) == int:
                Select(element).select_by_index(item['input'])
            else:
                Select(element).select_by_value(item['input'])
        print(item['input'])
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
