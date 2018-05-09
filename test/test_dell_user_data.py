from model.postaldata import Postaldata
from random import randrange

def test_del_some_user_data(app):
    if app.postaldata.count_user_data() == 0:
        app.postaldata.create_user_data(Postaldata(country="Ukraine", name="Ilyk Stepan", street="Lazarenka str", num_house="23", city="Lviv", state="Lviv reg", zip="82100", phone="0938211673"))
    old_postaldata_list = app.postaldata.count_postal_data_object_list()
    index_postal_data = randrange(0, len(old_postaldata_list), 1)
    app.postaldata.delete_user_data_by_index(index_postal_data)
    new_postaldata_list = app.postaldata.count_postal_data_object_list()
    assert len(old_postaldata_list) == len(new_postaldata_list) + 1
    old_postaldata_list[index_postal_data:index_postal_data+1] = []
    assert old_postaldata_list == new_postaldata_list