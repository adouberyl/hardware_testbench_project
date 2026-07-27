import pytest
from banc import ConnexionSimulee, Driver, DeviceSimule

@pytest.fixture
def connexion():
    return ConnexionSimulee(DeviceSimule())

@pytest.fixture
def driver(connexion):
    return Driver(connexion)