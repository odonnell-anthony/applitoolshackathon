from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

class CommonClass(Base):

    def title_is_as_expected(self, text):
        '''Returns expected page title'''
        return (text) in self.driver.title


    def has_expected_element_on_page(self, locator):
        '''Attempts to find expected element on page'''
        element = self.driver.find_element(*locator)
        return (element)


    def element_has_correct_src(self, locator, src):
        '''Check element source attribute agaisnt provided source'''
        element_src = self.driver.find_element(*locator).get_attribute("src") == src
        return (element_src)


    def element_has_correct_text(self, locator, text):
        '''Check element has expected text content'''
        element_txt = self.driver.find_element(*locator).text == text
        return (element_txt)


    def element_is_selected(self, locator):
        '''Check element is selected'''
        element_selected = self.driver.find_element(*locator).is_selected()
        return (element_selected)


    def element_click(self, locator):
        '''Click Element'''
        element_click = self.driver.find_element(*locator).click()
        return (element_click)


    def element_clear(self, locator):
        '''Clear Element'''
        element_clear = self.driver.find_element(*locator).clear()
        return (element_clear)


    def element_input_text(self, locator, input):
        '''Input text to element'''
        element_input_text = self.driver.find_element(*locator).send_keys(input)
        return (element_input_text)

    def element_get_html(self, locator):
        '''Input text to element'''
        element_html = self.driver.find_element(*locator).get_attribute('innerHTML')
        return (element_html)







