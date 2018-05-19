# -*- coding: utf-8 -*-
from model.postaldata import Postaldata
import pytest
from data.data_postal_data import testdata2 as testdata






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


