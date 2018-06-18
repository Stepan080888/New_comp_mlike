class ProductHelper:
    def __init__(self, app):
        self.app = app

    def get_product_data(self):
        wd = self.app.wd
        wd.find_element_by_class_name("product-name").text()
        wd.find_element_by_class_name("product-price").text()