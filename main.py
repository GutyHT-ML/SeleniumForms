import json
import sys
import traceback

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con


def step(item: dict, web_driver: webdriver):
    if 'abs_xpath' in item:
        xpath = item['abs_xpath']
    else:
        tag = item['tag'] or '*'
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
            driver.execute_script('arguments[0].value = "'+item['input']+'"', element)
    elif item['action'] == 'check':
        if item['input']:
            try:
                element.click()
            except ElementNotInteractableException or ElementClickInterceptedException:
                driver.execute_script('arguments[0].click()', element)
    elif item['action'] == 'select':
        print(type(item['input']))
        if type(item['input']) == int:
            Select(element).select_by_index(item['input'])
        else:
            Select(element).select_by_value(item['input'])
    driver.implicitly_wait(3)


file = open('info.json')
data: dict = json.load(file)
print("data ", data)
settings: dict = data['settings'][0]
url: str = settings['url']
print("url ", url)
driver: webdriver = webdriver.Edge()

# Acceder a la aplicación web

driver.get(url)

try:
    for i in settings['items']:
        # print(i['tag'], i['xpath'], sep=' - ')
        step(i, driver)
except Exception:
    ex, val, tb = sys.exc_info()
    traceback.print_exception(ex, val, tb)
finally:
    print('Error')
    # driver.close()
