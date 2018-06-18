class Product:
    def __init__(self, name, price, quantity, id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = id

    def __repr__(self):
        return "%s : %s : %s :  %s" % (self.id, self.name, self.price, self.quantity)

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity and self.price == other.price

    def sort_param_product_quantity(self):
        return int(self.quantity)

    def give_price_deleted_dolar_in_front(self):
        return float(self.price[1:])

    def give_quantity(self):
        return int(self.quantity)