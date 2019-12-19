#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from appium import webdriver

class ChromeTests(unittest.TestCase):
    def get_desired_capabilities(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'newCommandTimeout': 240,
            'automationName': 'UIAutomator2',
            'uiautomator2ServerInstallTimeout': 120000,
            'adbExecTimeout': 120000
        }
        return desired_caps

    def setUp(self):
        caps = self.get_desired_capabilities()
        caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        self.driver.get("http://html5geek.azurewebsites.net/")
        self.driver.find_element_by_link_text("Vuejs test page").click()
        self.assertTrue('Vue.js test home page' in self.driver.page_source)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChromeTests)
    unittest.TextTestRunner(verbosity=2).run(suite)