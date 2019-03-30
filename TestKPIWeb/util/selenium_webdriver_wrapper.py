from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from singleton_decorator import singleton

CHROMEDRIVER = '../../chromedriver_web/chromedriver'


@singleton
class WebDriver(object):

	def __init__(self, url, is_headless):
		super().__init__()
		self.__option = Options()
		self.__option.add_argument("--ignore-certificate-errors")
		self.__option.add_argument("--test-type")
		if is_headless:
			self.__option.add_argument("--headless")
		self.__driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=self.__option)
		self.__driver.get(url)
		self.__driver.implicitly_wait(1)

	def get_driver(self):
		return self.__driver

	def set_driver(self, driver):
		self.__driver = driver
