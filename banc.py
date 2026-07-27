class ConnexionSimulee:
    def __init__(self, device):
        self._canal = ""
        self._device = device

    def envoyer(self, info):
        self._canal = self._device.traitement(info)

    def recevoir(self):
        return self._canal



class Driver:
    def __init__(self, connexion):
        self._connexion = connexion      # composition

    def regler_tension(self, v):
        self._connexion.envoyer(f"SET V {v}")

    def lire_tension(self):
        self._connexion.envoyer("GET V")
        reponse = self._connexion.recevoir()
        return float(reponse)
    
class DeviceSimule :
    def __init__(self):
        self._consigne = 0
        self._mesure = 0

    def traitement (self, commande):
        if commande.startswith("SET V "):
            valeur = float(commande[len("SET V "):])
            self._consigne = valeur
            self._mesure = valeur    
            return "OK"
        
        elif commande == "GET V":
            return str(self._mesure)
        
        elif commande =="STATUS":
            return "READY"
        
        else :
            return "ERR"