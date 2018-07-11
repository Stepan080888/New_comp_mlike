from fixture.carthelper import CartHelper
from selenium.common.exceptions import NoSuchElementException
from model.product import Product
from data.data_postal_data import data_for_creation_postaldata_in_smoke_test as postaldata
from model.postaldata import Postaldata



class CheckoutHelper(CartHelper):
    def __init__(self, app):
        self.app = app

    def add_product_to_checkout_page(self):
        wd = self.app.wd
        self.open_cart_page()
        wd.find_element_by_class_name("checkout-btn").click()
        #self.open_cart_page()

    def get_order_total_from_chackout(self, number):
        wd = self.app.wd
        return float(wd.find_elements_by_class_name("total-price")[number].text[1:].replace(",", ""))

    def click_change_buttons(self, number):
        wd = self.app.wd
        wd.find_elements_by_class_name('change-checkout-block-details')[number].click()

    def press_use_this_payment_method(self):
        wd = self.app.wd
        wd.find_element_by_class_name('set-selected-address').click()

    def change_payment_method_to_steam(self): #TEMPORARY METHOD TO PREVENT TEST FAIL
        wd = self.app.wd
        self.click_change_buttons(1)
        self.press_use_this_payment_method()

    def check_existant_default_payment_method(self):
        wd = self.app.wd
        try:
            wd.find_element_by_class_name('steam-balance')
            return True
        except NoSuchElementException:
            print("NO DEFAULT PAYMENT METHOD")
            return False

    def press_place_order_button(self, number):
        wd = self.app.wd
        wd.find_elements_by_class_name('active-button')[number].click()

    def add_fractional_part(self, text):
        if "." not in text:
            text = text + ".00"
        text = text.replace(",", "")
        return text

    def get_list_product_objects_from_checkout(self):
        wd = self.app.wd
        product_list_on_checkout = []
        for product_item in wd.find_elements_by_class_name('checkout-product-item'):
            product_name = product_item.find_element_by_class_name('product-name').text
            product_price = self.add_fractional_part(product_item.find_element_by_class_name('product-price').text[1:])
            product_quantity = int(product_item.find_element_by_tag_name("select").get_attribute("value"))
            product_list_on_checkout.append(Product(name=product_name, price=product_price, quantity=product_quantity))
        self.list_of_products_by_one = []
        return product_list_on_checkout

    def check_the_existent_shipping_inf(self):
        wd = self.app.wd
        if len(wd.find_elements_by_class_name('message-for-user')) > 0:
            print("SHIPPING INFORMATION DOES NOT EXIST. WE START CREATION")
            self.add_postal_data_from_checkout()
        if len(wd.find_elements_by_class_name('shipping-address')) > 0:
            print("SHIPPING INFORMATION EXISTS")

    def add_postal_data_from_checkout(self):
        wd = self.app.wd
        wd.find_element_by_class_name('button-add-address').click()
        self.app.postaldata.open_user_data_form()
        self.app.postaldata.fill_in_user_data_form(postaldata)
        wd.execute_script("window.history.go(-1)")
        self.check_the_existent_shipping_inf()

    def check_enough_bal(self, db):
        wd = self.app.wd
        user_balance = float(wd.find_element_by_class_name('amount').text[1:])
        order_total_amount = self.get_order_total_from_chackout(0)
        if order_total_amount * 5 != user_balance:
            k = db.users.find({"steamId": "76561198824314514"})
            #db.users.update({ $set: {'balance': '120'} })
            for i in k:
                print(i['balance'])



