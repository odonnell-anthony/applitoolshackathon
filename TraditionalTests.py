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



class TraditionalTestsV1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(1024, 768)
        self.AssertionErrors = []


    def test_Login_Page_UI_Elements_V1(self):
        '''Check login page UI Elements'''

        '''Visit V1'''
        self.driver.get(locators.URLS.URL)

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
        except Exception: self.AssertionErrors.append(str("Cannot find expected TWITTER_ICON element"))

        '''Twitter icon source is as expected'''
        if (self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.TWITTER_ICON))):
            try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.TWITTER_ICON, src=URLS.TWITTER_ICON_SRC))
            except Exception: self.AssertionErrors.append(str("TWITTER_ICON source is not as expected"))

        '''Check for Facebook icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.FACEBOOK_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected FACEBOOK_ICON element"))

        '''Facebook icon source is as expected'''
        if (self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.FACEBOOK_ICON))):
            try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.FACEBOOK_ICON, src=URLS.FACEBOOK_ICON_SRC))
            except Exception: self.AssertionErrors.append(str("FACEBOOK_ICON source is not as expected"))


        '''Check for LinkedIn icon'''
        try: self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LINKEDIN_ICON))
        except Exception: self.AssertionErrors.append(str("Cannot find expected LINKEDIN_ICON element"))

        '''LinkedIn icon source is as expected'''
        if (self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LINKEDIN_ICON))):
            try: self.assertTrue(login_page.element_has_correct_src(locator=LogInPageObject.LINKEDIN_ICON, src=URLS.LINKEDIN_ICON_SRC))
            except Exception: self.AssertionErrors.append(str("LINKEDIN_ICON source is not as expected"))


    def test_Data_Driven_Test_V1(self):
        '''If you don’t enter the username and password and click the login button, it should throw an error'''
        '''Visit V1'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE),\
            "Login page title doesn't match expected --> " + str(LogInPageText.TITLE))

        '''Check For Login button'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON),\
            "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))

        ''''Click Login button'''
        login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)

        '''Check For Alert'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.ALERT),\
            "Cannot find Alert --> " + str(LogInPageObject.ALERT[1]))

        '''Check Alert Text - NO CREDENTIALS'''
        self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_CREDS),\
            "Alert text with no credentials supplied not as expected --> " + str(LogInPageText.ALERT_NO_CREDS))

        '''If you only enter the username and click the login button, it should throw an error'''
        '''Visit V1'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE),\
            "Login page title doesn't match expected --> " + str(LogInPageText.TITLE))

        '''Check For Username input'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT),\
            "Cannot find Username input --> " + str(LogInPageObject.USERNAME_INPUT[1]))

        '''Input Username'''
        login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")

        '''Check For Login button'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.LOGIN_BUTTON),\
            "Cannot find Login button --> " + str(LogInPageObject.LOGIN_BUTTON[1]))

        ''''Click Login button'''
        login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)

        '''Check For Alert'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.ALERT),\
            "Cannot find Alert --> " + str(LogInPageObject.ALERT[1]))

        '''Check Alert Text - ONLY USERNAME'''
        self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_PASSWORD),\
            "Alert text with only username supplied not as expected --> " + str(LogInPageText.ALERT_NO_PASSWORD))

        '''If you only enter the password and click the login button, it should throw an error'''
        '''Visit V1'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE),\
            "Login page title doesn't match expected --> " + str(LogInPageText.TITLE))

        '''Check For Password input'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT),\
            "Cannot find Password input --> " + str(LogInPageObject.PASSWORD_INPUT[1]))

        '''Input Password'''
        login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")

        ''''Click Login button'''
        login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)

        '''Check Alert Text - ONLY PASSWORD'''
        self.assertTrue(login_page.element_has_correct_text(locator=LogInPageObject.ALERT, text=LogInPageText.ALERT_NO_USERNAME),\
            "Alert text with only password supplied not as expected --> " + str(LogInPageText.ALERT_NO_USERNAME))

        '''If you enter both username (any value) and password (any value), it should log you in.'''
        '''Visit V1'''
        self.driver.get(locators.URLS.URL)

        '''Set CommonClass as login_page'''
        login_page = pages.CommonClass(self.driver)

        '''Login page title as expected'''
        self.assertTrue(login_page.title_is_as_expected(text=LogInPageText.TITLE),\
            "Login page title doesn't match expected --> " + str(LogInPageText.TITLE))

        '''Check For Username input'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.USERNAME_INPUT),\
            "Cannot find Username input --> " + str(LogInPageObject.USERNAME_INPUT[1]))

        '''Input Username'''
        login_page.element_input_text(locator=LogInPageObject.USERNAME_INPUT, input="anthony")

        '''Check For Password input'''
        self.assertTrue(login_page.has_expected_element_on_page(locator=LogInPageObject.PASSWORD_INPUT),\
            "Cannot find Password input --> " + str(LogInPageObject.PASSWORD_INPUT[1]))

        '''Input Password'''
        login_page.element_input_text(locator=LogInPageObject.PASSWORD_INPUT, input="password")

        ''''Click Login button'''
        login_page.element_click(locator=LogInPageObject.LOGIN_BUTTON)

        '''Set CommonClass as main_page'''
        main_page = pages.CommonClass(self.driver)

        '''Check For main page avatar'''
        self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.AVATAR_TOP_RIGHT),\
            "Cannot find expected element --> " + str(MainPageObject.AVATAR_TOP_RIGHT[1]))


    def test_Table_Sort_V1(self):
        '''Table sort test'''

        '''Visit V1 Main page'''
        self.driver.get(locators.URLS.MAIN)

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
        self.assertTrue(str(table_as_expected) == str(table_on_page))

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
        self.assertTrue(str(table_as_expected_sorted) == str(table_on_page_sorted))


    def test_Canvas_Chart_Test_V1(self):
        '''Canvas Chart test'''

        '''Visit V1 Charts'''
        self.driver.get(locators.URLS.CHART)

        '''Set CommonClass as chart_page'''
        chart_page = pages.CommonClass(self.driver)

        '''Get Chart data for first year'''
        year_1 = (self.driver.execute_script("return window.barChartData.datasets[0].label"))
        months = (self.driver.execute_script("return window.barChartData.labels"))
        data_1 = (self.driver.execute_script("return window.barChartData.datasets[0].data"))

        '''Check Month labels are as expected'''
        expected_months= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        self.assertTrue(months == expected_months)

        '''Check Year as expected for first year'''
        expected_year_1 = "2017"
        self.assertTrue(str(year_1) == str(expected_year_1))

        '''Check data is as expected for first year'''
        expected_data_1 = [10, 20, 30, 40, 50, 60, 70]
        self.assertTrue(expected_data_1 == data_1)

        '''Get Chart data for second year'''
        year_2 = (self.driver.execute_script("return window.barChartData.datasets[1].label"))
        data_2 = (self.driver.execute_script("return window.barChartData.datasets[1].data"))

        '''Check Year as expected for second year'''
        expected_year_2 = "2018"
        self.assertTrue(str(year_2) == str(expected_year_2))

        '''Check data is as expected for second year'''
        expected_data_2 = [8, 9, -10, 10, 40, 60, 40]
        self.assertTrue(expected_data_2 == data_2)

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
        self.assertTrue(str(year_3) == str(expected_year_3))

        '''Check data is as expected for third year'''
        expected_data_3 = [5, 10, 15, 20, 25, 30, 35]
        self.assertTrue(expected_data_3 == data_3)

    def test_Dynamic_Content_test(self):
        '''Dynamic Content test'''

        '''Visit V1 Main'''
        self.driver.get(locators.URLS.MAIN_WITH_ADS)

        '''Set CommonClass as main page'''
        main_page = pages.CommonClass(self.driver)

        '''Check for advert element'''
        self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.ADVERT_1),\
            "Cannot find expected advert element --> " + str(MainPageObject.ADVERT_1[1]))

        '''Check for second advert element'''
        self.assertTrue(main_page.has_expected_element_on_page(locator=MainPageObject.ADVERT_2),\
            "Cannot find expected advert element --> " + str(MainPageObject.ADVERT_2[1]))

        '''Get first adverts source'''
        ad_1_src = self.driver.find_element_by_xpath(MainPageObject.ADVERT_1_IMG[1]).get_attribute("src")
        self.assertTrue(ad_1_src == URLS.ADVERT_1)

        '''Get second adverts source'''
        ad_2_src = self.driver.find_element_by_xpath(MainPageObject.ADVERT_2_IMG[1]).get_attribute("src")
        '''Check second adverts source'''
        self.assertTrue(ad_2_src == URLS.ADVERT_2)


    def tearDown(self):
        self.driver.close()
        testname = (self.id().rsplit('.', -1)[2])
        msg = str("\n--------------------------------\nTHE FOLLOWING ISSUES WERE FOUND RUNNING " + testname.upper() + "\n\n" + ('\n'.join(str(e) for e in self.AssertionErrors) + "\n\nEND OF "  + testname.upper() + " ISSUES\n--------------------------------\n"))
        self.assertTrue([] == self.AssertionErrors, msg)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.\\results'))
