from selenium import webdriver

driver = webdriver.Chrome("C:\\WebDriver\\bin\\chromedriver.exe")
driver.get('https://finance.yahoo.com/quote/TSLA/')

searchElem = driver.find_element_by_css_selector('#quote-summary > div.D\(ib\).W\(1\/2\).Bxz\(bb\).Pend\(12px\).Va\(t\).ie-7_D\(i\).smartphone_D\(b\).smartphone_W\(100\%\).smartphone_Pend\(0px\).smartphone_BdY.smartphone_Bdc\(\$seperatorColor\) > table > tbody > tr:nth-child(1) > td.Ta\(end\).Fw\(600\).Lh\(14px\) > span')
prevClose = searchElem.text
driver.quit()

print("The Previous Close value of TSLA is $" + prevClose)


