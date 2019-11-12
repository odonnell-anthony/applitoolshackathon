from selenium.webdriver.common.by import By


class URLS(object):
    #-------------------------------------Version 1-----------------------------------------#
    URL                         = ("http://demo.applitools.com/hackathon.html")
    LOGO_SRC                    = ("http://demo.applitools.com/img/logo-big.png")
    TWITTER_ICON_SRC            = ("http://demo.applitools.com/img/social-icons/twitter.png")
    FACEBOOK_ICON_SRC           = ("http://demo.applitools.com/img/social-icons/facebook.png")
    LINKEDIN_ICON_SRC           = ("http://demo.applitools.com/img/social-icons/linkedin.png")
    MAIN                        = ("http://demo.applitools.com/hackathonApp.html")
    CHART                       = ("http://demo.applitools.com/hackathonChart.html")
    MAIN_WITH_ADS               = ("http://demo.applitools.com/hackathonApp.html?showAd=true")
    ADVERT_1                    = ("http://demo.applitools.com/img/flashSale.gif")
    ADVERT_2                    = ("http://demo.applitools.com/img/flashSale2.gif")
    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    URL_V2                      = ("http://demo.applitools.com/hackathonV2.html")
    LOGO_SRC_V2                 = ("http://demo.applitools.com/img/logo-big.png")
    TWITTER_ICON_SRC_V2         = ("http://demo.applitools.com/img/social-icons/twitter.png")
    FACEBOOK_ICON_SRC_V2        = ("http://demo.applitools.com/img/social-icons/facebook.png")
    LINKEDIN_ICON_SRC_V2        = ("http://demo.applitools.com/img/social-icons/linkedin.png")
    MAIN_V2                     = ("http://demo.applitools.com/hackathonAppV2.html")
    CHART_V2                    = ("http://demo.applitools.com/hackathonChartV2.html")
    MAIN_WITH_ADS_V2            = ("http://demo.applitools.com/hackathonAppV2.html?showAd=true")
    ADVERT_1_V2                 = ("http://demo.applitools.com/img/flashSale.gif")
    ADVERT_2_V2                 = ("http://demo.applitools.com/img/flaseSale3.gif")
    #---------------------------------------------------------------------------------------#


class LogInPageObject(object):
    #-------------------------------------Version 1-----------------------------------------#
    LOGO                        = (By.XPATH, '//div[@class="logo-w"]/a/img')
    HEADER                      = (By.CLASS_NAME, "auth-header")
    USERNAME_LABEL              = (By.XPATH, "//form[1]/div[1]/label")
    USERNAME_ICON               = (By.CLASS_NAME, "os-icon-user-male-circle")
    USERNAME_INPUT              = (By.ID, "username")
    PASSWORD_LABEL              = (By.XPATH, "//form[1]/div[2]/label")
    PASSWORD_ICON               = (By.CLASS_NAME, "os-icon-fingerprint")
    PASSWORD_INPUT              = (By.ID, "password")
    LOGIN_BUTTON                = (By.ID, "log-in")
    REMEMBER_ME_LABEL           = (By.XPATH, "//div[3]/div[1]/label")
    REMEMBER_ME_CHECKBOX        = (By.XPATH, "//div[3]/div[1]/label/input")
    TWITTER_ICON                = (By.XPATH, "//div[@class='buttons-w']/div[2]/a[1]/img[1]")
    FACEBOOK_ICON               = (By.XPATH, "//div[@class='buttons-w']/div[2]/a[2]/img[1]")
    LINKEDIN_ICON               = (By.XPATH, "//div[@class='buttons-w']/div[2]/a[3]/img[1]")
    ALERT                       = (By.CLASS_NAME, "alert-warning")

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    LOGO_V2                     = (By.XPATH, '//div[@class="logo-w"]/a/img')
    HEADER_V2                   = (By.CLASS_NAME, "auth-header")
    USERNAME_LABEL_V2           = (By.XPATH, "//form[1]/div[1]/label")
    USERNAME_ICON_V2            = (By.CLASS_NAME, "os-icon-user-male-circle")
    USERNAME_INPUT_V2           = (By.ID, "username")
    PASSWORD_LABEL_V2           = (By.XPATH, "//form[1]/div[2]/label")
    PASSWORD_ICON_V2            = (By.CLASS_NAME, "os-icon-fingerprint")
    PASSWORD_INPUT_V2           = (By.ID, "password")
    LOGIN_BUTTON_V2             = (By.XPATH, '//div[@class="buttons-w"]/button')
    REMEMBER_ME_LABEL_V2        = (By.XPATH, "//div[3]/div[1]/label")
    REMEMBER_ME_CHECKBOX_V2     = (By.XPATH, "//div[3]/div[1]/label/input")
    TWITTER_ICON_V2             = (By.XPATH, "//div[@class='buttons-w']/div[2]/span[1]/img")
    FACEBOOK_ICON_V2            = (By.XPATH, "//div[@class='buttons-w']/div[2]/span[2]/img")
    LINKEDIN_ICON_V2            = (By.XPATH, "//div[@class='buttons-w']/div[2]/a[3]/img[1]")
    ALERT_V2                    = (By.CLASS_NAME, "alert-warning")

    #---------------------------------------------------------------------------------------#


