"""
Input Setter for Simulated Page
"""
import time
from selenium.webdriver.common.action_chains import ActionChains
from util.browser_refresh import BrowserRefresher

WAITING_SEC = 1


class SimulatedPageInputSetter(object):

	def __init__(self, simulated_page, driver, browser_refresher):
		self.simulated_page = simulated_page
		self.driver = driver
		self.browser_refresher = browser_refresher

	def __set_branch(self, branch, is_set):
		branch_text = self.simulated_page.input_data_text_branch()
		if is_set:
			present_branch = self.simulated_page.input_data_text_branch_value()
			if branch == present_branch:
				return
			self.browser_refresher.refresh_browser()
			branch_text = self.simulated_page.input_data_text_branch()
			branch_text.send_keys(branch)
		else:
			branch_text.send_keys(branch)
		time.sleep(WAITING_SEC)
		branch_react_devel = self.simulated_page.input_data_react_branch_devel()
		ActionChains(self.driver).move_to_element(branch_react_devel).click().perform()
		time.sleep(WAITING_SEC)

	def __set_test_suite(self, index, test_suite, is_set):
		if is_set:
			present_test_suite = self.simulated_page.input_data_test_suite_value()
			if present_test_suite == test_suite:
				return
			test_suite_selector = self.simulated_page.input_data_select_values()[0]
		else:
			test_suite_selector = self.simulated_page.input_data_selector_test_suite()
		ActionChains(self.driver).move_to_element(test_suite_selector).click().perform()
		time.sleep(WAITING_SEC)
		test_suit_item = self.simulated_page.input_data_select_test_suites()[index]
		ActionChains(self.driver).move_to_element(test_suit_item).click().perform()
		time.sleep(WAITING_SEC)

	def __set_test_case(self, index, test_case, is_set, is_test_suite_changed):
		if is_set and not is_test_suite_changed:
			present_test_case = self.simulated_page.input_data_test_case_value()
			if present_test_case == test_case:
				return
			test_case_selector = self.simulated_page.input_data_select_values()[1]
		else:
			test_case_selector = self.simulated_page.input_data_selector_test_case()
		ActionChains(self.driver).move_to_element(test_case_selector).click().perform()
		time.sleep(WAITING_SEC)
		test_case_item = self.simulated_page.input_data_select_test_cases()[index]
		ActionChains(self.driver).move_to_element(test_case_item).click().perform()
		time.sleep(WAITING_SEC)

	def __set_kpi(self, index, kpi, is_set):
		if is_set:
			present_kpi = self.simulated_page.input_data_kpi_value()
			if present_kpi == kpi:
				return
			kpi_selector = self.simulated_page.input_data_select_values()[2]
		else:
			kpi_selector = self.simulated_page.input_data_selector_kpi()
		ActionChains(self.driver).move_to_element(kpi_selector).click().perform()
		time.sleep(WAITING_SEC)
		kpi_item = self.simulated_page.input_data_kpis()[index]
		ActionChains(self.driver).move_to_element(kpi_item).click().perform()
		time.sleep(WAITING_SEC)

	def set_input_data(self, input_data_list, is_set, is_test_suite_changed):
		self.__set_branch(input_data_list[0], is_set)
		self.__set_test_suite(input_data_list[1], input_data_list[2], is_set)
		self.__set_test_case(input_data_list[3], input_data_list[4], is_set, is_test_suite_changed)
		self.__set_kpi(input_data_list[5], input_data_list[6], is_set)
