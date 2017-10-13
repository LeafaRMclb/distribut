from selenium import webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get('http://statistics.cbn.gov.ng/cbn-onlinestats/DataBrowser.aspx')
input = browser.find_element_by_css_selector("#MainContent_ddlCategories")
input.click()
input.send_keys("Financial Statistics")
input.click()
s1 = browser.find_element_by_css_selector("#MainContent_dgLinks_lnkSubCategories_0")
s1.click()
s2 = browser.find_element_by_css_selector("#MainContent_ddlFrequency")
s2.click()
s2.send_keys("Monthly")
s2.click()
s3 = browser.find_element_by_css_selector("#MainContent_btnContinue")
s3.click()
s4 = browser.find_element_by_css_selector("#MainContent_dgTableSelection_chkApply_9")
s4.click()
s5 = browser.find_element_by_css_selector("#chkAllMonths")
s5.click()
s6 = browser.find_element_by_css_selector("#MainContent_ddlMonthStartYear")
s6.click()
s6.send_keys("2015")
s7 = browser.find_element_by_css_selector("#MainContent_ddlMonthEndYear")
s7.click()
s7.send_keys("2017")
s8 = browser.find_element_by_css_selector("#MainContent_btnProcessMonthlyData")
s8.click()






