import unittest
import os
import inspect
import HtmlTestRunner
import os
from selenium import webdriver
import locators
import pages
from locators import URLS, LogInPageObject, MainPageObject, ChartPageObject
from applitools.selenium import Eyes, Target, BatchInfo, Region, MatchLevel



APP_VERSION = 1


class VisualAITests(unittest.TestCase):


    '''Load Eyes and set API key'''
    eyes = Eyes()
    eyes.api_key = (os.environ['MY_APPLITOOLS_API_KEY'])

    '''Set Batch name'''
    if (APP_VERSION == 1):
        eyes.batch = BatchInfo(name="Application Version 1")
    elif (APP_VERSION == 2):
        eyes.batch = BatchInfo(name="Application Version 2")

    '''Set URLS'''
    if (APP_VERSION == 1):
        LOGIN_URL = str(locators.URLS.URL)
    elif (APP_VERSION == 2):
        LOGIN_URL = str(locators.URLS.URL_V2)

    if (APP_VERSION == 1):
        MAIN_URL = str(locators.URLS.MAIN)
    elif (APP_VERSION == 2):
        MAIN_URL = str(locators.URLS.MAIN_V2)

    if (APP_VERSION == 1):
        CHART_URL = str(locators.URLS.CHART)
    elif (APP_VERSION == 2):
        CHART_URL = str(locators.URLS.CHART_V2)

    if (APP_VERSION == 1):
        MAIN_WITH_ADS_URL = str(locators.URLS.MAIN_WITH_ADS)
    elif (APP_VERSION == 2):
        MAIN_WITH_ADS_URL = str(locators.URLS.MAIN_WITH_ADS_V2)

    '''Set Regions'''
    ALERT_REGION = Region(288, 288, 448, 64)
    JAN_CHART = Region(57, 172, 131, 382)
    FEB_CHART = Region(187, 171, 133, 385)
    MAR_CHART = Region(318, 171, 135, 385)
    APR_CHART = Region(452, 172, 131, 384)
    MAY_CHART = Region(585, 172, 131, 383)
    JUN_CHART = Region(715, 171, 133, 385)
    JUL_CHART = Region(847, 172, 133, 338)
    AD_1 = Region(43, 210, 133, 103)
    AD_2 = Region(455, 207, 146, 108)

    '''Set Browser size'''
    VIEWPORT = {'width': 1024, 'height': 768}


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.AssertionErrors = []


    def test_Login_Page_UI_Elements_Test(self):
        '''Set up test function'''
        def check_ui_elements():
            '''Check login page UI Elements'''
            try:
                self.eyes.open(self.driver, "Hackathon", "Login", self.VIEWPORT)
                self.driver.get(self.LOGIN_URL)
                self.eyes.match_level  = "exact"
                self.eyes.check_window("Login V" + str(APP_VERSION))
            finally:
                self.eyes.close()

        '''Run UI elements test function'''
        try: check_ui_elements()
        except Exception: self.AssertionErrors.append(str("Difference Detected in Login page UI"))


    def test_Data_Driven_Test(self):
        '''Set up test functions'''
        def no_credentials():
            '''If you don’t enter the username and password and click the login button, it should throw an error'''
            try:
                login_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Data Driven - No Username or Password provided", self.VIEWPORT)
                self.driver.get(self.LOGIN_URL)
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON), "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))
                login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
                self.eyes.match_level  = "exact"
                self.eyes.check_region(region=self.ALERT_REGION, tag="Data Driven V" + str(APP_VERSION) + " - No Credentials provided")
            finally:
                self.eyes.close()

        def only_username():
            '''If you only enter the username and click the login button, it should throw an error'''
            try:
                login_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Data Driven - No Password provided", self.VIEWPORT)
                self.driver.get(self.LOGIN_URL)
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT), "Cannot find Username Input --> " + str(LogInPageObject.USERNAME_INPUT[1]))
                login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON), "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))
                login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
                self.eyes.match_level  = "exact"
                self.eyes.check_region(region=self.ALERT_REGION, tag="Data Driven V"  + str(APP_VERSION) + " - No Password provided")
            finally:
                self.eyes.close()

        def only_password():
            '''If you only enter the password and click the login button, it should throw an error'''
            try:
                login_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Data Driven - No Username provided", self.VIEWPORT)
                self.driver.get(self.LOGIN_URL)
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT), "Cannot find Password Input --> " + str(LogInPageObject.PASSWORD_INPUT[1]))
                login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON), "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))
                login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
                self.eyes.match_level  = "exact"
                self.eyes.check_region(region=self.ALERT_REGION, tag="Data Driven V"  + str(APP_VERSION) + " - No Username provided")
            finally:
                self.eyes.close()

        def should_login():
            '''If you enter both username (any value) and password (any value), it should log you in.'''
            try:
                login_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Data Driven - Can Login", self.VIEWPORT)
                self.driver.get(self.LOGIN_URL)
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT), "Cannot find Username Input --> " + str(LogInPageObject.USERNAME_INPUT[1]))
                login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT), "Cannot find Password Input --> " + str(LogInPageObject.PASSWORD_INPUT[1]))
                login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")
                self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON), "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))
                login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
                main_page = pages.CommonClass(self.driver)
                self.eyes.match_level  = "exact"
                self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.AVATAR_TOP_RIGHT), "Cannot find expected element --> " + str(MainPageObject.AVATAR_TOP_RIGHT[1]))
                self.eyes.match_level  = "layout"
                self.eyes.check_window("Logged In V"  + str(APP_VERSION))
            finally:
                self.eyes.close()

        '''Run All 4 functions of the data driven test'''
        try: no_credentials()
        except Exception: self.AssertionErrors.append(str("Difference Detected when no credentials provided for login"))
        try: only_username()
        except Exception: self.AssertionErrors.append(str("Difference Detected when only username provided for login"))
        try: only_password()
        except Exception: self.AssertionErrors.append(str("Difference Detected when only password provided for login"))
        try: should_login()
        except Exception: self.AssertionErrors.append(str("Difference Detected when logging in with both username and password"))


    def test_Table_Sort_Test(self):
        '''Set up test function'''
        def table_sort():
            '''If you only enter the password and click the login button, it should throw an error'''
            try:
                main_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Table Sort Test", self.VIEWPORT)
                self.driver.get(self.MAIN_URL)
                self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.TABLE), "Cannot find expected element --> " + str(MainPageObject.TABLE[1]))
                main_page.element_click(locator=MainPageObject.TABLE_HEADER_AMOUNT)
                main_page.element_click(locator=MainPageObject.TABLE_HEADER_AMOUNT)
                self.eyes.match_level  = "exact"
                self.eyes.check_region(region=MainPageObject.TABLE, tag=("Table Sort Test V"  + str(APP_VERSION)))
            finally:
                self.eyes.close()

        ''' Run table sort test function'''
        try: table_sort()
        except Exception: self.AssertionErrors.append(str("Difference Detected when table is sorted"))


    def test_Canvas_Chart_Test(self):
        '''Set up test functions'''
        def canvas_chart_month(month, region_area):
            '''Check canvas chart months'''
            try:
                chart_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Canvas Chart test - " + str(month), self.VIEWPORT)
                self.driver.get(self.CHART_URL)
                self.eyes.match_level  = "strict"
                self.eyes.check_region(region=region_area, tag=(str(month) + " - Initial Canvas Chart Test V"  + str(APP_VERSION)))
                chart_page.element_click(locator=ChartPageObject.ADD_DATA_SET_BUTTON)
                self.eyes.check_region(region=region_area, tag=(str(month) + " - Data Added Canvas Chart Test V"  + str(APP_VERSION)))
            finally:
                self.eyes.close()

        def canvas_chart_all():
            '''Check whole window with canvas chart'''
            try:
                chart_page = pages.CommonClass(self.driver)
                self.eyes.open(self.driver, "Hackathon", "Canvas Chart test - All", self.VIEWPORT)
                self.driver.get(self.CHART_URL)
                self.eyes.match_level  = "strict"
                self.eyes.check_window(tag=("All - Initial Canvas Chart Test V"  + str(APP_VERSION)))
                self.assertTrue(chart_page.has_expected_element_on_page(locator=ChartPageObject.ADD_DATA_SET_BUTTON), "Cannot find expected element --> " + str(ChartPageObject.ADD_DATA_SET_BUTTON[1]))
                chart_page.element_click(locator=ChartPageObject.ADD_DATA_SET_BUTTON)
                self.eyes.check_window(tag=("All - Data Added Canvas Chart Test V"  + str(APP_VERSION)))
            finally:
                self.eyes.close()

        ''' Run table canvas chart functions'''
        try: canvas_chart_all()
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - All" + str(e)))
        try: canvas_chart_month("January", self.JAN_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - January" + str(e)))
        try: canvas_chart_month("February", self.FEB_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - February" + str(e)))
        try: canvas_chart_month("March", self.MAR_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - March" + str(e)))
        try: canvas_chart_month("April", self.APR_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - April" + str(e)))
        try: canvas_chart_month("May", self.MAY_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - May" + str(e)))
        try: canvas_chart_month("June", self.JUN_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - June" + str(e)))
        try: canvas_chart_month("July", self.JUL_CHART)
        except Exception as e: self.AssertionErrors.append(str("Difference Detected in canvas chart - July" + str(e)))


    def test_Dynamic_Content_Test(self):
        '''Check canvas chart months'''
        try:
            self.eyes.open(self.driver, "Hackathon", "Canvas Chart test - ", self.VIEWPORT)
            self.driver.get(self.MAIN_WITH_ADS_URL)
            self.eyes.match_level  = "layout"
            self.eyes.check_region(region=self.AD_1, tag="Advert 1 - Dynamic Content Test V"  + str(APP_VERSION))
            self.eyes.check_region(region=self.AD_2, tag="Advert 2 - Dynamic Content Test V"  + str(APP_VERSION))
        finally:
            self.eyes.close()


    def tearDown(self):
        self.eyes.abort()
        self.driver.close()
        '''Get test name'''
        testname = (self.id().rsplit('.', -1)[2])
        '''Create console out put for issues found'''
        msg = str("\n--------------------------------\nTHE FOLLOWING ISSUES WERE FOUND RUNNING " + testname.upper() + "\n\n" + ('\n'.join(str(e) for e in self.AssertionErrors) + "\n\nEND OF "  + testname.upper() + " ISSUES\n--------------------------------\n"))
        '''Check if there were any issues found and if so print them to the console'''
        self.assertTrue([] == self.AssertionErrors, msg)


'''Run everything, output HTML report to Reports folder in current working directory'''
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.\\results'))
