#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import re
import pprint

driver = webdriver.Chrome(r"C:/chromedriver.exe")
driver.get("https://www.amazon.com")
    
elems = driver.find_elements_by_css_selector("div#nav-flyout-shopAll div a.nav-item")

categories = {}
for item in elems:
    name = item.find_element_by_css_selector("span").get_attribute('textContent')
    link = item.get_attribute('href')
    categories[name] = link

for key in categories.keys():
    print(key)


print("Cat_name = ")
#cat_name = input()
cat_name = 'Software'
print("Search(%s)......." %cat_name)

prods = []
driver.get(categories[cat_name])
page = 1
while True:
    driver.get(categories[cat_name]+'&page=%s'%page)
    elems = driver.find_elements_by_css_selector("ul.s-result-list li.s-result-item")
    if not elems:
        break


    for item in elems:
        link = item.find_element_by_css_selector("a.a-link-normal.s-access-detail-page").get_attribute('href')
        name = item.find_element_by_css_selector("h2").get_attribute('textContent')
        try:
            price0 = item.find_element_by_css_selector("span.sx-price-whole").get_attribute('textContent')+ '.' + item.find_element_by_css_selector("sup.sx-price-fractional").get_attribute('textContent')
        except:
            price0 = "-"
        try:
            price1 = item.find_element_by_css_selector(".a-text-strike").get_attribute('textContent')
            if(price1==""):
                price1="-"
        except:
            price1 = "-"

        try:
            instock = item.find_element_by_css_selector(".a-color-price").get_attribute('textContent')
            instock = re.search("Only (.+?) left in stock - order soon.", instock).group(1)
        except:
            instock = "-"

        prods.append({'name':name, 'link':link, 'price0':price0, 'price1':price1, 'instock':instock})
    page+=1 

driver.close()
