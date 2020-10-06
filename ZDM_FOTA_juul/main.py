################################################################################
# Zerynth Device Manager
#
# Created by Zerynth Team 2020 CC
# Authors: E.Neri, D.Neri
###############################################################################

from bsp.drivers import eth
import streams
from zdm import zdm


def fota_callback(fw_version):
    # This function is called in order to let the user define if the fota process can be accepted.
    # The parameter is the new firmware version that is going to be installed.
    # If it returns True the FOTA is accepted.
    # If it returns False the FOTA is refused.
    print("Fota callback called with firmware version: ", fw_version)
    return True


streams.serial()
print("hello")

try:
    print("##################################")
    print("##################################")

    eth.init()
    print("Connecting to eth...")
    interface = eth.interface()
    
    print("Connect eth done")


    # Create a ZDM Device instance and define the fota callback. The default fota callback function returns always True.
    device = zdm.Device(fota_callback=fota_callback)
    device.connect()

    while True:
        print("Waiting fota update ...")
        sleep(2000)

except Exception as e:
    print("main", e)
