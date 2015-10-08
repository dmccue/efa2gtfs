#!/usr/bin/python

import time, json, os
from selenium import webdriver

def print_urls():
    elems = driver.find_elements_by_xpath('//td/a[contains(@class, "pdf-ico")]')
    for elem in elems:
        links.append(elem.get_attribute('href'))


links = []
driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds

driver.get("https://www.translink.co.uk/Services/Metro-Service-Page/Timetables/")
print_urls()
elem_next = driver.find_element_by_xpath('//input[contains(@title, "Next Page")]')

while elem_next and not elem_next.get_attribute('onclick'):
    elem_next.click()
    time.sleep(5)
    print_urls()
    elem_next = driver.find_element_by_xpath('//input[contains(@title, "Next Page")]')

driver.close()

if not os.path.exists('tmp'):
    os.makedirs('tmp')
with open('tmp/pdf_links.json', 'w') as outfile:
    json.dump(links, outfile)
