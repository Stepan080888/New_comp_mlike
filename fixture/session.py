from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait

class SessionHelper:
    def __init__(self, app):
        self.app = app


    def log_in(self, username, password):
        wd = self.app.wd
        wd.find_element_by_class_name("sign-in-title").click()
        WebDriverWait(wd, 10).until(lambda wd: wd.find_element_by_class_name('steam-button')).click()
        self.ensure_steam_log_in(username, password)

    def ensure_log_in(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        if len(wd.find_elements_by_class_name("under_dropdown")) == 0:
            self.log_in(username, password)

    def ensure_steam_log_in(self, username, password):
        wd = self.app.wd
        if len(wd.find_elements_by_class_name("OpenID_UserContainer")) > 0:
            wd.find_element_by_class_name("btn_green_white_innerfade").click()
        else:
            wd.find_element_by_id("steamAccountName").click()
            wd.find_element_by_id("steamAccountName").clear()
            wd.find_element_by_id("steamAccountName").send_keys(username)
            wd.find_element_by_id("steamPassword").click()
            wd.find_element_by_id("steamPassword").clear()
            wd.find_element_by_id("steamPassword").send_keys(password)
            wd.find_element_by_id("imageLogin").click()

    def log_out(self):
        wd = self.app.wd
        log_out_drop_down = wd.find_element_by_xpath("//*[@id='root']/div/header/div/div/div[4]/div/div/span/div")
        hover = ActionChains(wd).move_to_element(log_out_drop_down)
        hover.perform()
        wd.find_element_by_class_name("dropdown-item").click()
        wd.find_element_by_class_name("sign-in-title").click()
        self.ensure_steam_logout()
        time.sleep(5)

    def ensure_log_out(self):
        wd = self.app.wd
        if len(wd.find_elements_by_class_name("under_dropdown")) > 0:
            self.log_out()

    def ensure_steam_logout(self):
        wd = self.app.wd
        if len(wd.find_elements_by_class_name("OpenID_UserContainer")) > 0:
            wd.find_element_by_link_text("Not You?").click()



    def clearstorage(self):
        wd = self.app.wd
        wd.execute_script("window.localStorage.clear();")
