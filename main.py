import logging_config          
from banc import DeviceSimule, ConnexionSimulee, Driver
from error_config import CommandInvalidError
 
device = DeviceSimule()
connexion = ConnexionSimulee(device)
driver = Driver(connexion)
 
driver.regler_tension(3.3)
print("Tension lue :", driver.lire_tension())

try:
    driver._dialoguer("REBOOT")
except CommandInvalidError as e:
    print("Exception attrapee :", e)