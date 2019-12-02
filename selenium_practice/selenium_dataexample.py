__author__ = 'j.zhang'
# Selenium Python documentation at: http://selenium-python.readthedocs.org/en/latest/
import collections
import time
# Import Selenium and its supporting packages: have to be installed
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

# The recursive query to chech multi pages of search results; check the main part of the code first
def checklinks(driver, element, element2):
	# Store the main URL
	mainurl = driver.current_url
	# Get all the links on the search query page; links is a Python collection of links
	# All links are stored which are in the xpath: xpath can be gathered by using Firebug in Firefox
	links = driver.find_elements_by_xpath("/html/body/")
	# For all links
	for link in links:
		# Open the link in the browser
	    driver.get(link.get_attribute("href"))
		# If there is an element on the page in the given xpath
	    if driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/div/"):
			# Print the following elements; and the text contained in the container of the specified xpath
	    	print element,element2,link.text,driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/").text
	    else:
			# else print the elements and a 0
		print element,element2,link.text,'0'
	# Go back to the search result page	after all links of the search result page have been parsed
	driver.get(mainurl)
	# Get the <a href=...>Next ></a> button on the pager of the search result page
	nextlink = driver.find_element_by_link_text('Next >')
	# If nextlink is given - if we are not on the last page
	if nextlink:
		# Open the next page
		driver.get(nextlink.get_attribute("href"))
		# Recursively check the links by recalling the above method
		checklinks(driver, element, element2)

# Dropdown values for the forms
dropdownelements = ['Selection1', 'Selection2']
dropdownelements2  = ['Selection10', 'Selection20']

# Open Firefox
driver = webdriver.Firefox()
# Open the webpage
driver.get("http://www.tobecheckedpage/")
# Find the form element named login, e.g. in the HTML <input name="login" type="text" /> and link it to username variable
username = driver.find_element_by_name('login')
# Add your user name to the login box
username.send_keys("myloginid")
# Find the form element named password
password = driver.find_element_by_name('password')
# Add your password to the login box
password.send_keys("password")
# Click on the button named signin
driver.find_element_by_name('signin').click()
# Find the link appearing as Link on the page and click on it, e.g. in the HTML <a href="continue.html">Link</a>
driver.find_element_by_link_text('Link').click()

# For all dropdownelements
for element in dropdownelements:
	# For all dropdownelements2
	for element2 in dropdownelements2:
		# Open a page
		driver.get("http://www.tobecheckedpage/page")
		# Find element by ID, e.g. in the HTML <form id="code">
		form = driver.find_element_by_id('code')
		# Form is a dropdown, parse through all the chosable options
		for option in form.find_elements_by_tag_name('option'):
			#If the currently selected option matches element
		    if option.text == element:
				#Then click on the element
		    	option.click()
		# Find an other form input element, having an id 'keywords'
		keywordsform = driver.find_element_by_id('keywords')
		# May be needed if Ajax is on the page and form changes;
		# for more complex waits, e.g. wait for an element to show up, see http://selenium-python.readthedocs.org/en/latest/waits.html
		time.sleep(1)
		# Add element2 to the page
		keywordsform.send_keys(element2)
		# Click on button, that have a class called submit, e.g. in the HTML <form class="submit">
		driver.find_element_by_class_name('submit').click()
		# Call recursive checker - as form has been sent, we have the results of the query
		checklinks(driver, country, job)
# Close the browser
driver.close()