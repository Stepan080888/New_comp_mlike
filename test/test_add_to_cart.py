# -*- coding: utf-8 -*-
import pytest
from model.product import Product
from data.data_product import product_lists as test_products

@pytest.mark.parametrize('list_add_to_cart', test_products,  ids=[repr(x) for x in test_products])
def test_add_to_cart_product(app, list_add_to_cart):
    app.cart.remove_products_from_cart(0)
    app.cart.add_to_cart_product(list_add_to_cart)
    app.cart.open_cart_page()
    object_from_cart = app.cart.get_product_object_from_cart_page()
    assert len(object_from_cart) == len(list_add_to_cart)
    assert object_from_cart == list_add_to_cart
    assert sorted(object_from_cart, key=Product.sort_param_product_quantity) == sorted(list_add_to_cart, key=Product.sort_param_product_quantity)
    result_amount_from_cart = round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in object_from_cart]), 2)
    result_amount_count_during_adding = round(sum([i.give_quantity() * i.price for i in list_add_to_cart]), 2)
    assert result_amount_from_cart == result_amount_count_during_adding
    assert result_amount_count_during_adding == app.cart.get_price_all_product_from_car()

