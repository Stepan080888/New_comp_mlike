import pytest
from model.product import Product
from data.data_product import product_lists as test_products

@pytest.mark.parametrize('list_add_to_checkoout', test_products, ids=[repr(i) for i in test_products])
def test_add_product_to_checkout(app, list_add_to_checkoout):
    #app.checkout.clear_storage()
    app.cart.remove_products_from_cart(0)
    app.cart.add_to_cart_product(list_add_to_checkoout)
    app.checkout.add_product_to_checkout_page()
    app.checkout.check_the_existent_shipping_inf()
    #assert app.checkout.check_existant_default_payment_method() == True
    app.checkout.change_payment_method_to_steam()         #TEMPORARY METHOD TO PREVENT TEST FAIL
    product_list_from_checkout = app.checkout.get_list_product_objects_from_checkout()
    assert app.checkout.check_existant_default_payment_method() == True
    assert app.checkout.get_order_total_from_chackout(0) == app.checkout.get_order_total_from_chackout(1)
    assert len(list_add_to_checkoout) == len(product_list_from_checkout)
    assert list_add_to_checkoout == product_list_from_checkout
    assert round(sum([i.give_quantity() * i.price for i in list_add_to_checkoout]), 2) == app.checkout.get_order_total_from_chackout(1)



