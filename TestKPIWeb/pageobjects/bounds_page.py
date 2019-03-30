from pageobjects.base_page import BasePage
from webelements.bounds_web_elements import BoundsWebElements


class BoundsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_data_labels_locator_xpath = \
            BoundsWebElements.locators['input_data_labels_locator_xpath']
        self.input_data_selectors_locator_xpath = \
            BoundsWebElements.locators['input_data_selectors_locator_xpath']
        self.input_data_texts_locator_xpath = \
            BoundsWebElements.locators['input_data_texts_locator_xpath']
        self.input_data_buttons_locator_xpath = \
            BoundsWebElements.locators['input_data_buttons_locator_xpath']

    def get_all_label_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_labels_locator_xpath)

    def get_all_selector_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_selectors_locator_xpath)

    def get_all_text_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_texts_locator_xpath)

    def get_all_button_elements(self):
        return self.driver.find_elements_by_xpath(self.input_data_buttons_locator_xpath)

    def input_data_label_testsuite(self):
        return self.get_all_label_elements()[0]

    def input_data_selector_testsuite(self):
        return self.get_all_selector_elements()[0]

    def input_data_label_testcase(self):
        return self.get_all_label_elements()[1]

    def input_data_selector_testcase(self):
        return self.get_all_selector_elements()[1]

    def input_data_label_kpi(self):
        return self.get_all_label_elements()[2]

    def input_data_selector_kpi(self):
        return self.get_all_selector_elements()[2]

    def input_data_text_upperbound(self):
        return self.get_all_text_elements()[0]

    def input_data_btn_upper_infinity(self):
        return self.get_all_button_elements()[2]

    def input_data_text_lowerbound(self):
        return self.get_all_text_elements()[1]

    def input_data_btn_lower_infinity(self):
        return self.get_all_button_elements()[3]

    def action_update_thresholds(self):
        return self.get_all_button_elements()[4]

    # def _validate_page(self, driver):
    #     super()._validate_page(driver)
    #     self.assertTrue(self.__input_data_label_testsuite().is_enabled())
    #     self.assertTrue(self.__input_data_selector_testsuite().is_enabled())
    #     self.assertTrue(self.__input_data_label_testcase().is_enabled())
    #     self.assertTrue(self.__input_data_selector_testcase().is_enabled())
    #     self.assertTrue(self.__input_data_label_kpi().is_enabled())
    #     self.assertTrue(self.__input_data_selector_kpi().is_enabled())
    #     self.assertTrue(self.__input_data_text_upperbound().is_enabled())
    #     self.assertTrue(self.__input_data_btn_upper_infinity().is_enabled())
    #     self.assertTrue(self.__input_data_text_lowerbound().is_enabled())
    #     self.assertTrue(self.__input_data_btn_lower_infinity().is_enabled())
    #     self.assertTrue(self.__action_update_thresholds().is_enabled())
