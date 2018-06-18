from model.postaldata import Postaldata
from random import randrange
from data.data_postal_data import testdata2 as testdata
import pytest
import random
import string

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

@pytest.mark.parametrize("postaldata", testdata, ids=[repr(x) for x in testdata])
def test_modify_first_user_data(app, postaldata):
    app.postaldata.make_postaldata_quantity(5, Postaldata(country="Ukraine", name=rand_str("name", 8), street=rand_str("street", 8),
                                                                          num_house=rand_str("num", 8), city=rand_str("city", 8), state=rand_str("state", 8),
                                                                          zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 8)))
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    index_postal_data = randrange(0, len(old_postaldata_list), 1)
    new_postaldata = postaldata
    app.postaldata.modify_postaldata_street_by_index(new_postaldata, index_postal_data)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert len(old_postaldata_list) == len(new_postaldata_list)
    assert new_postaldata in new_postaldata_list
    #assert old_postaldata_list[index_postal_data] in new_postaldata_list == False