from webelements.base_web_elements import BasePageWebElements


class BasePage(object):
    """[summary]
    Base class for all page objects.
    """
    
    # Webdriver associated with this instance of the PageObject
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.app_title = "AD KPIs"
        # self._validate_page(driver)
        # Element locators area
        self.ele_top_bar_locator_xpath = \
            BasePageWebElements.locators['ele_top_bar_locator_xpath']
        self.ele_nio_logo_locator_xpath = \
            BasePageWebElements.locators['ele_nio_logo_locator_xpath']
        self.ele_top_left_btn_locator_xpath = \
            BasePageWebElements.locators['ele_top_left_btn_locator_xpath']
        self.ele_left_nav_bar_locator_xpath = \
            BasePageWebElements.locators['ele_left_nav_bar_locator_xpath']
        self.ele_left_nav_buttons_locator_xpath = \
            BasePageWebElements.locators['ele_left_nav_button_elements_locator_xpath']
        self.ele_main_pad_locator_xpath = \
            BasePageWebElements.locators['ele_main_pad_locator_xpath']

    def get_all_nav_button_elements(self):
        all_button_elements = self.driver.find_elements_by_xpath(self.get_all_locators()['ele_left_nav_button_elements_locator_xpath'])
        return all_button_elements

    def ele_top_bar(self):
        return self.driver.find_element_by_xpath(self.ele_top_bar_locator_xpath)

    def ele_nio_logo(self):
        return self.driver.find_element_by_xpath(self.ele_nio_logo_locator_xpath)

    def ele_top_left_btn(self):
        return self.driver.find_element_by_xpath(self.ele_top_left_btn_locator_xpath)

    def ele_left_nav_bar(self):
        return self.driver.find_element_by_xpath(self.ele_left_nav_bar_locator_xpath)

    def ele_left_nav_simulated_btn(self):
        return self.get_all_nav_button_elements()[0]

    def ele_left_nav_realworld_btn(self):
        return self.get_all_nav_button_elements()[1]

    def ele_left_nav_bounds_btn(self):
        return self.get_all_nav_button_elements()[2]

    def ele_main_pad(self):
        return self.driver.find_element_by_xpath(self.ele_main_pad_locator_xpath)

    def get_app_title(self):
        return self.driver.title

    @staticmethod
    def get_all_locators():
        return BasePageWebElements.locators

    def get_all_elements(self):
        elements = list()
        locators = self.get_all_locators()
        for locator_key in locators.keys():
            elements.append(self.driver.find_element_by_xpath(locators[locator_key]))
        return elements

    # @abstractmethod
    # def _validate_page(self, driver):
    #     """Perform checks to validate this page is the correct target page.
    #     @raise IncorrectPageException: Raised when we try to assign the wrong page
    #     to this page object."""
    #     pass
        # self.assertTrue(self.__ele_top_bar().is_enabled())
        # self.assertTrue(self.__ele_nio_logo().is_enabled())
        # self.assertTrue(self.__ele_top_left_btn().is_enabled())
        # self.assertTrue(self.__ele_left_nav_bar().is_enabled())
        # self.assertTrue(self.__ele_left_nav_simulated_btn().is_enabled())
        # self.assertTrue(self.__ele_left_nav_realworld_btn().is_enabled())
        # self.assertTrue(self.__ele_left_nav_bounds_btn().is_enabled())
        # self.assertTrue(self.__ele_main_pad().is_enabled())
        # self.assertTrue(self.get_app_title() == self.app_title)

# class InvalidPageError(Exception):
#     '''Thrown when we have tried to instantiate the incorrect page to a PageObject.'''

#     def __init__(self, *args: object, **kwargs: object) -> None:
#         super().__init__(*args, **kwargs)

#     def with_traceback(self, tb: Optional[TracebackType]) -> BaseException:
#         return super().with_traceback(tb)