class LogInPageText(object):
    #-------------------------------------Version 1-----------------------------------------#
    TITLE                       = "ACME demo app"
    HEADER                      = "Login Form"
    USERNAME_LABEL              = "Username"
    PASSWORD_LABEL              = "Password"
    REMEMBER_ME_LABEL           = "Remember Me"
    LOGIN_BUTTON                = "Log In"
    ALERT_NO_CREDS              = "Both Username and Password must be present"
    ALERT_NO_PASSWORD           = "Password must be present"
    ALERT_NO_USERNAME           = "Username must be present"

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    TITLE_V2                    = "ACME demo app"
    HEADER_V2                   = "Logout Form"
    USERNAME_LABEL_V2           = "Username"
    PASSWORD_LABEL_V2           = "Pwd"
    REMEMBER_ME_LABEL_V2        = "Remember Me"
    LOGIN_BUTTON_V2             = "Log In"
    ALERT_NO_CREDS_V2           = "Please enter both username and password"
    ALERT_NO_USERNAME_V2        = "Username must be present"

    #---------------------------------------------------------------------------------------#


class MainPageObject(object):
    #-------------------------------------Version 1-----------------------------------------#
    AVATAR_TOP_RIGHT            = (By.CLASS_NAME, 'logged-user-w')
    TABLE                       = (By.CLASS_NAME, "table-responsive")
    TABLE_HEADER_AMOUNT         = (By.ID, "amount")
    COMPARE_EXPENSES_LINK       = (By.ID, "showExpensesChart")
    ADVERT_1                    = (By.ID, "flashSale")
    ADVERT_1_IMG                = (By.XPATH, "//div[@id='flashSale']//img")
    ADVERT_2                    = (By.ID, "flashSale2")
    ADVERT_2_IMG                = (By.XPATH, "//div[@id='flashSale2']//img")

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    AVATAR_TOP_RIGHT_V2         = (By.CLASS_NAME, 'logged-user-w')
    TABLE_V2                    = (By.ID, "transactionsTable")
    TABLE_HEADER_AMOUNT_V2      = (By.ID, "amount")
    COMPARE_EXPENSES_LINK_V2    = (By.ID, "showExpensesChart")
    ADVERT_1_V2                 = (By.ID, "flashSale")
    ADVERT_1_IMG_V2             = (By.XPATH, "//div[@id='flashSale']//img")
    ADVERT_2_V2                 = (By.ID, "flashSale2")
    ADVERT_2_IMG_V2             = (By.XPATH, "//div[@id='flashSale2']//img")

    #---------------------------------------------------------------------------------------#


class MainPageText(object):
    #-------------------------------------Version 1-----------------------------------------#
    COMPARE_EXPENSES            = "Compare Expenses"

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    COMPARE_EXPENSES_V2         = "Compare Expenses"

    #---------------------------------------------------------------------------------------#

class ChartPageObject(object):
    #-------------------------------------Version 1-----------------------------------------#
    ADD_DATA_SET_BUTTON         = (By.ID, "addDataset")

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    ADD_DATA_SET_BUTTON_V2      = (By.ID, "addDataset")

    #---------------------------------------------------------------------------------------#


class ChartPageText(object):
    #-------------------------------------Version 1-----------------------------------------#
    ADD_DATA_SET                = ("Show data for next year")

    #---------------------------------------------------------------------------------------#


    #-------------------------------------Version 2-----------------------------------------#
    ADD_DATA_SET_V2             = ("Show data for next year")

    #---------------------------------------------------------------------------------------#