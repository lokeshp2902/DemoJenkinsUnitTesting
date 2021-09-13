import pytest

def pytest_addoption(parser):
    parser.addoption("--PALLADIUM_CONFIG", action="store")

@pytest.fixture
def PALLADIUM_CONFIG(request):
    return request.config.getoption("--PALLADIUM_CONFIG")