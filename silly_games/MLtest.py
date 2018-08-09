import unittest
from appium import webdriver

class DialPhoneTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['deviceConnectUsername'] = 'admin'
        desired_caps['deviceConnectApiKey'] = 'fddc063b-72bc-46a6-9060-6ae256455d5d'
        desired_caps['deviceConnectSkipInstall'] = 1
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['udid'] = '1c83df18f017c7c01a2839ecc11b0e7e245bb2b8'
        desired_caps['platformName'] = 'iOS'
        desired_caps['bundleId'] = 'com.mobilelabsinc.PhoneLookup'
        desired_caps['automationName'] = 'XCUITest'

        self.driver = webdriver.Remote('http://10.10.0.31/Appium', desired_caps)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@label='Enter Username']").click()
        self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@label='Enter Username']").setValue("test")
        self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@label='Enter Password']").click()
        self.driver.find_element_by_xpath("//XCUIElementTypeTextField[@label='Enter Password']").setValue("test")



suite = unittest.TestLoader().loadTestsFromTestCase(DialPhoneTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
