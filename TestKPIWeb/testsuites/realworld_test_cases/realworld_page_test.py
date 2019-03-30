"""
KPI Web Test Cases
v0.0.1
2018
"""
import unittest
import time
import os
from selenium import webdriver
from pageobjects.base_page import BasePage
from pageobjects.real_world_page import RealWorldPage
from selenium.webdriver.chrome.options import Options

# Global variables
CHROMEDRIVER = '../../chromedriver_web/chromedriver'
WAITING_SEC = 2
URL = "http://localhost:3030"
EXPECT_URL = "http://ad-build-5:3030/#/graphs/simulated"
CMD = """osascript -e 'tell application "Google Chrome"
                   activate
                   delay 1
               end tell'"""


class RealworldPageIniTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # cls.driver = Webdriver.get_intance()
        cls.opts = Options()
        cls.opts.add_argument('--ignore-certificate-errors')
        cls.opts.add_argument("--test-type")
        cls.opts.add_argument("--headless")
        cls.driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=cls.opts)
        cls.driver.implicitly_wait(WAITING_SEC)
        os.system(CMD)
        cls.driver.get(URL)
        time.sleep(WAITING_SEC)
        cls.base_page = BasePage(cls.driver)
        cls.realworld_page = RealWorldPage(cls.driver)
        cls.realworld_button = cls.base_page._BasePage__ele_left_nav_realworld_btn()
        cls.realworld_button.click()
        time.sleep(WAITING_SEC)

    def test_all_elements_initialized(self):
        """
        Verify proper rendering and visibility of all elements on simulated page
        """
        # Validate base page elements
        self.assertTrue(self.base_page._BasePage__ele_top_bar().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_nio_logo().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_top_left_btn().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_left_nav_bar().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_left_nav_simulated_btn().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_left_nav_realworld_btn().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_left_nav_bounds_btn().is_enabled())
        self.assertTrue(self.base_page._BasePage__ele_main_pad().is_enabled())
        self.assertTrue(self.base_page.get_app_title() == self.base_page.app_title)

        # Validate realworld page specific elements
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_label_car().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_selector_car().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_label_kpi().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_selector_kpi().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_label_daterange().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_start_date().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__input_data_end_date().is_enabled())
        self.assertTrue(self.realworld_page._RealWorldPage__output_data_chart().is_enabled())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
