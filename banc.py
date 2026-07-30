import logging

from error_config import CommandInvalidError, ReturnInvalidError

logger = logging.getLogger(__name__)


class ConnexionSimulee:
    def __init__(self, device):
        self._canal = ""
        self._device = device

    def envoyer(self, info):
        logger.debug("Commande envoyee : %s", info)
        self._canal = self._device.traitement(info)

    def recevoir(self):
        return self._canal


class Driver:
    def __init__(self, connexion):
        self._connexion = connexion      # composition

    def _dialoguer(self, commande):
        self._connexion.envoyer(commande)
        reponse = self._connexion.recevoir()
        if reponse == "ERR":
            logger.error("Commande rejetee par le device : %s", commande)
            raise CommandInvalidError(f"Commande rejetee : {commande!r}")
        return reponse

    def regler_tension(self, v):
        logger.info("Tension reglee a %s V", v)
        self._dialoguer(f"SET V {v}")

    def lire_tension(self):
        reponse = self._dialoguer("GET V")
        try:
            return float(reponse)
        except ValueError as e:
            raise ReturnInvalidError(
                f"La reponse envoyee n'est pas une valeur numerique : {reponse!r}"
            ) from e


class DeviceSimule:
    def __init__(self):
        self._consigne = 0
        self._mesure = 0

    def traitement(self, commande):
        if commande.startswith("SET V "):
            valeur = float(commande[len("SET V "):])
            self._consigne = valeur
            self._mesure = valeur
            return "OK"
        elif commande == "GET V":
            return str(self._mesure)
        elif commande == "STATUS":
            return "READY"
        else:
            return "ERR"