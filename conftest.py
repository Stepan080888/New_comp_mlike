import pytest
from fixture.application import Application

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        baseurl = request.config.getoption("--baseurl")
        fixture = Application(browser=browser, baseurl=baseurl)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_log_in(username="no_exp2", password="Keplercode344")
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
    parser.addoption("--baseurl", action="store", default="http://stagingskinstock.gamingdev.io")