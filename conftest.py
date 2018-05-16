import pytest
from fixture.application import Application
import json

fixture = None
target = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    global target
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        if target is None:
            with open(request.config.getoption("--target")) as config_file:
                target = json.load(config_file)
                print(target)
        #baseurl = request.config.getoption("--baseurl")
        fixture = Application(browser=browser, baseurl=target['baseurl'])
    fixture.session.ensure_log_in(username=target['username'], password=target['password'])
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

#py.test test\test add_user_data.py
#py.test --browser=chrome test\test_add_user_data.py