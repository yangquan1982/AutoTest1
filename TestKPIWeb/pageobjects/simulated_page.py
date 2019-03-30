from pageobjects.base_page import BasePage
from webelements.simulated_web_elements import SimulatedWebElements


class SimulatedPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)
		self.input_data_label_branch_locator_xpath = SimulatedWebElements.locators['input_data_label_branch_locator_xpath']
		self.input_data_text_branch_locator_xpath = SimulatedWebElements.locators['input_data_text_branch_locator_xpath']
		self.input_data_label_test_suite_locator_xpath = SimulatedWebElements.locators['input_data_label_test_suite_locator_xpath']
		self.input_data_selector_test_suite_locator_xpath = SimulatedWebElements.locators['input_data_selector_test_suite_locator_xpath']
		self.input_data_label_test_case_locator_xpath = SimulatedWebElements.locators['input_data_label_test_case_locator_xpath']
		self.input_data_selector_test_case_locator_xpath = SimulatedWebElements.locators['input_data_selector_test_case_locator_xpath']
		self.input_data_label_kpi_locator_xpath = SimulatedWebElements.locators['input_data_label_kpi_locator_xpath']
		self.input_data_selector_kpi_locator_xpath = SimulatedWebElements.locators['input_data_selector_kpi_locator_xpath']
		self.output_data_label_parameters_locator_xpath = SimulatedWebElements.locators['output_data_label_parameters_locator_xpath']
		self.output_data_chart_locator_xpath = SimulatedWebElements.locators['output_data_chart_locator_xpath']
		self.input_data_react_branch_devel_locator_xpath = SimulatedWebElements.locators['input_data_react_branch_devel_locator_xpath']
		self.input_data_select_test_suites_locator_xpath = SimulatedWebElements.locators['input_data_select_test_suites_locator_xpath']
		self.input_data_select_test_cases_locator_xpath = SimulatedWebElements.locators['input_data_select_test_cases_locator_xpath']
		self.input_data_kpis_locator_xpath = SimulatedWebElements.locators['input_data_kpis_locator_xpath']
		self.output_data_parameters_locator_xpath = SimulatedWebElements.locators['output_data_parameters_locator_xpath']
		self.input_data_select_values_locator_xpath = SimulatedWebElements.locators['input_data_select_values_locator_xpath']

	def input_data_select_values(self):
		return self.driver.find_elements_by_xpath(self.input_data_select_values_locator_xpath)

	def output_data_parameters(self):
		return self.driver.find_elements_by_xpath(self.output_data_parameters_locator_xpath)

	def input_data_kpis(self):
		return self.driver.find_elements_by_xpath(self.input_data_kpis_locator_xpath)

	def input_data_select_test_suites(self):
		return self.driver.find_elements_by_xpath(self.input_data_select_test_suites_locator_xpath)

	def input_data_select_test_cases(self):
		return self.driver.find_elements_by_xpath(self.input_data_select_test_cases_locator_xpath)

	def input_data_react_branch_devel(self):
		return self.driver.find_element_by_xpath(self.input_data_react_branch_devel_locator_xpath)

	def input_data_label_branch(self):
		return self.driver.find_element_by_xpath(self.input_data_label_branch_locator_xpath)

	def input_data_text_branch(self):
		return self.driver.find_element_by_xpath(self.input_data_text_branch_locator_xpath)

	def input_data_text_branch_value(self):
		return self.input_data_text_branch().get_attribute("value")

	def input_data_label_test_suite(self):
		return self.driver.find_element_by_xpath(self.input_data_label_test_suite_locator_xpath)

	def input_data_selector_test_suite(self):
		return self.driver.find_element_by_xpath(self.input_data_selector_test_suite_locator_xpath)

	def input_data_test_suite_value(self):
		return self.input_data_select_values()[0].text

	def input_data_label_test_case(self):
		return self.driver.find_element_by_xpath(self.input_data_label_test_case_locator_xpath)

	def input_data_selector_test_case(self):
		return self.driver.find_element_by_xpath(self.input_data_selector_test_case_locator_xpath)

	def input_data_test_case_value(self):
		return self.input_data_select_values()[1].text

	def input_data_label_kpi(self):
		return self.driver.find_element_by_xpath(self.input_data_label_kpi_locator_xpath)

	def input_data_selector_kpi(self):
		return self.driver.find_element_by_xpath(self.input_data_selector_kpi_locator_xpath)

	def input_data_kpi_value(self):
		return self.input_data_select_values()[2].text

	def output_data_label_parameters(self):
		return self.driver.find_element_by_xpath(self.output_data_label_parameters_locator_xpath)

	def output_data_chart(self):
		return self.driver.find_element_by_xpath(self.output_data_chart_locator_xpath)

	# def input_data_react_branch_value_list(self):
	# 	branch_item_value_list = []
	# 	react_branch_list = self.input_data_react_branch_list()
	# 	for branch_item in react_branch_list:
	# 		branch_item_list = branch_item.find_elements_by_xpath(self.input_data_react_branch_item_list)
	# 		branch_item_value = ""
	# 		for branch_item_list_item in branch_item_list:
	# 			branch_item_value += branch_item_list_item.text
	# 		branch_item_value_list.append(branch_item_value)
	# 	return branch_item_value_list
