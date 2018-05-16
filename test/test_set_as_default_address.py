from fixture.postaldata import Postaldata
import pytest
import random
import string

def rand_str(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])




@pytest.mark.parametrize("number_postaldata", range(3,10))
def test_set_as_default(app, number_postaldata):
    while app.postaldata.count_user_data() < number_postaldata:
        app.postaldata.create_user_data(Postaldata(country="Ukraine", name=rand_str("name", 5), street=rand_str("street", 5), num_house=rand_str("num", 5), city=rand_str("city", 5), state=rand_str("state", 5), zip=int(random.randint(10000, 99000)), phone=rand_str("phone", 5)))
    if not app.postaldata.check_the_first_one_is_default(1):
        app.postaldata.set_as_default_postaldata_by_index(0)
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    index_to_set_default = random.randint(1, len(old_postaldata_list)-1)
    app.postaldata.set_as_default_postaldata_by_index(index_to_set_default)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert sorted(old_postaldata_list, key=Postaldata.sort_param) == sorted(new_postaldata_list, key=Postaldata.sort_param)
    assert app.postaldata.check_the_first_one_is_default(1)
    assert old_postaldata_list[index_to_set_default] == new_postaldata_list[0]
