from selenium import webdriver

driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
driver.get('https://support.leetcode.com/hc/en-us')

searchElem = driver.find_element_by_css_selector('#query')
searchElem.send_keys('hello')
searchElem.submit()
