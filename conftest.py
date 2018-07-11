import pytest
from fixture.application import Application
import json
import os.path
from pymongo import MongoClient
from fixture.db import DbFixture

fixture = None
target_main = None
target_db = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    global target_main
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        if target_main is None:
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
            with open(config_file) as f:
                target_main = json.load(f)
                print("1 ", target_main)
        #baseurl = request.config.getoption("--baseurl")
        fixture = Application(browser=browser, baseurl=target_main['web']['baseurl'])
    fixture.session.ensure_log_in(username=target_main['web']['username'], password=target_main['web']['password'])
    return fixture

@pytest.fixture(scope="session", autouse="True")
def stop(request):
    def fin():
        fixture.session.ensure_log_out()
        fixture.destroy()
    request.addfinalizer(fin)
    #return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    #parser.addoption("--baseurl", action="store", default="http://stagingskinstock.gamingdev.io")


@pytest.fixture(scope="session")
def db(request):
    global target_db
    if target_db is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target_db = json.load(f)
            print("2 ", target_db)
    dbfixture = MongoClient('192.168.12.203', 27018).shopdb
    #dbfixture = DbFixture(host=target_db['db']['host'], port=target_db['db']['port'], database=target_db['db']['database'])
    print(dbfixture)
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


#py.test test\test add_user_data.py
#py.test --browser=chrome test\test_add_user_data.py