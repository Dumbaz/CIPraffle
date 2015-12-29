from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


questionpage = "https://secure.tibia.com/community/?subtopic=feedbackform&page=show&questionaireid=693"


accountName = 	"NAMEHERE"
password	=	"PASSWORDHERE"


def openwebsite(questionpage, accountName, password):

	# Load the website
	driver = webdriver.Firefox()
	driver.get(questionpage)
	
	#Wait a sec
	assert 'Tibia' in driver.title
	# Safety sleep
	time.sleep(2)
	
	# Click the login link
	elem = driver.find_element_by_link_text('Log in')
	elem.click()

	# Actually log in
	elem = driver.find_element_by_name("loginname")
	elem.send_keys(accountName + Keys.TAB + password + Keys.RETURN)

	# Wait a bit
	time.sleep(3)
	assert 'Community' in driver.title
	
	# Click the Radio Button
	elem = driver.find_element_by_id("RADIO-786_0_1-6689-TEXT").click()
	
	# Write a witty text
	elem = driver.find_element_by_id("RADIO-786_0_1-6689-TEXT-INPUT").click()
	elem = driver.find_element_by_id("RADIO-786_0_1-6689-TEXT-INPUT")
	elem.send_keys("Thanks Santa")

	# Click on Submit
	submitbutton = driver.find_element_by_name("Submit")
	submitbutton.click()

	# Close the Firefox instance
	driver.quit()


openwebsite(questionpage, accountName, password)