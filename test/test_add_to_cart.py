# -*- coding: utf-8 -*-
import pytest
from model.product import Product
from data.data_product import a as execution_number

@pytest.mark.parametrize('execution_number', range(1,8))
def test_add_to_cart_product(app, execution_number):
    app.cart.remove_products_from_cart()
    for i in range(execution_number):
        list_product_should_be_in_cart = app.cart.add_to_cart_product(i, i+25)
    app.cart.open_cart_page()
    object_from_cart = app.cart.get_product_object_from_cart_page()
    assert len(object_from_cart) == len(list_product_should_be_in_cart)
    assert sorted(object_from_cart, key=Product.sort_param_product_quantity) == sorted(list_product_should_be_in_cart, key=Product.sort_param_product_quantity)
    result_amount_from_cart = round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in object_from_cart]), 2)
    result_amount_count_during_adding = round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in list_product_should_be_in_cart]), 2)
    assert result_amount_from_cart == result_amount_count_during_adding
    assert result_amount_count_during_adding == app.cart.get_price_all_product_from_car()

