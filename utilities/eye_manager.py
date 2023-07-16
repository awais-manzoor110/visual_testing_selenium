from applitools.common import BatchInfo
from applitools.common.selenium import Configuration
from applitools.selenium import Eyes
from utilities.baseclass import BaseClass

APP_NAME = 'automation_bookstore'
appilitools_api_key = "uM61UPR7DiRPvcPJ5G8RCCHnAQBpfIVJ6YdXHYeAP78110"


#
class Eyes_Manager(BaseClass):
    @staticmethod
    def initialize_eyes():
        eyes = Eyes()
        eyes.set_configuration(Eyes_Manager.set_batch("first batch"))
        eyes.api_key = appilitools_api_key

        return eyes

    def validate_window(self, driver, eyes, tag=None):
        self.open_eyes(driver, eyes)
        # eyes_param.match_level = MatchLevel
        # eyes_param.force_full_page_screenshot = True
        eyes.check_window(tag=tag)
        self.close_eyes(eyes)

    def validate_element(self, driver, eyes, element, tag=None):
        self.open_eyes(driver, eyes)
        eyes.check_region(element, tag=tag)
        # eyes_param.match_level = MatchLevel
        self.close_eyes(eyes)

    @staticmethod
    def set_batch(batch_name):
        if batch_name:
            suite_config = (Configuration().set_batch(BatchInfo(batch_name)))
            return suite_config

    @staticmethod
    def open_eyes(driver, eyes):
        eyes.open(driver, APP_NAME, test_name=Eyes_Manager.get_test_name())

    @staticmethod
    def get_test_name():
        import inspect
        return inspect.stack()[3].function

    def close_eyes(self, eyes):
        eyes.close()
