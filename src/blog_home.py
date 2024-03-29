import datetime as dt
import logging
import my_secrets
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)


def browse(browser, site: str) -> object:
	try:
		# searching this even though click elsewhere!!?!
		browser.get(site)
		WebDriverWait(browser, 1000)
		logger.info(f"Blog posts: {site}")
	except Exception as e:
		logger.error(e)


	blog_entries = browser.find_elements(By.CLASS_NAME, "entry-title")
	blog_titles = [e.text for e in blog_entries]
	print(blog_titles)
	logger.info(f"First Page Blog Count: {len(blog_titles)}")
	# 	fname = browser.find_element(By.NAME, 'firstname')
	# 	fname.clear()
	# 	fname.send_keys("SELENIUM CONSULT")
	# 	WebDriverWait(browser, 1000)
	#
	# 	lname = browser.find_element(By.NAME, 'lastname')
	# 	lname.clear()
	# 	lname.send_keys("TESTER")
	# 	WebDriverWait(browser, 1000)
	#
	# 	email = browser.find_element(By.NAME, 'email')
	# 	email.clear()
	# 	email.send_keys("TESTER@CONSULTFORM.COM")
	# 	WebDriverWait(browser, 1000)
	#
	# 	company = browser.find_element(By.NAME, 'company')
	# 	company.clear()
	# 	company.send_keys("SELENIUM CONSULT TESTING INC.")
	# 	WebDriverWait(browser, 1000)
	#
	# 	phone = browser.find_element(By.NAME, 'telephone')
	# 	phone.clear()
	# 	phone.send_keys("1234567890")
	# 	WebDriverWait(browser, 1000)
	#
	# except ElementNotSelectableException as e:
	# 	logger.error(e)
	#
	# try:
	# 	captcha = browser.find_element(By.NAME, 'captcha')
	# 	captcha.send_keys('17')
	# 	WebDriverWait(browser, 1000)
	#
	# 	browser.find_element(By.NAME, 'submit').click()
	#
	# 	# GET RESPONSE AND ADD TO CHECKS
	# 	response_element = browser.find_element(By.ID, 'msg')
	# 	response_text = response_element.text
	# 	if response_text == 'Request sent successfully':
	# 		logger.info("CONSULT EMAIL SENT")
	# 	else:
	# 		logger.error("**CONSULT EMAIL NOT SENT**")
	# except Exception as e:
	# 	logger.error(e)

	return browser