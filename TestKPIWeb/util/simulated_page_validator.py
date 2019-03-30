"""
Validator for Simulated Page
"""
import unittest


class SimulatedPageValidator(unittest.TestCase):

    refresher = None
    base_page = None
    simulated_page = None

    def set_refresher(self, refresher):
        self.refresher = refresher

    def get_refresher(self):
        return self.refresher

    def set_base_page(self, base_page):
        self.base_page = base_page

    def get_base_page(self):
        return self.base_page

    def __get_input_data_values(self):
        input_list = list()
        input_list.append(self.simulated_page.input_data_text_branch().get_attribute("value"))
        for i in range(3):
            input_list.append(self.simulated_page.input_data_select_values()[i].text)
        return input_list

    def __get_output_elements(self):
        output_list = list()
        parameter_elements = self.simulated_page.output_data_parameters()
        for elem in parameter_elements:
            output_list.append(elem)
        output_list.append(self.simulated_page.output_data_chart())
        return output_list

    def set_simulated_page(self, simulated_page):
        self.simulated_page = simulated_page

    def get_simulated_page(self):
        return self.simulated_page

    def validate_input(self, second_list):
        """Assert each element in first_list is equal to the element with the same index in second_list"""
        first_list = self.__get_input_data_values()
        self.assertTrue(second_list[0].lower() in first_list[0].lower())
        first_sub_list = first_list[1:]
        second_sub_list = second_list[1:]
        first_second_sub_dict = zip(first_sub_list, second_sub_list)
        for first, second in first_second_sub_dict:
            self.assertEqual(first, second)

    def validate_output(self):
        """Assert each element in output_list is enabled"""
        for item in self.__get_output_elements():
            self.assertTrue(item.is_enabled())

    def validate_base_page_ini_elements_enabled(self):
        # Validate base page elements
        self.assertTrue(self.base_page.ele_top_bar().is_enabled())
        self.assertTrue(self.base_page.ele_nio_logo().is_enabled())
        self.assertTrue(self.base_page.ele_top_left_btn().is_enabled())
        self.assertTrue(self.base_page.ele_left_nav_bar().is_enabled())
        self.assertTrue(self.base_page.ele_left_nav_simulated_btn().is_enabled())
        self.assertTrue(self.base_page.ele_left_nav_realworld_btn().is_enabled())
        self.assertTrue(self.base_page.ele_left_nav_bounds_btn().is_enabled())
        self.assertTrue(self.base_page.ele_main_pad().is_enabled())
        self.assertTrue(self.base_page.get_app_title() == self.base_page.app_title)

    def validate_simulated_page_specific_ini_elements_enabled(self):
        # Validate simulated page specific elements
        self.assertTrue(self.simulated_page.input_data_label_branch().is_enabled())
        self.assertTrue(self.simulated_page.input_data_text_branch().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_test_suite().is_enabled())
        self.assertTrue(self.simulated_page.input_data_selector_test_suite().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_test_case().is_enabled())
        self.assertTrue(self.simulated_page.input_data_selector_test_case().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_kpi().is_enabled())
        self.assertTrue(self.simulated_page.input_data_selector_kpi().is_enabled())
        self.assertTrue(self.simulated_page.output_data_label_parameters().is_enabled())
        self.assertTrue(self.simulated_page.output_data_chart().is_enabled())

    def validate_simulated_page_specific_after_selection_elements_enabled(self):
        # Validate simulated page specific elements after selection
        self.assertTrue(self.simulated_page.input_data_label_branch().is_enabled())
        self.assertTrue(self.simulated_page.input_data_text_branch().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_test_suite().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_test_case().is_enabled())
        self.assertTrue(self.simulated_page.input_data_label_kpi().is_enabled())
        self.assertTrue(self.simulated_page.output_data_label_parameters().is_enabled())
        self.assertTrue(self.simulated_page.output_data_chart().is_enabled())
        self.assertTrue(self.simulated_page.input_data_select_values()[0].is_enabled())
        self.assertTrue(self.simulated_page.input_data_select_values()[1].is_enabled())
        self.assertTrue(self.simulated_page.input_data_select_values()[2].is_enabled())
