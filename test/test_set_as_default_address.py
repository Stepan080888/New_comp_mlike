from fixture.postaldata import Postaldata
import pytest
import random
import string

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])




@pytest.mark.parametrize("number_postaldata", range(2,10))
def test_set_as_default(app, number_postaldata):
    app.postaldata.make_postaldata_quantity(number_postaldata, Postaldata(country="Ukraine", name=rand_str("name", 8), street=rand_str("street", 8),
                                                        num_house=rand_str("num", 8), city=rand_str("city", 8),
                                                        state=rand_str("state", 8), zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 8)))
    if not app.postaldata.check_the_first_one_is_default(1):
        app.postaldata.set_as_default_postaldata_by_index(0)
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    index_to_set_default = random.randint(1, len(old_postaldata_list)-1)
    app.postaldata.set_as_default_postaldata_by_index(index_to_set_default)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert sorted(old_postaldata_list, key=Postaldata.sort_param) == sorted(new_postaldata_list, key=Postaldata.sort_param)
    assert app.postaldata.check_the_first_one_is_default(1)
    assert old_postaldata_list[index_to_set_default] == new_postaldata_list[0]
