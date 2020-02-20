import os
import unittest
from appium import webdriver
from time import sleep


class MacToDoTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "Pixel 2"
        desired_caps["app"] = "/Users/yulianayagodka/WS/Minimal-Todo/app/build/outputs/apk/debug/app-debug.apk"
        #desired_caps["appActivity"] = "com.example.avjindersinghsekhon.minimaltodo.Main.MainActivity",
        #desired_caps["appPackage"] = "com.avjindersinghsekhon.minimaltodo",

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_initialize(self):
        self.driver.find_element_by_id("com.avjindersinghsekhon.minimaltodo:id/addToDoItemFAB").click()
        sleep(7)


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MacToDoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)