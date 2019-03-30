"""
Refresh browser within time frame in 2 seconds
"""
import time
from singleton_decorator import singleton


@singleton
class BrowserRefresher(object):

    WAITING_SEC = 2

    def __init__(self, driver, test_case_state):
        super().__init__()
        self.driver = driver
        self.test_case_state = test_case_state

    def refresh_browser(self):
        time.sleep(self.WAITING_SEC)
        self.driver.refresh()
        self.test_case_state.set_is_set(False)
        time.sleep(self.WAITING_SEC)
