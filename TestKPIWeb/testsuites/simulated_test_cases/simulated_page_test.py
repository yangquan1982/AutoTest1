"""
KPI Web Test Cases
v0.0.1
2018
"""
import os
import unittest
import time
from util.simulated_page_validator import SimulatedPageValidator
from util.simulated_page_input_setter import SimulatedPageInputSetter
from util.browser_refresh import BrowserRefresher
from pageobjects.base_page import BasePage
from pageobjects.simulated_page import SimulatedPage
from util.test_case_state import TestCaseState
from util.selenium_webdriver_wrapper import WebDriver

# Global variables
CHROMEDRIVER = '../../chromedriver_web/chromedriver'
WAITING_SEC = 2
URL = "http://localhost:3030"
# EXPECT_URL = "http://ad-build-5:3030/#/graphs/simulated"
CMD = """osascript -e 'tell application "Google Chrome"
                   activate
                   delay 1
               end tell'"""


class SimulatedPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(URL, True).get_driver()
        cls.driver.maximize_window()
        os.system(CMD)
        time.sleep(WAITING_SEC)
        cls.base_page = BasePage(cls.driver)
        cls.simulated_page = SimulatedPage(cls.driver)
        cls.simulated_button = cls.base_page.ele_left_nav_simulated_btn()
        cls.simulated_button.click()
        time.sleep(WAITING_SEC)
        cls.test_case_state = TestCaseState(False)
        cls.browser_refresher = BrowserRefresher(cls.driver, cls.test_case_state)
        cls.simulated_page_validator = SimulatedPageValidator()
        cls.simulated_page_validator.set_refresher(cls.browser_refresher)
        cls.simulated_page_validator.set_base_page(cls.base_page)
        cls.simulated_page_validator.set_simulated_page(cls.simulated_page)
        cls.simulated_page_input_setter = SimulatedPageInputSetter(cls.simulated_page, cls.driver, cls.browser_refresher)

    def test_all_elements_initialized_success(self):
        """
        Verify proper rendering and visibility of all elements on simulated page
        """
        self.simulated_page_validator.validate_base_page_ini_elements_enabled()
        self.simulated_page_validator.validate_simulated_page_specific_ini_elements_enabled()

    # devel, first sim test, arc_500
    def test_devel_first_sim_test_arc_500_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 0, "acc free_driving_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 1, "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 2, "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 3, "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 4, "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 5, "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 6, "acc leader_vehicle_distance max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 7, "acc leader_vehicle_distance min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_distance_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_distance rms
        :return:
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 8, "acc leader_vehicle_distance rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_distance rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 9, "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 10, "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 11, "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 12, "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 13, "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 14, "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 15, "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 16, "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 17, "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 18, "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 19, "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 20, "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 21, "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 22, "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 23, "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: ad_miles
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 24, "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_ad_miles_overflow(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: ad_miles overflow
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 25, "ad_miles overflow"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "ad_miles overflow"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_ad_miles_segments(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: ad_miles segments
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 26, "ad_miles segments"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "ad_miles segments"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_ad_miles_segments_0(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: ad_miles segments 0
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 27, "ad_miles segments 0"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "ad_miles segments 0"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_cumulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: cumulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 28, "cumulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_cumulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: cumulative_driver_override_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 29, "cumulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_cumulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: cumulative_manual_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 30, "cumulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interaction_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interaction_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 31, "driver_interaction_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interaction_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_acc_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions acc_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 32,
                           "driver_interactions acc_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions acc_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_ad_disable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions ad_disable_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 33,
                           "driver_interactions ad_disable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions ad_disable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_ad_enable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions ad_enable_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 34,
                           "driver_interactions ad_enable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions ad_enable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_lk_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions lk_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 35,
                           "driver_interactions lk_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions lk_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_speed_offset_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions speed_offset_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 36,
                           "driver_interactions speed_offset_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions speed_offset_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_driver_interactions_turn_signal_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: driver_interactions turn_signal_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 37,
                           "driver_interactions turn_signal_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "driver_interactions turn_signal_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 38,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 39,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 40,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 41,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 42,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 43,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 44,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 45,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 46,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 47,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 48,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 49,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 50,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 51,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: manual_miles
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 52,
                           "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: override_count
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 53,
                           "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_arc_500_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: arc_500
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 0, "first sim test", 0, "arc_500", 54,
                           "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "arc_500", "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    # devel, first sim test, yo-1_lo-1
    def test_devel_first_sim_test_yo_1_lo_1_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 0,
                           "acc free_driving_velocity_error max"]
        self.browser_refresher.refresh_browser()
        self.test_case_state.set_is_set(False)
        time.sleep(WAITING_SEC)
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 1,
                           "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 2,
                           "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 3,
                           "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 4,
                           "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 5,
                           "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 6,
                           "acc leader_vehicle_distance max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 7,
                           "acc leader_vehicle_distance min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_distance_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_distance rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 8,
                           "acc leader_vehicle_distance rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_distance rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 9,
                           "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 10,
                           "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 11,
                           "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 12,
                           "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 13,
                           "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 14,
                           "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 15,
                           "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 16,
                           "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 17,
                           "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 18,
                           "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 19,
                           "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 20,
                           "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 21,
                           "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 22,
                           "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 23,
                           "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: ad_miles
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 24, "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_ad_miles_overflow(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: ad_miles overflow
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 25, "ad_miles overflow"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "ad_miles overflow"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_ad_miles_segments(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: ad_miles segments
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 26, "ad_miles segments"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "ad_miles segments"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_ad_miles_segments_0(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: ad_miles segments 0
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 27, "ad_miles segments 0"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "ad_miles segments 0"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_commit_hash(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: commit_hash
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 28, "commit_hash"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "commit_hash"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_cummulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: cummulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 29, "cummulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_cummulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: cummulative_driver_override_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 30, "cummulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_cummulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: cummulative_manual_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 31, "cummulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interaction_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interaction_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 32, "driver_interaction_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interaction_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_acc_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions acc_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 33,
                           "driver_interactions acc_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions acc_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_ad_disable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions ad_disable_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 34,
                           "driver_interactions ad_disable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions ad_disable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_ad_enable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions ad_enable_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 35,
                           "driver_interactions ad_enable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions ad_enable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_lk_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions lk_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 36,
                           "driver_interactions lk_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions lk_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_speed_offset_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions speed_offset_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 37,
                           "driver_interactions speed_offset_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions speed_offset_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_driver_interactions_turn_signal_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: driver_interactions turn_signal_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 38,
                           "driver_interactions turn_signal_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "driver_interactions turn_signal_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 39,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 40,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 41,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 42,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 43,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 44,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 45,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 46,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 47,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 48,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_new_leader_detection_signals_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection new_leader_detection_signals max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 49,
                           "leader_detection new_leader_detection_signals max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection new_leader_detection_signals max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_new_leader_detection_signals_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection new_leader_detection_signals min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 50,
                           "leader_detection new_leader_detection_signals min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection new_leader_detection_signals min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_new_leader_detection_signals_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection new_leader_detection_signals rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 51,
                           "leader_detection new_leader_detection_signals rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection new_leader_detection_signals rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 52,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 53,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 54,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 55,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: manual_miles
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 56, "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_new_kpi_example(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: new_kpi_example
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 57, "new_kpi_example"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "new_kpi_example"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: override_count
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 58, "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1", "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo_1_lo_1_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo-1_lo-1
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 0, "first sim test", 1, "yo-1_lo-1", 59, "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo-1_lo-1",
                                                          "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    # devel, first sim test, yo0_lo0
    def test_devel_first_sim_test_yo0_lo0_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 0,
                           "acc free_driving_velocity_error max"]
        self.browser_refresher.refresh_browser()
        self.test_case_state.set_is_set(False)
        time.sleep(WAITING_SEC)
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 1,
                           "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 2,
                           "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 3,
                           "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 4,
                           "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 5,
                           "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 6,
                           "acc leader_vehicle_distance max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 7,
                           "acc leader_vehicle_distance min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_distance_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_distance rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 8,
                           "acc leader_vehicle_distance rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_distance rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 9,
                           "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 10,
                           "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 11,
                           "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 12,
                           "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 13,
                           "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 14,
                           "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 15,
                           "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 16,
                           "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 17,
                           "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 18,
                           "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 19,
                           "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 20,
                           "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 21,
                           "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 22,
                           "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 23,
                           "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: ad_miles
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 24, "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_ad_miles_overflow(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: ad_miles overflow
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 25, "ad_miles overflow"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "ad_miles overflow"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_ad_miles_segments(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: ad_miles segments
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 26, "ad_miles segments"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "ad_miles segments"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_ad_miles_segments_0(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: ad_miles segments 0
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 27, "ad_miles segments 0"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "ad_miles segments 0"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_commit_hash(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: commit_hash
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 28, "commit_hash"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "commit_hash"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_cummulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: cummulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 29, "cummulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_cummulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: cummulative_driver_override_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 30, "cummulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_cummulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: cummulative_manual_miles_driven
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 31, "cummulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interaction_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interaction_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 32, "driver_interaction_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interaction_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_acc_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions acc_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 33,
                           "driver_interactions acc_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions acc_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_ad_disable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions ad_disable_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 34,
                           "driver_interactions ad_disable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions ad_disable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_ad_enable_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions ad_enable_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 35,
                           "driver_interactions ad_enable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions ad_enable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_lk_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions lk_enable_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 36,
                           "driver_interactions lk_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions lk_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_speed_offset_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions speed_offset_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 37,
                           "driver_interactions speed_offset_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions speed_offset_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_driver_interactions_turn_signal_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: driver_interactions turn_signal_change_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 38,
                           "driver_interactions turn_signal_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "driver_interactions turn_signal_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 39,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 40,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 41,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 42,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 43,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 44,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 45,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 46,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 47,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 48,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_new_leader_detection_signals_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection new_leader_detection_signals max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 49,
                           "leader_detection new_leader_detection_signals max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection new_leader_detection_signals max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_new_leader_detection_signals_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection new_leader_detection_signals min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 50,
                           "leader_detection new_leader_detection_signals min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection new_leader_detection_signals min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_new_leader_detection_signals_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection new_leader_detection_signals rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 51,
                           "leader_detection new_leader_detection_signals rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection new_leader_detection_signals rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 52,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 53,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 54,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 55,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: manual_miles
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 56, "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_new_kpi_example(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: new_kpi_example
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 57, "new_kpi_example"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "new_kpi_example"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: override_count
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 58, "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0", "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_first_sim_test_yo0_lo0_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: first sim test
        TEST CASE: yo0_lo0
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 0, "first sim test", 2, "yo0_lo0", 59, "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "first sim test", "yo0_lo0",
                                                          "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    # devel, two target tylenol circuit, simple_acc_test
    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 0,
                           "acc free_driving_velocity_error max"]
        self.browser_refresher.refresh_browser()
        self.test_case_state.set_is_set(False)
        time.sleep(WAITING_SEC)
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), True)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 1,
                           "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 2,
                           "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 3,
                           "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 4,
                           "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 5,
                           "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 6,
                           "acc leader_vehicle_distance max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 7,
                           "acc leader_vehicle_distance min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_distance_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_distance rms
        :return:
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 8,
                           "acc leader_vehicle_distance rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_distance rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 9,
                           "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 10,
                           "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 11,
                           "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 12,
                           "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 13,
                           "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 14,
                           "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 15,
                           "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 16,
                           "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 17,
                           "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 18,
                           "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 19,
                           "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 20,
                           "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 21,
                           "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 22,
                           "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 23,
                           "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: ad_miles
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 24, "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_ad_miles_overflow(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: ad_miles overflow
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 25, "ad_miles overflow"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "ad_miles overflow"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_ad_miles_segments(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: ad_miles segments
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 26, "ad_miles segments"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "ad_miles segments"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_ad_miles_segments_0(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: ad_miles segments 0
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 27, "ad_miles segments 0"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "ad_miles segments 0"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_cumulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: cumulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 28,
                           "cumulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_cumulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: cumulative_driver_override_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 29,
                           "cumulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_cumulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: cumulative_manual_miles_driven
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 30,
                           "cumulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interaction_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interaction_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 31,
                           "driver_interaction_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interaction_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_acc_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions acc_enable_change_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 32,
                           "driver_interactions acc_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions acc_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_ad_disable_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions ad_disable_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 33,
                           "driver_interactions ad_disable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions ad_disable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_ad_enable_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions ad_enable_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 34,
                           "driver_interactions ad_enable_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions ad_enable_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_lk_enable_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions lk_enable_change_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 35,
                           "driver_interactions lk_enable_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions lk_enable_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_speed_offset_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions speed_offset_change_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 36,
                           "driver_interactions speed_offset_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions speed_offset_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_driver_interactions_turn_signal_change_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: driver_interactions turn_signal_change_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 37,
                           "driver_interactions turn_signal_change_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "driver_interactions turn_signal_change_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 38,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 39,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 40,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 41,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 42,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 43,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 44,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 45,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 46,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 47,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 48,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 49,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 50,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 51,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: manual_miles
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 52,
                           "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: override_count
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 53,
                           "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_two_target_tylenol_circuit_simple_acc_test_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: two target tylenol circuit
        TEST CASE: simple_acc_test
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 1, "two target tylenol circuit", 0, "simple_acc_test", 54,
                           "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "two target tylenol circuit", "simple_acc_test",
                                                          "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    # # devel, two target tylenonl circuit, simple_acc_test
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_free_driving_velocity_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc free_driving_velocity_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 0,
    #                        "acc free_driving_velocity_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), True)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc free_driving_velocity_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_free_driving_velocity_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc free_driving_velocity_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 1,
    #                        "acc free_driving_velocity_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc free_driving_velocity_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_free_driving_velocity_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc free_driving_velocity_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 2,
    #                        "acc free_driving_velocity_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc free_driving_velocity_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 3,
    #                        "acc leader_vehicle_distance_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 4,
    #                        "acc leader_vehicle_distance_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 5,
    #                        "acc leader_vehicle_distance_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 6,
    #                        "acc leader_vehicle_distance max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 7,
    #                        "acc leader_vehicle_distance min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_distance_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_distance rms
    #     :return:
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 8,
    #                        "acc leader_vehicle_distance rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_distance rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_velocity_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 9,
    #                        "acc leader_vehicle_velocity_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_velocity_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_velocity_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 10,
    #                        "acc leader_vehicle_velocity_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_velocity_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_leader_vehicle_velocity_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc leader_vehicle_velocity_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 11,
    #                        "acc leader_vehicle_velocity_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc leader_vehicle_velocity_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_acceleration_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_acceleration max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 12,
    #                        "acc longitudinal_acceleration max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_acceleration max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_acceleration_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_acceleration min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 13,
    #                        "acc longitudinal_acceleration min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_acceleration min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_acceleration_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_acceleration rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 14,
    #                        "acc longitudinal_acceleration rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_acceleration rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_jerk_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_jerk max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 15,
    #                        "acc longitudinal_jerk max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_jerk max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_jerk_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_jerk min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 16,
    #                        "acc longitudinal_jerk min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_jerk min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_longitudinal_jerk_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc longitudinal_jerk rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 17,
    #                        "acc longitudinal_jerk rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc longitudinal_jerk rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_distance_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_distance_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 18,
    #                        "acc traffic_light_distance_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_distance_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_distance_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_distance_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 19,
    #                        "acc traffic_light_distance_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_distance_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_distance_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_distance_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 20,
    #                        "acc traffic_light_distance_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_distance_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_velocity_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_velocity_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 21,
    #                        "acc traffic_light_velocity_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_velocity_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_velocity_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_velocity_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 22,
    #                        "acc traffic_light_velocity_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_velocity_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_acc_traffic_light_velocity_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: acc traffic_light_velocity_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 23,
    #                        "acc traffic_light_velocity_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "acc traffic_light_velocity_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_ad_miles(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: ad_miles
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 24, "ad_miles"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "ad_miles"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_ad_miles_overflow(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: ad_miles overflow
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 25, "ad_miles overflow"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "ad_miles overflow"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_ad_miles_segments(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: ad_miles segments
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 26, "ad_miles segments"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "ad_miles segments"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_ad_miles_segments_0(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: ad_miles segments 0
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 27, "ad_miles segments 0"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "ad_miles segments 0"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_cumulative_autonomous_miles_driven(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: cumulative_autonomous_miles_driven
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 28,
    #                        "cumulative_autonomous_miles_driven"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "cummulative_autonomous_miles_driven"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_cumulative_driver_override_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: cumulative_driver_override_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 29,
    #                        "cumulative_driver_override_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "cummulative_driver_override_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_cumulative_manual_miles_driven(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: cumulative_manual_miles_driven
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 30,
    #                        "cumulative_manual_miles_driven"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "cummulative_manual_miles_driven"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interaction_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interaction_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 31,
    #                        "driver_interaction_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interaction_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_acc_enable_change_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions acc_enable_change_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 32,
    #                        "driver_interactions acc_enable_change_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions acc_enable_change_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_ad_disable_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions ad_disable_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 33,
    #                        "driver_interactions ad_disable_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions ad_disable_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_ad_enable_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions ad_enable_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 34,
    #                        "driver_interactions ad_enable_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions ad_enable_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_lk_enable_change_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions lk_enable_change_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 35,
    #                        "driver_interactions lk_enable_change_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions lk_enable_change_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_speed_offset_change_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions speed_offset_change_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 36,
    #                        "driver_interactions speed_offset_change_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions speed_offset_change_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_driver_interactions_turn_signal_change_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: driver_interactions turn_signal_change_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 37,
    #                        "driver_interactions turn_signal_change_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "driver_interactions turn_signal_change_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lat_acc_violation_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lat_acc_violation_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 38,
    #                        "lat_acc_violation_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lat_acc_violation_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_heading_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc heading_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 39,
    #                        "lc heading_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc heading_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_heading_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc heading_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 40,
    #                        "lc heading_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc heading_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_heading_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc heading_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 41,
    #                        "lc heading_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc heading_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_lateral_error_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc lateral_error max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 42,
    #                        "lc lateral_error max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc lateral_error max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_lateral_error_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc lateral_error min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 43,
    #                        "lc lateral_error min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc lateral_error min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lc_lateral_error_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lc lateral_error rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 44,
    #                        "lc lateral_error rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lc lateral_error rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_distance_std_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection distance_std max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 45,
    #                        "leader_detection distance_std max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection distance_std max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_distance_std_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection distance_std min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 46,
    #                        "leader_detection distance_std min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection distance_std min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_distance_std_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection distance_std rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 47,
    #                        "leader_detection distance_std rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection distance_std rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_velocity_std_max(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection velocity_std max
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 48,
    #                        "leader_detection velocity_std max"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection velocity_std max"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_velocity_std_min(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection velocity_std min
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 49,
    #                        "leader_detection velocity_std min"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection velocity_std min"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_leader_detection_velocity_std_rms(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: leader_detection velocity_std rms
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 50,
    #                        "leader_detection velocity_std rms"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "leader_detection velocity_std rms"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_lon_acc_violation_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: lon_acc_violation_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 51,
    #                        "lon_acc_violation_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "lon_acc_violation_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_manual_miles(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: manual_miles
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 52,
    #                        "manual_miles"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "manual_miles"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_override_count(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: override_count
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 53,
    #                        "override_count"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "override_count"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)
	#
    # def test_devel_two_target_tylenonl_circuit_simple_acc_test_trip_start_timestamp(self):
    #     """
    #     BRANCH: devel
    #     TEST SUITE: two target tylenonl circuit
    #     TEST CASE: simple_acc_test
    #     KPI: trip_start_timestamp
    #     """
    #     input_data_list = ["devel", 2, "two target tylenonl circuit", 0, "simple_acc_test", 54,
    #                        "trip_start_timestamp"]
    #     self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
    #     time.sleep(WAITING_SEC)
    #     try:
    #         # Validate simulated page specific elements after selection
    #         self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
    #         # Validation input parameters
    #         self.simulated_page_validator.validate_input(["devel", "two target tylenonl circuit", "simple_acc_test",
    #                                                       "trip_start_timestamp"])
    #         # Validation output parameters and chart
    #         self.simulated_page_validator.validate_output()
    #         self.test_case_state.set_is_set(True)
    #     except:
    #         self.browser_refresher.refresh_browser()
    #         self.test_case_state.set_is_set(False)
    #         self.assertTrue(False)

    # devel, sample algorithms test, yo-1_lo0
    def test_devel_sample_algorithms_test_yo_1_lo0_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 0,
                           "acc free_driving_velocity_error max"]
        self.browser_refresher.refresh_browser()
        self.test_case_state.set_is_set(False)
        time.sleep(WAITING_SEC)
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), True)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 1,
                           "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 2,
                           "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 3,
                           "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 4,
                           "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 5,
                           "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 6,
                           "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 7,
                           "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 8,
                           "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 9,
                           "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 10,
                           "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 11,
                           "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 12,
                           "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 13,
                           "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 14,
                           "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 15,
                           "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 16,
                           "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 17,
                           "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 18,
                           "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 19,
                           "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 20,
                           "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: ad_miles
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 21,
                           "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_commit_hash(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: commit_hash
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 22,
                           "commit_hash"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "commit_hash"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_cummulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: cummulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 23,
                           "cummulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_cummulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: cummulative_driver_override_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 24,
                           "cummulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_cummulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: cummulative_manual_miles_driven
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 25,
                           "cummulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 26,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 27,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 28,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 29,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 30,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 31,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 32,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 33,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 34,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 35,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 36,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 37,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 38,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 39,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: manual_miles
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 40,
                           "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: override_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 41,
                           "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo_1_lo0_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo-1_lo0
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 3, "sample algorithms test", 1, "yo-1_lo0", 42,
                           "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo-1_lo0",
                                                          "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    # devel, sample algorithms test, yo0_lo-1
    def test_devel_sample_algorithms_test_yo0_lo_1_acc_free_driving_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc free_driving_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 0,
                           "acc free_driving_velocity_error max"]
        self.browser_refresher.refresh_browser()
        self.test_case_state.set_is_set(False)
        time.sleep(WAITING_SEC)
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), True)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc free_driving_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_free_driving_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc free_driving_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 1,
                           "acc free_driving_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc free_driving_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_free_driving_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc free_driving_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 2,
                           "acc free_driving_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc free_driving_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_distance_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 3,
                           "acc leader_vehicle_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_distance_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 4,
                           "acc leader_vehicle_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_distance_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 5,
                           "acc leader_vehicle_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 6,
                           "acc leader_vehicle_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 7,
                           "acc leader_vehicle_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_leader_vehicle_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc leader_vehicle_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 8,
                           "acc leader_vehicle_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc leader_vehicle_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_acceleration_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_acceleration max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 9,
                           "acc longitudinal_acceleration max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_acceleration max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_acceleration_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_acceleration min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 10,
                           "acc longitudinal_acceleration min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_acceleration min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_acceleration_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_acceleration rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 11,
                           "acc longitudinal_acceleration rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_acceleration rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_jerk_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_jerk max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 12,
                           "acc longitudinal_jerk max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_jerk max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_jerk_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_jerk min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 13,
                           "acc longitudinal_jerk min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_jerk min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_longitudinal_jerk_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc longitudinal_jerk rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 14,
                           "acc longitudinal_jerk rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc longitudinal_jerk rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_distance_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_distance_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 15,
                           "acc traffic_light_distance_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_distance_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_distance_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_distance_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 16,
                           "acc traffic_light_distance_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_distance_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_distance_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_distance_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 17,
                           "acc traffic_light_distance_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_distance_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_velocity_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_velocity_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 18,
                           "acc traffic_light_velocity_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_velocity_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_velocity_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_velocity_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 19,
                           "acc traffic_light_velocity_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_velocity_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_acc_traffic_light_velocity_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: acc traffic_light_velocity_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 20,
                           "acc traffic_light_velocity_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "acc traffic_light_velocity_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_ad_miles(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: ad_miles
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 21,
                           "ad_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "ad_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_commit_hash(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: commit_hash
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 22,
                           "commit_hash"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "commit_hash"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_cummulative_autonomous_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: cummulative_autonomous_miles_driven
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 23,
                           "cummulative_autonomous_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "cummulative_autonomous_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_cummulative_driver_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: cummulative_driver_override_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 24,
                           "cummulative_driver_override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "cummulative_driver_override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_cummulative_manual_miles_driven(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: cummulative_manual_miles_driven
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 25,
                           "cummulative_manual_miles_driven"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "cummulative_manual_miles_driven"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lat_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lat_acc_violation_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 26,
                           "lat_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lat_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_heading_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc heading_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 27,
                           "lc heading_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc heading_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_heading_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc heading_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 28,
                           "lc heading_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc heading_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_heading_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc heading_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 29,
                           "lc heading_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc heading_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_lateral_error_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc lateral_error max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 30,
                           "lc lateral_error max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc lateral_error max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_lateral_error_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc lateral_error min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 31,
                           "lc lateral_error min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc lateral_error min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lc_lateral_error_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lc lateral_error rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 32,
                           "lc lateral_error rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lc lateral_error rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_distance_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection distance_std max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 33,
                           "leader_detection distance_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection distance_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_distance_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection distance_std min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 34,
                           "leader_detection distance_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection distance_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_distance_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection distance_std rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 35,
                           "leader_detection distance_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection distance_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_velocity_std_max(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection velocity_std max
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 36,
                           "leader_detection velocity_std max"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection velocity_std max"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_velocity_std_min(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection velocity_std min
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 37,
                           "leader_detection velocity_std min"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection velocity_std min"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_leader_detection_velocity_std_rms(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: leader_detection velocity_std rms
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 38,
                           "leader_detection velocity_std rms"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "leader_detection velocity_std rms"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_lon_acc_violation_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: lon_acc_violation_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 39,
                           "lon_acc_violation_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "lon_acc_violation_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_manual_miles(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: manual_miles
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 40,
                           "manual_miles"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "manual_miles"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_override_count(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: override_count
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 41,
                           "override_count"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "override_count"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    def test_devel_sample_algorithms_test_yo0_lo_1_trip_start_timestamp(self):
        """
        BRANCH: devel
        TEST SUITE: sample algorithms test
        TEST CASE: yo0_lo-1
        KPI: trip_start_timestamp
        """
        input_data_list = ["devel", 3, "sample algorithms test", 2, "yo0_lo-1", 42,
                           "trip_start_timestamp"]
        self.simulated_page_input_setter.set_input_data(input_data_list, self.test_case_state.get_is_set(), False)
        time.sleep(WAITING_SEC)
        try:
            # Validate simulated page specific elements after selection
            self.simulated_page_validator.validate_simulated_page_specific_after_selection_elements_enabled()
            # Validation input parameters
            self.simulated_page_validator.validate_input(["devel", "sample algorithms test", "yo0_lo-1",
                                                          "trip_start_timestamp"])
            # Validation output parameters and chart
            self.simulated_page_validator.validate_output()
            self.test_case_state.set_is_set(True)
        except:
            self.browser_refresher.refresh_browser()
            self.test_case_state.set_is_set(False)
            self.assertTrue(False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
