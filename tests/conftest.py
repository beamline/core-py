import pytest
from beamline.web.Beamline import *


@pytest.fixture(scope='module')
def test_client():
    flask_app = Beamline.app

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


def pytest_configure():
    pytest.miner_id = ''
