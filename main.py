import json
import sys
import traceback

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

data = {
    "settings": [{
        "url": "https://alexlozano.limesurvey.net/452258",
        "items": [
            {
                "tag": "button",
                "action": "check",
                "input": True,
                "xpath": "[@id=\"ls-button-submit\"][@type=\"submit\"]"
            },
            {
                "tag": "textarea",
                "action": "text",
                "input": "Hola",
                "xpath": "[@id=\"answer452258X1X1\"]"
            },
            {
                "tag": "select",
                "action": "select",
                "input": 1,
                "xpath": "[@id=\"answer452258X1X2\"]"
            },
            {
                "tag": "input",
                "action": "check",
                "type": "checkbox",
                "input": True,
                "xpath": "[@id=\"answer452258X1X3SQ001\"]"
            },
            {
                "tag": "input",
                "action": "check",
                "type": "radio",
                "input": True,
                "xpath": ""
            },
            {
                "tag": "input",
                "action": "text",
                "type": "text",
                "input": "Mundo",
                "xpath": "[@id=\"answer452258X1X7SQ001\"]"
            }
        ]
    },
        {
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSe-K-BXchYBdcjPYvZHvEzAW69Ajd24HzVDGIWqsb101MEsUQ"
                   "/viewform?usp=sf_link",
            "items": [
                {
                    "tag": "input",
                    "action": "text",
                    "type": "text",
                    "input": "Guty",
                    "abs_xpath": "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div["
                                 "1]/input "
                },
                {
                    "tag": "select",
                    "action": "select",
                    "input": "Un vato loco",
                    "abs_xpath": "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div["
                                 "2]/textarea "
                },
                {
                    "action": "check",
                    "input": True,
                    "type": "radio",
                    "abs_xpath": "//*[@id=\"i13\"]/div[3]/div"
                },
                {
                    "action": "check",
                    "input": True,
                    "type": "radio",
                    "abs_xpath": "//*[@id=\"i16\"]/div[3]/div"
                },
                {
                    "action": "check",
                    "input": True,
                    "type": "checkbox",
                    "abs_xpath": "//*[@id=\"i24\"]/div[2]"
                },
                {
                    "action": "check",
                    "input": True,
                    "type": "checkbox",
                    "abs_xpath": "//*[@id=\"i27\"]/div[2]"
                },
                {
                    "action": "check",
                    "input": True,
                    "type": "checkbox",
                    "abs_xpath": "//*[@id=\"i30\"]/div[2]"
                },
                {
                    "tag": "input",
                    "action": "check",
                    "input": True,
                    "type": "text",
                    "abs_xpath": "//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div["
                                 "1]/input "
                },
                {
                    "action": "check",
                    "input": True,
                    "abs_xpath": "//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span"
                }
            ]
        },
        {
            "url": "https://alexlozano.limesurvey.net/452258",
            "items": [
                {
                    "tag": "textarea",
                    "action": "textarea",
                    "input": "Hola",
                    "xpath": "[@id=\"answer452258X1X1\"]"
                },
                {
                    "tag": "select",
                    "action": "select",
                    "input": "1",
                    "xpath": "[@id=\"answer452258X1X2\"]"
                },
                {
                    "tag": "input",
                    "action": "checkbox",
                    "input": True,
                    "xpath": "[@id=\"answer452258X1X3SQ001\"]"
                },
                {
                    "tag": "input",
                    "action": "radio",
                    "input": True,
                    "xpath": ""
                },
                {
                    "tag": "input",
                    "action": "text",
                    "input": "Mundo",
                    "xpath": "[@id=\"answer452258X1X7SQ001\"]"
                }
            ]
        }
    ]
}


def step(item, web_driver: webdriver):
    if item['xpath'] is None:
        xpath = item['abs_xpath']
    else:
        tag = item['tag'] or '*'
        xpath = '//' + tag + item['xpath']
    element: WebElement = web_driver.find_element(By.XPATH, xpath)
    # print(element.tag_name, xpath)
    if item['action'] == 'text':
        element.send_keys(item['input'])
    elif item['action'] == 'check':
        if item['input']:
            element.click()
    elif item['action'] == 'select':
        print(type(item['input']))
        if type(item['input']) == int:
            Select(element).select_by_index(item['input'])
        else:
            Select(element).select_by_value(item['input'])
    driver.implicitly_wait(3)


print("data ", data)
settings = data['settings'][1]
url = settings['url']
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

# # Localizar cuadro de texto
# button = driver.find_element(By.ID, "ls-button-submit")
# button.click()
# search_field = driver.find_element(By.ID, "answer452258X1X1")
# search_field.send_keys("Ayuda")
# # search_field.clear()
#
# # Indicar y confirmar término de búsqueda
# #
# search_field.send_keys("Minions")
# # search_field.submit()
#
# select = Select(driver.find_element(By.ID, "answer452258X1X2"))
# select.select_by_value("AO02")
# # select.select_by_value("Si")
#
# '''checkbox = driver.find_element(By.NAME, "452258X1X3SQ001")
# checkbox.click()'''
#
# radio1 = driver.find_element(By.ID, "answer452258X1X5AO01")
# radio1.click()
# # Obtener la lista de resultados de la búsqueda y mostrarla
# # mediante el método find_elements_by_class_name
# # lists= driver.find_elements_by_class_name("gb_d")
# # lists.click()
#
# search_field2 = driver.find_element(By.ID, "answer452258X1X7SQ001")
# search_field2.send_keys("Efectivamente todo esta funcionando como deberia")
#
# # inicio = driver.find_element(By.ID, "logo-icon")
# # inicio.click()
#
#
# radio2 = driver.find_element(By.ID, "answer452258X1X9AO02")
# radio2.click()
# # inicio2 = driver.find_element(By.ID, "search-icon-legacy")
# # inicio2.click()
# # Pasar por todos los elementos y reproducir el texto individual
#
# '''i=0
# for listitem in lists:
#   print (listitem.get_attribute("innerHTML"))
#   i=i+1
#   if(i>10):
#     break'''
#
# # Cerrar la ventana del navegador
# # driver.implicitly_wait(30)
# # driver.quit()
