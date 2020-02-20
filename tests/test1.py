import os
import unittest
from appium import webdriver
from time import sleep


class MacInstalledAppTests(unittest.TestCase):

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps["platformName"] = "Mac"
        desired_caps["deviceName"] = "Mac"
        desired_caps["app"] = "/Applications/Calculator.app"


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    '''def test_new_note(self):
        "Test the Notes app launches correctly and click on new note button"
        element = self.driver.find_element_by_id("uk.co.aifactory.chessfree:id/ButtonPlay")
        element.click()
        sleep(5)'''

    def test_initialize(self):
        #self.driver.find_element_by_name("One").click()
        #self.driver.find_element_by_name("Seven").click()
        #self.assertEqual(self.getresults(), "7")
        self.driver.find_element_by_name("Clear").click()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MacInstalledAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)