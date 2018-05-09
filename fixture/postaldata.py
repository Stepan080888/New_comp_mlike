from selenium.webdriver.support.ui import Select
from model.postaldata import Postaldata
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PostaldataHelper:
    def __init__(self, app):
        self.app = app

    def create_user_data(self, postaldata):
        self.open_profile_page()
        self.open_address_page()
        self.open_user_data_form()
        self.fill_in_user_data_form(postaldata)
        self.list_objects_cash = None

    def fill_in_user_data_form(self, postaldata):
        wd = self.app.wd
        wd.find_element_by_name("rcrs-country").click()
        Select(wd.find_element_by_name("rcrs-country")).select_by_visible_text(postaldata.country)
        wd.find_element_by_xpath("//option[@value='Ukraine']").click()
        self.check_inputs_for_none(postaldata.name, xpath_1=1, xpath_2="input[1]")
        self.check_inputs_for_none(postaldata.street, xpath_1=1, xpath_2="input[2]")
        self.check_inputs_for_none(postaldata.num_house, xpath_1=1, xpath_2="input[3]")
        self.check_inputs_for_none(postaldata.city, xpath_1=1, xpath_2="input[4]")
        self.check_inputs_for_none(postaldata.state, xpath_1=2, xpath_2="input[1]")
        self.check_inputs_for_none(postaldata.zip, xpath_1=2, xpath_2="input[2]")
        self.check_inputs_for_none(postaldata.phone, xpath_1=2, xpath_2="input[3]")
        self.check_inputs_for_none(postaldata.sec_code, xpath_1=2, xpath_2="input[4]")
        self.check_inputs_for_none(postaldata.sec_code, xpath_1=2, xpath_2="textarea")
        wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[2]/textarea").click()
        wd.find_element_by_xpath("//button[@value='Submit']").click()

    def check_inputs_for_none(self, input_data, xpath_1=None, xpath_2=None):
        wd = self.app.wd
        if input_data is not None:
            wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[" + str(xpath_1) + "]/" + xpath_2).click()
            wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[" + str(xpath_1) + "]/" + xpath_2).clear()
            wd.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[3]/form/div[" + str(xpath_1) + "]/" + xpath_2).send_keys(input_data)

    def open_user_data_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[3]/div/div/span").click()

    def open_address_page(self):
        wd = self.app.wd
        #if wd.current_url.endswith("/addresses") and len(wd.find_elements_by_class_name("single-address-container")) > 0:
            #return
        element_address = WebDriverWait(wd, 20).until(lambda wd: wd.find_element_by_class_name("addresses"))
        element_address.click()
        #wd.find_element_by_class_name("addresses").click()

    def open_profile_page(self):
        wd = self.app.wd
        time.sleep(5)
        element_profile = WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='User']")))
        element_profile.click()
        if len(wd.find_elements_by_class_name("link-to-steam")) == 0:
            wd.get("http://stagingskinstock.gamingdev.io/profile")

    def delete_user_data_by_index(self, index):
        wd = self.app.wd
        self.open_profile_page()
        self.open_address_page()
        user_action_class = wd.find_elements_by_class_name("users-actions-section")[index]
        user_action_class.find_element_by_xpath("span[3]").click()
        self.list_objects_cash = None

    def delete_first_user_data(self):
        """unnecessary method"""
        self.delete_user_data_by_index(0)

    def modify_postaldata_street_by_index(self, postaldata, index):
        self.open_profile_page()
        self.open_address_page()
        self.open_edit_window_by_index(index)
        self.fill_in_user_data_form(postaldata)
        self.list_objects_cash = None

    def modify_first_postaldata_street(self):
        """unnecessary method"""
        self.modify_postaldata_street_by_index(Postaldata(country="Ukraine", street="Lazarenka str newnew new new"), 0)

    def open_edit_window_by_index(self, index):
        wd = self.app.wd
        user_action_class = wd.find_elements_by_class_name("users-actions-section")[index]
        user_action_class.find_element_by_xpath("span[1]").click()

    def count_user_data(self):
        wd = self.app.wd
        self.open_profile_page()
        self.open_address_page()
        return len(wd.find_elements_by_class_name("users-actions-section"))

    list_objects_cash = None

    def count_postal_data_object_list(self):
        if self.list_objects_cash is None:
            wd = self.app.wd
            self.open_profile_page()
            self.open_address_page()
            self.list_objects_cash = []
            k = wd.find_elements_by_xpath("//div[contains(@class,'single-address-container')]")
            global user_data
            for user_data in k[1:len(k)]:
                if user_data.find_element_by_xpath("div[1]").text == "DEFAULT":
                    self.list_objects_cash.append(self.if_default_postal_data(2))
                else:
                    self.list_objects_cash.append(self.if_default_postal_data(1))
        return list(self.list_objects_cash)

    def split_string_by_comma(self, string_value, number_string):
        return string_value.split(",")[number_string].strip()

    def split_phone_number(self, string_value, number_string):
        return string_value.split(": ")[number_string].strip()

    def if_default_postal_data(self, number_div):
        name = user_data.find_element_by_xpath("div[" + str(number_div) + "]").text
        street = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 1) + "]").text, 1)
        num_house = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 1) + "]").text, 0)
        city = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 2) + "]").text, 0)
        state = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 2) + "]").text, 1)
        zip = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 2) + "]").text, 2)
        country = self.split_string_by_comma(user_data.find_element_by_xpath("div[" + str(number_div + 3) + "]").text, 0)
        phone = self.split_phone_number(user_data.find_element_by_xpath("div[" + str(number_div + 4) + "]").text, 1)
        return Postaldata(name=name, street=street, num_house=num_house, city=city, state=state, zip=zip, country=country, phone=phone)

    def get_postaldata_index_by_postaldata(self, postaldata, postaldatalist):
        index_postaldata = postaldatalist.index(postaldata)
        return index_postaldata


