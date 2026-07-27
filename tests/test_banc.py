import pytest

@pytest.mark.parametrize("tension", [3.3, 0.0, 5.0, 12.0, 99999, -1.2])

def test_regler_puis_lire_tension(driver, tension):

    driver.regler_tension(tension)
    assert driver.lire_tension() == tension

    
def test_status_renvoie_ready(connexion):

    connexion.envoyer("STATUS")
    assert connexion.recevoir() == "READY"

def test_set_renvoie_ok(connexion):

    connexion.envoyer("SET V 3.3")
    assert connexion.recevoir() == "OK"

def test_inc_renvoie_ERR(connexion):

    connexion.envoyer("test")
    assert connexion.recevoir()== "ERR"

def test_cas_d_erreur(connexion):

    connexion.envoyer("BERYL")
    with pytest.raises(ValueError):float(connexion.recevoir())