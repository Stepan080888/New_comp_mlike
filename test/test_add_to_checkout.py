import pytest
from model.product import Product


@pytest.mark.parametrize('execution_number', range(1, 16))
def test_add_product_to_checkout(app, execution_number):
    #app.checkout.clear_storage()
    app.cart.remove_products_from_cart()
    for i in range(execution_number):
        list_product_should_be_in_cart = app.cart.add_to_cart_product(i, i+25)
    app.checkout.add_product_to_checkout_page()
    app.checkout.check_the_existent_shipping_inf()
    #assert app.checkout.check_existant_default_payment_method() == True
    app.checkout.change_payment_method_to_steam()         #TEMPORARY METHOD TO PREVENT TEST FAIL
    product_list_from_checkout = app.checkout.get_list_product_objects_from_checkout()
    assert app.checkout.get_order_total_from_chackout(0) == app.checkout.get_order_total_from_chackout(1)
    assert len(list_product_should_be_in_cart) == len(product_list_from_checkout)
    assert list_product_should_be_in_cart == product_list_from_checkout
    assert round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in list_product_should_be_in_cart]), 2) == app.checkout.get_order_total_from_chackout(1)
    #assert app.checkout.check_existant_default_payment_method() == True


    """
    object2 = app.cart.get_product_object_from_cart_page()
    assert len(object2) == len(list_product_should_be_in_cart)
    assert sorted(object2, key=Product.sort_param_product_quantity) == sorted(list_product_should_be_in_cart,key=Product.sort_param_product_quantity)
    result = round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in object2]), 2)
    res = round(sum([i.give_quantity() * i.give_price_deleted_dolar_in_front() for i in object2]), 2)
    assert result == res
    assert res == app.cart.get_price_all_product_from_car()
    """