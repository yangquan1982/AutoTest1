from pageobjects.base_page import BasePage
from webelements.realworld_web_elements import RealworldWebElements


class RealWorldPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_data_labels_locator_xpath = \
            RealworldWebElements.locators['input_data_labels_locator_xpath']
        self.input_data_selectors_locator_xpath = \
            RealworldWebElements.locators['input_data_selectors_locator_xpath']
        self.input_data_start_date_locator_xpath = \
            RealworldWebElements.locators['input_data_start_date_locator_xpath']
        self.input_data_end_date_locator_xpath = \
            RealworldWebElements.locators['input_data_end_date_locator_xpath']
        self.output_data_chart_locator_xpath = \
            RealworldWebElements.locators['output_data_chart_locator_xpath']

    def input_data_label_car(self):
        return self.get_all_label_elements()[0]

    def input_data_selector_car(self):
        return self.get_all_selector_elements()[0]

    def input_data_label_kpi(self):
        return self.get_all_label_elements()[1]

    def input_data_selector_kpi(self):
        return self.get_all_selector_elements()[1]

    def input_data_label_daterange(self):
        return self.get_all_label_elements()[2]

    def input_data_start_date(self):
        return self.driver.find_element_by_xpath(self.input_data_start_date_locator_xpath)

    def input_data_end_date(self):
        return self.driver.find_element_by_xpath(self.input_data_end_date_locator_xpath)

    def output_data_chart(self):
        return self.driver.find_element_by_xpath(self.output_data_chart_locator_xpath)

    def get_all_label_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_labels_locator_xpath)

    def get_all_selector_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_selectors_locator_xpath)
    # def _validate_page(self, driver):
    #     super()._validate_page(driver)
    #     self.assertTrue(self.__input_data_label_car().is_enabled())
    #     self.assertTrue(self.__input_data_selector_car().is_enabled())
    #     self.assertTrue(self.__input_data_label_kpi().is_enabled())
    #     self.assertTrue(self.__input_data_selector_kpi().is_enabled())
    #     self.assertTrue(self.__input_data_label_daterange().is_enabled())
    #     self.assertTrue(self.__input_data_start_date().is_enabled())
    #     self.assertTrue(self.__input_data_end_date().is_enabled())
    #     self.assertTrue(self.__output_data_chart().is_enabled())
