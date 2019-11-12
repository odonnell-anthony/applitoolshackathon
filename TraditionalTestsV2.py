import unittest
import os
import pandas
import pages
import locators
import HtmlTestRunner
from selenium import webdriver
from locators import (LogInPageObject,
                        URLS,
                        LogInPageText,
                        MainPageObject,
                        MainPageText,
                        ChartPageObject,
                        ChartPageText)


class TraditionalTestsV2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(1024, 768)
        self.AssertionErrors = []


    def test_Login_Page_UI_Elements_V2(self):
        '''Check login page UI Elements'''

        '''Visit V2'''
        self.driver.get(locators.URLS.URL_V2)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        try: self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE))
        except Exception: self.AssertionErrors.append(str("Login page title doesn't match expected"))


        '''Logo is on page'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGO))
        except Exception: self.AssertionErrors.append(str("Cannot find expected LOGO element"))

        '''Logo Source is as expected'''
        if (self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGO))):
            try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.LOGO, src=URLS.LOGO_SRC))
            except Exception: self.AssertionErrors.append(str("LOGO source is not as expected"))


        ''''Check for Header'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.HEADER))
        except Exception: self.AssertionErrors.append(str("Cannot find expected HEADER element"))


        ''''Check Header text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.HEADER, text=LogInPageText.HEADER))
        except Exception: self.AssertionErrors.append(str("HEADER text not as expected"))


        '''Check For Username label'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_LABEL))
        except Exception: self.AssertionErrors.append(str("Cannot find expected USERNAME_LABEL element"))
        except: pass

        '''Check Username label text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.USERNAME_LABEL, text=LogInPageText.USERNAME_LABEL))
        except Exception: self.AssertionErrors.append(str("USERNAME_LABEL text not as expected"))
        except: pass

        '''Check Username icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected USERNAME_ICON element"))

        '''Check For Username input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT))
        except Exception: self.AssertionErrors.append(str("Cannot find expected USERNAME_INPUT element"))

        '''Check For Password label'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_LABEL))
        except Exception: self.AssertionErrors.append(str("Cannot find expected PASSWORD_LABEL element"))

        '''Check Password label text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.PASSWORD_LABEL, text=LogInPageText.PASSWORD_LABEL))
        except Exception: self.AssertionErrors.append(str("PASSWORD_LABEL text not as expected"))

        '''Check Password icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected PASSWORD_ICON element"))

        '''Check For Password input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT))
        except Exception: self.AssertionErrors.append(str("Cannot find expected PASSWORD_INPUT element"))

        '''Check For Login button'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected LOGIN_BUTTON element"))

        '''Check Login button text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.LOGIN_BUTTON, text=LogInPageText.LOGIN_BUTTON))
        except Exception: self.AssertionErrors.append(str("LOGIN_BUTTON text not as expected"))

        '''Check For Remember Me label'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.REMEMBER_ME_LABEL))
        except Exception: self.AssertionErrors.append(str("Cannot find expected REMEMBER_ME_LABEL element"))

        '''Check Remember Me label text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.REMEMBER_ME_LABEL, text=LogInPageText.REMEMBER_ME_LABEL))
        except Exception: self.AssertionErrors.append(str("REMEMBER_ME_LABEL text not as expected"))

        '''Check for Remember Me checkbox and that it is not selected'''
        try: self.assertFalse(login_page.element_is_selected(locator=LogInPageObject.REMEMBER_ME_CHECKBOX))
        except Exception: self.AssertionErrors.append(str("Cannot find expected REMEMBER_ME_CHECKBOX element"))

        '''Check for Twitter icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.TWITTER_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected TWITTER_ICON_LINK element"))

        '''Twitter icon source is as expected'''
        try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.TWITTER_ICON, src=URLS.TWITTER_ICON_SRC))
        except Exception: self.AssertionErrors.append(str("TWITTER_ICON source is not as expected or not found"))

        '''Check for Facebook icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.FACEBOOK_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected FACEBOOK_ICON_LINK element"))

        '''Facebook icon source is as expected'''
        try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.FACEBOOK_ICON, src=URLS.FACEBOOK_ICON_SRC))
        except Exception: self.AssertionErrors.append(str("FACEBOOK_ICON source is not as expected or not found"))


        '''Check for LinkedIn icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LINKEDIN_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected LINKEDIN_ICON_LINK element"))

        '''LinkedIn icon source is as expected'''
        try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.LINKEDIN_ICON, src=URLS.LINKEDIN_ICON_SRC))
        except Exception: self.AssertionErrors.append(str("LINKEDIN_ICON source is not as expected or not found"))


    def test_Data_Driven_Test_V2(self):
        '''If you don’t enter the username and password and click the login button, it should throw an error'''

        '''Visit V2'''
        self.driver.get(locators.URLS.URL_V2)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        try: self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE))
        except Exception: self.AssertionErrors.append(str("NO CREDENTIALS - Login page title doesn't match expected"))

        '''Check For Login button'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON))
        except Exception: self.AssertionErrors.append(str("NO CREDENTIALS - Cannot find expected LOGIN_BUTTON element"))

        ''''Click Login button'''
        try: login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
        except Exception: self.AssertionErrors.append(str("NO CREDENTIALS - Failed to click LOGIN_BUTTON"))

        '''Check For Alert'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.ALERT))
        except Exception: self.AssertionErrors.append(str("NO CREDENTIALS - Cannot find expected ALERT element"))

        '''Check Alert Text - NO CREDENTIALS'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_CREDS))
        except Exception: self.AssertionErrors.append(str("NO CREDENTIALS - ALERT text not as expected or not found"))

        '''Check Alert size - NO CREDENTIALS'''
        try:
            alert = self.driver.find_element_by_class_name(LogInPageObject.ALERT)
            self.assertTrue(alert == {'height': 49, 'width': 450})
        except Exception:
            self.AssertionErrors.append(str("NO CREDENTIALS - ALERT element is the wrong size"))


        '''If you only enter the username and click the login button, it should throw an error'''

        '''Visit V2'''
        self.driver.get(locators.URLS.URL_V2)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        try: self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE))
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Login page title doesn't match expected"))

        '''Check For Username input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT))
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Cannot find expected USERNAME_INPUT element"))

        '''Input Username'''
        try: login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Failed to input text in USERNAME_INPUT element"))

        '''Check For Login button'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON))
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Cannot find expected LOGIN_BUTTON element"))

        ''''Click Login button'''
        try: login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Failed to click LOGIN_BUTTON"))

        '''Check For Alert'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.ALERT))
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - Cannot find expected ALERT element"))

        '''Check Alert Text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_PASSWORD))
        except Exception: self.AssertionErrors.append(str("ONLY USERNAME - ALERT text not as expected or not found"))

        '''Check Alert Size'''
        try:
            alert = self.driver.find_element_by_class_name(LogInPageObject.ALERT)
            self.assertTrue(alert == {'height': 49, 'width': 450})
        except Exception:
            self.AssertionErrors.append(str("ONLY USERNAME - ALERT element is the wrong size"))


        '''If you only enter the password and click the login button, it should throw an error'''

        '''Visit V2'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        try: self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE))
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - Login page title doesn't match expected"))

        '''Check For Password input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT))
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - Cannot find expected PASSWORD_INPUT element"))

        '''Input Password'''
        try: login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - Failed to input text in PASSWORD_INPUT element"))

        '''Check For Login button'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON))
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - Cannot find expected LOGIN_BUTTON element"))

        ''''Click Login button'''
        try: login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - Failed to click LOGIN_BUTTON"))

        '''Check For Alert'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.ALERT))
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD- Cannot find expected ALERT element"))

        '''Check Alert Text'''
        try: self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_USERNAME))
        except Exception: self.AssertionErrors.append(str("ONLY PASSWORD - ALERT text not as expected or not found"))

        '''Check Alert Size'''
        try:
            alert = self.driver.find_element_by_class_name(LogInPageObject.ALERT)
            self.assertTrue(alert == {'height': 49, 'width': 450})
        except Exception:
            self.AssertionErrors.append(str("ONLY PASSWORD - ALERT element is the wrong size"))


        '''If you enter both username (any value) and password (any value), it should log you in.'''

        '''Visit V2'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        try: self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE))
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Login page title doesn't match expected"))

        '''Check For Username input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT))
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Cannot find expected USERNAME_INPUT element"))

        '''Input Username'''
        try: login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Failed to input text in USERNAME_INPUT element"))

        '''Check For Password input'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT))
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Cannot find expected PASSWORD_INPUT element"))

        '''Input Password'''
        try: login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN- Failed to input text in PASSWORD_INPUT element"))

        ''''Click Login button'''
        try: login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Failed to click LOGIN_BUTTON"))

        '''Set CommonClass as main_page'''
        main_page = pages.CommonClass(self.driver)

        '''Check For main page avatar'''
        try: self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.AVATAR_TOP_RIGHT))
        except Exception: self.AssertionErrors.append(str("CREDS GIVEN - Failed to Login (cannot find avatar)"))


    def test_Table_Sort_V2(self):
        '''Table sort test'''

        '''Visit V2 Main page'''
        self.driver.get(locators.URLS.MAIN_V2)

        '''Set CommonClass as login_page'''
        main_page = pages.CommonClass(self.driver)

        '''Check for table'''
        self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.TABLE),\
            "Cannot find expected element --> " + str(MainPageObject.TABLE[1]))

        '''Get table HTML for first visit'''
        table_html = main_page.element_get_html(locator=MainPageObject.TABLE),\
            "Cannot find expected element --> " + str(MainPageObject.TABLE[1])

        '''Read table from page in to dataframe'''
        table_dataframe  = pandas.read_html(str(table_html[0]), header =0, flavor = 'bs4')
        table_on_page = table_dataframe[0]

        '''Set expectation for table on first visit'''
        tabledata = [
                    ['Complete',     'Today1:52am',         'Starbucks coffee',             'Restaurant / Cafe',    '+ 1,250.00 USD'],
                    ['Declined',     'Jan 19th3:22pm',      'Stripe Payment Processing',    'Finance',              '+ 952.23 USD'],
                    ['Pending',      'Yesterday7:45am',     'MailChimp Services',           'Software',             '- 320.00 USD'],
                    ['Pending',      'Jan 23rd2:7pm',       'Shopify product',              'Shopping',             '+ 17.99 USD'],
                    ['Complete',     'Jan 7th9:51am',       'Ebay Marketplace',             'Ecommerce',            '- 244.00 USD'],
                    ['Pending',      'Jan 9th7:45pm',       'Templates Inc',                'Business',             '+ 340.00 USD']
                    ]
        table_as_expected = pandas.DataFrame(tabledata, columns = ['Status','Date','Description','Category','Amount'])

        '''Confirm table is as expected'''
        try: self.assertTrue(str(table_as_expected) == str(table_on_page))
        except Exception: self.AssertionErrors.append(str("Table data not as expected on visit"))

        '''Click Amount header twice to sort ascending'''
        main_page.element_click(locator=MainPageObject.TABLE_HEADER_AMOUNT)
        main_page.element_click(locator=MainPageObject.TABLE_HEADER_AMOUNT)

        '''Get sorted table HTML'''
        table_html = main_page.element_get_html(locator=MainPageObject.TABLE),\
            "Cannot find expected element --> " + str(MainPageObject.TABLE[1])
        '''Read table from page in to dataframe'''
        table_dataframe_sorted  = pandas.read_html(str(table_html[0]), header =0, flavor = 'bs4')
        table_on_page_sorted  = table_dataframe_sorted [0]

        '''Set expectation for table sorted by amount'''
        tabledata_sorted  = [
                    ['Complete',     'Today1:52am',         'Starbucks coffee',             'Restaurant / Cafe',    '+ 1,250.00 USD'],
                    ['Declined',     'Jan 19th3:22pm',      'Stripe Payment Processing',    'Finance',              '+ 952.23 USD'],
                    ['Pending',      'Jan 9th7:45pm',       'Templates Inc',                'Business',             '+ 340.00 USD'],
                    ['Pending',      'Jan 23rd2:7pm',       'Shopify product',              'Shopping',             '+ 17.99 USD'],
                    ['Complete',     'Jan 7th9:51am',       'Ebay Marketplace',             'Ecommerce',            '- 244.00 USD'],
                    ['Pending',      'Yesterday7:45am',     'MailChimp Services',           'Software',             '- 320.00 USD']
                    ]
        table_as_expected_sorted  = pandas.DataFrame(tabledata_sorted , columns = ['Status','Date','Description','Category','Amount'])

        '''Confirm sorted table is as expected'''
        try: self.assertTrue(str(table_as_expected_sorted) == str(table_on_page_sorted))
        except Exception: self.AssertionErrors.append(str("Table data not as expected when sorted by Amount"))


    def test_Canvas_Chart_Test_V2(self):
        '''Canvas Chart test'''

        '''Visit V2 Charts'''
        self.driver.get(locators.URLS.CHART_V2)

        '''Set CommonClass as chart_page'''
        chart_page = pages.CommonClass(self.driver)

        '''Get Chart data for first year'''
        year_1 = (self.driver.execute_script("return window.barChartData.datasets[0].label"))
        months = (self.driver.execute_script("return window.barChartData.labels"))
        data_1 = (self.driver.execute_script("return window.barChartData.datasets[0].data"))

        '''Check Month labels are as expected'''
        expected_months= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        try: self.assertTrue(months == expected_months)
        except Exception: self.AssertionErrors.append(str("Canvas Chart months are not as expected"))

        '''Check Year as expected for first year'''
        expected_year_1 = "2017"
        try: self.assertTrue(str(year_1) == str(expected_year_1))
        except Exception: self.AssertionErrors.append(str("Canvas Chart first year is not as expected"))

        '''Check data is as expected for first year'''
        expected_data_1 = [10, 20, 30, 40, 50, 60, 70]
        try: self.assertTrue(expected_data_1 == data_1)
        except Exception: self.AssertionErrors.append(str("Canvas Chart first year data is not as expected"))

        '''Get Chart data for second year'''
        year_2 = (self.driver.execute_script("return window.barChartData.datasets[1].label"))
        data_2 = (self.driver.execute_script("return window.barChartData.datasets[1].data"))

        '''Check Year as expected for second year'''
        expected_year_2 = "2018"
        try: self.assertTrue(str(year_2) == str(expected_year_2))
        except Exception: self.AssertionErrors.append(str("Canvas Chart second year is not as expected"))

        '''Check data is as expected for second year'''
        expected_data_2 = [8, 9, -10, 10, 40, 60, 40]
        try: self.assertTrue(expected_data_2 == data_2)
        except Exception: self.AssertionErrors.append(str("Canvas Chart second year data is not as expected"))

        '''Check for show data for new year button'''
        self.assertTrue(chart_page.has_expected_element_on_page(locator=ChartPageObject.ADD_DATA_SET_BUTTON),\
            "Cannot find expected element --> " + str(ChartPageObject.ADD_DATA_SET_BUTTON[1]))

        '''Check show data for new year button text'''
        self.assertTrue(chart_page.element_has_correct_text(locator=ChartPageObject.ADD_DATA_SET_BUTTON, text=ChartPageText.ADD_DATA_SET),\
            "Show data for new year button text not as expected --> " + str(ChartPageText.ADD_DATA_SET))

        '''Click button to add new data'''
        chart_page.element_click(locator=ChartPageObject.ADD_DATA_SET_BUTTON)

        '''Get Chart data for third year'''
        year_3 = (self.driver.execute_script("return window.barChartData.datasets[2].label"))
        data_3 = (self.driver.execute_script("return window.barChartData.datasets[2].data"))

        '''Check Year as expected for third year'''
        expected_year_3 = "2019"
        try: self.assertTrue(str(year_3) == str(expected_year_3))
        except Exception: self.AssertionErrors.append(str("Canvas Chart second year is not as expected"))

        '''Check data is as expected for third year'''
        expected_data_3 = [5, 10, 15, 20, 25, 30, 35]
        try: self.assertTrue(expected_data_3 == data_3)
        except Exception: self.AssertionErrors.append(str("Canvas Chart second year data is not as expected"))

    def test_Dynamic_Content_test_V2(self):
        '''Dynamic Content test'''

        '''Visit V2 Main'''
        self.driver.get(locators.URLS.MAIN_WITH_ADS_V2)

        '''Set CommonClass as main page'''
        main_page = pages.CommonClass(self.driver)

        '''Check for advert element'''
        try: self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.ADVERT_1))
        except Exception: self.AssertionErrors.append(str("ADVERT_1 element not found"))

        '''Check for second advert element'''
        try: self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.ADVERT_2))
        except Exception: self.AssertionErrors.append(str("ADVERT_2 element not found"))


        '''Get first adverts source'''
        try: ad_1_src = self.driver.find_element_by_xpath(MainPageObject.ADVERT_1_IMG[1]).get_attribute("src")
        except Exception: self.AssertionErrors.append(str("ADVERT_1_IMG not found"))
        '''Check first adverts source'''
        try: self.assertTrue(ad_1_src == URLS.ADVERT_1)
        except Exception: self.AssertionErrors.append(str("ADVERT_1 source not as expected or not found"))

        '''Get second adverts source'''
        try: ad_2_src = self.driver.find_element_by_xpath(MainPageObject.ADVERT_2_IMG[1]).get_attribute("src")
        except Exception: self.AssertionErrors.append(str("ADVERT_2 source not found"))
        '''Check second adverts source'''
        try: self.assertTrue(ad_2_src == URLS.ADVERT_2 or ad_2_src == URLS.ADVERT_2_V2)
        except Exception: self.AssertionErrors.append(str("ADVERT_2 source not as expected or not found"))


    def tearDown(self):
        self.driver.close()
        testname = (self.id().rsplit('.', -1)[2])
        msg = str("\n--------------------------------\nTHE FOLLOWING ISSUES WERE FOUND RUNNING " + testname.upper() + "\n\n" + ('\n'.join(str(e) for e in self.AssertionErrors) + "\n\nEND OF "  + testname.upper() + " ISSUES\n--------------------------------\n"))
        self.assertTrue([] == self.AssertionErrors, msg)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.\\results'))
