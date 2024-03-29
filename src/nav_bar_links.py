import datetime as dt
import logging
import my_secrets
import selenium.common.exceptions
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ERROR_URL
from typing import Dict

now: dt = dt.date.today()
todays_date: str = now.strftime('%D').replace('/', '-')

logger = logging.getLogger(__name__)



def browse(browser,  nav_menu_links: Dict , site: str,) -> object:
	try:
		browser.get(site)
		WebDriverWait(browser, 1000)
		logger.info(f"Navigating menu bar links")
	except ERROR_URL as e:
		logger.error(e)

	for title, href in nav_menu_links.items():
		print(href)
		try:
			browser.get(f"{site}/{href}")
			time.sleep(10)

		except ERROR_URL as e:
			logger.exception(e)

	return browser



	# navbar_items = browser.find_elements(By.TAG_NAME, 'a')
	# print(navbar_items)
	# for item in navbar_items:
	# 	print(item)
	# 	print(item.title)
	# WebDriverWait(browser, 1000)

	# browser.find_element(By.LINK_TEXT, "BLOG").click()
	# WebDriverWait(browser, 1000)
	# browser.find_element(By.LINK_TEXT, "HOA").click()
	# WebDriverWait(browser, 1000)
	#
	# logger.info("FINISHED SELENIUM WEBSITE NAVBAR TESTING")
	#
	# browser.find_element(By.LINK_TEXT, "WHY TASCS?").click()
	# WebDriverWait(browser, 1000)
	#
	# browser.find_element(By.LINK_TEXT, "SOLUTIONS").click()
	# WebDriverWait(browser, 1000)

	# browser.close()
