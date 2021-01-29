import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--log_file", action="store", default="log.txt", help="Return log file name"
    )


@pytest.fixture
def log_file(request):
    return request.config.getoption("--log_file")
