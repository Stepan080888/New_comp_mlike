from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.postaldata import PostaldataHelper
from fixture.carthelper import CartHelper
from fixture.checkouthelper import CheckoutHelper
#from fixture.producthelper import ProductHelper

class Application:
    def __init__(self, browser, baseurl):
        if browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r'C:\Users\admin\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        elif browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.wd.maximize_window()
        self.session = SessionHelper(self)
        self.postaldata = PostaldataHelper(self)
        self.cart = CartHelper(self)
        self.checkout = CheckoutHelper(self)
        #self.product = ProductHelper(self)
        self.baseurl = baseurl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        #element_cart = WebDriverWait(wd, 20).until(lambda wd: wd.find_element_by_link_text("Cart"))
        #element_cart.click()
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()
