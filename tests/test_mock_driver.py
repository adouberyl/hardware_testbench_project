from unittest.mock import Mock
from banc import Driver

def test_regler_puis_lire_tension_mock():
    fausse_connexion = Mock()
    fausse_connexion.recevoir.return_value = 3.3

    driver = Driver(fausse_connexion)
    assert driver.lire_tension() == 3.3

    fausse_connexion.envoyer.assert_called_with("GET V")