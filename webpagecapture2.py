from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get(r'https://www.a6cc3.com/LotteryChart?id=1&t=1523239858634')
#driver.maximize_window()
driver.switch_to.frame(0)
 #time.sleep(10)
driver.find_element_by_xpath('//*[@id="row_feature"]/span[8]/a').click()
time.sleep(5)
#js='var q=document.documentElement.scrollTop=121'
#driver.execute_script(js) 
#time.sleep(5)
#driver.save_screenshot(os.getcwd()+'\screenshot1.png')
#js='var q=document.documentElement.scrollTop=840'
#driver.execute_script(js) 
#time.sleep(5)
#print (elements.type())
#print (elements)
#time.sleep(10)
driver.save_screenshot(os.getcwd()+'\screenshot.png')
#chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = '/opt/google/chrome/chrome'
#opener = webdriver.Chrome(chrome_options=chrome_options)
