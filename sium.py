from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import time
# time is used to wait for the page to load to access its contents 

# Creating a driver to access the browser
chromedriver = '/chromerdriver'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.facebook.com')


ls = []
with open("file.txt",'r') as file :
	for line in file :
		ls.append(line.strip())
# strip() method is used to remove the /n at the end of each line

# we start by just taking one acc detail for now
# You can later try to expand it for number of acccounts

num_friends = 0
#finding required elements using querySelector
if len(ls) == 2 :
	#logging in
	browser.find_element_by_id('email').send_keys(ls[0])
	browser.find_element_by_id('pass').send_keys(ls[1])
	
	#navigation
	browser.find_element_by_id('loginbutton').click()
	browser.find_element_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a').click()


	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="u_fetchstream_2_a"]/li[3]/a').click()
	


