# -*- coding: utf-8 -*-
from model.postaldata import Postaldata
import pytest
import random
import string


def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#counry_list[]
#[Postaldata(country="Algeria", name="Jhon Travolta", street="Shev4enka str", num_house="12", city="Drogobych",state="Lviv reg", zip=12300, phone="0978339274")] +

testdata = [Postaldata(country="Ukraine", name=rand_str("name", 20), street=rand_str("street", 20),
                            num_house=rand_str("num", 20), city=rand_str("city", 20), state=rand_str("state", 20),
                            zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 20)) for i in range(25)]

@pytest.mark.parametrize("postaldata", testdata, ids=[repr(x) for x in testdata])
def test_add_req_user_data(app, postaldata):
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    app.postaldata.create_user_data(postaldata)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert len(old_postaldata_list) + 1 == len(new_postaldata_list)
    postaldata_index = app.postaldata.get_postaldata_index_by_postaldata(postaldata, new_postaldata_list)
    assert postaldata == new_postaldata_list[postaldata_index]
    new_postaldata_list.pop(postaldata_index)
    old_sorted_list = sorted(old_postaldata_list, key=Postaldata.sort_param)
    new_sorted_list = sorted(new_postaldata_list, key=Postaldata.sort_param)
    assert old_sorted_list == new_sorted_list




#def test_add_all_user_data(app):
    #old_postaldata_list = app.postaldata.count_postal_data_object_list()
    #app.postaldata.create_user_data(Postaldata(country="Ukraine", name="Ilyk Stepan", street="Lazarenka str", num_house="23", city="Lviv", state="Lviv reg", zip="82100", phone="0938211673", sec_code="93317", address_det="lvivska"))
    #new_postaldata_list = app.postaldata.count_postal_data_object_list()
    #assert len(old_postaldata_list) + 1 == len(new_postaldata_list)
    #new_postaldata_list = new_postaldata_list[:-1]
    #assert old_postaldata_list == new_postaldata_list