from model.postaldata import Postaldata
from random import randrange
import pytest
import random
import string

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Postaldata(country="Ukraine", name=rand_str("name", 5), street=rand_str("street", 5), num_house=rand_str("num", 5), city=rand_str("city", 5), state=rand_str("state", 5), zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 5)) for i in range(5)]


@pytest.mark.parametrize('execution_number', range(1,8))
def test_del_some_user_data(app, execution_number):
    app.postaldata.make_postaldata_quantity(execution_number, Postaldata(country="Ukraine", name=rand_str("name", 8),
                                                       street=rand_str("street", 8), num_house=rand_str("num", 8), city=rand_str("city", 8),
                                                       state=rand_str("state", 8), zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 8)))
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    index_postal_data = randrange(0, len(old_postaldata_list), 1)
    deleted_postaldata = old_postaldata_list[index_postal_data]
    app.postaldata.delete_user_data_by_index(index_postal_data)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert len(old_postaldata_list) == len(new_postaldata_list) + 1
    old_postaldata_list[index_postal_data:index_postal_data+1] = []
    assert old_postaldata_list == new_postaldata_list
    #assert (deleted_postaldata in new_postaldata_list) == False