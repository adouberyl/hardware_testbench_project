import pytest
from banc import DeviceSimule, ConnexionSimulee, Driver

def test_regler_puis_lire_tension_1():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)
    driver = Driver(connexion)

    driver.regler_tension(3.3)
    assert driver.lire_tension()==3.3


def test_regler_puis_lire_tension_2():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)
    driver = Driver(connexion)

    driver.regler_tension(5.0)
    assert driver.lire_tension()==5.0


def test_regler_puis_lire_tension_3():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)
    driver = Driver(connexion)

    driver.regler_tension(0.0)
    assert driver.lire_tension()==0.0


def test_regler_puis_lire_tension_4():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)
    driver = Driver(connexion)

    driver.regler_tension(12.0)
    assert driver.lire_tension()==12.0

    
def test_status_renvoie_ready():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)

    connexion.envoyer("STATUS")
    assert connexion.recevoir() == "READY"

def test_set_renvoie_ok():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)

    connexion.envoyer("SET V 3.3")
    assert connexion.recevoir() == "OK"

def test_inc_renvoie_ERR():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)

    connexion.envoyer("test")
    assert connexion.recevoir()== "ERR"

def test_cas_d_erreur():
    device = DeviceSimule()
    connexion = ConnexionSimulee(device)
    driver = Driver(connexion)

    connexion.envoyer("BERYL")
    with pytest.raises(ValueError):float(connexion.recevoir())