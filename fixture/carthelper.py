from selenium.webdriver.support.ui import Select
from model.product import Product
from selenium.webdriver.support.ui import WebDriverWait
import time


class CartHelper:
    def __init__(self, app):
        self.app = app

    def open_product_page(self, product_number):
        wd = self.app.wd
        href = "/product/" + str(product_number)
        try:
            wd.find_element_by_css_selector("a[href=" + "'" + href + "'" + "]").click()
        except:
            wd.get("http://stagingskinstock.gamingdev.io" + href)

    def select_quantity_of_product(self, quantity):
        wd = self.app.wd
        wd.find_element_by_tag_name("select").click()
        Select(wd.find_element_by_tag_name("select")).select_by_visible_text(str(quantity))
        time.sleep(1)

    def click_add_to_cart_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name("add-to-cart").click()

    def add_to_cart_product(self, product_number, quantity):
        self.app.open_home_page()
        self.open_product_page(product_number)
        self.select_quantity_of_product(quantity)
        self.list_shold_add_to_cart = self.get_product_object_from_product_page()
        self.click_add_to_cart_button()
        return list(self.list_shold_add_to_cart)

    def open_cart_page(self):
        wd = self.app.wd
        element_cart = WebDriverWait(wd, 20).until(lambda wd: wd.find_element_by_link_text("Cart"))
        element_cart.click()
        #wd.find_element_by_link_text("Cart").click()

    list_of_products_by_one = None

    def add_fractional_part(self):
        wd = self.app.wd
        price_product = wd.find_element_by_class_name("product-price").text
        if "." not in price_product:
            price_product = price_product + ".00"
        return price_product

    def get_product_object_from_product_page(self):
        wd = self.app.wd
        if self.list_of_products_by_one is None or self.list_of_products_by_one == []:
            self.list_of_products_by_one = []
        #self.open_product_page(23)
        product_name = wd.find_element_by_class_name("product-name").get_attribute("textContent")
        product_price = self.add_fractional_part()
        product_quantity = wd.find_element_by_tag_name("select").get_attribute("value")
        self.list_of_products_by_one.append(Product(name=product_name, price=product_price, quantity=product_quantity))
        return list(self.list_of_products_by_one)

    def get_product_object_from_cart_page(self):
        wd = self.app.wd
        self.list_in_cart = []
        for product_row in wd.find_elements_by_class_name("cart-product-row"):
            product_name = product_row.find_element_by_class_name('cart-product-text').find_element_by_tag_name("div").text
            product_price = product_row.find_element_by_class_name('cart-product-price').text
            product_quantity = product_row.find_element_by_tag_name("select").get_attribute("value")
            self.list_in_cart.append(Product(name=product_name, price=product_price, quantity=product_quantity))
        #self.list_of_products_by_one = []
        return list(self.list_in_cart)

    def remove_products_from_cart(self):
        wd = self.app.wd
        self.open_cart_page()
        self.list_of_products_by_one = []
        list_items_in_the_cart = wd.find_elements_by_class_name("cart-product")
        for product_row in range(len(list_items_in_the_cart)):
            wd.find_element_by_class_name("cart-item-actions").find_element_by_xpath("span[1]").click()
            time.sleep(1)
        return True

    def get_price_all_product_from_car(self):
        wd = self.app.wd
        self.open_cart_page()
        return float(wd.find_element_by_tag_name('em').text[1:])