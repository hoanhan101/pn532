#
# api.py contains a set of core functions
#

import smbus

from pn532.register import *

class PN532(object):
    def __init__(self):
        # i2c device address
        self.address = PN532_DEFAULT_ADDRESS

        # smbus object
        self.bus = smbus.SMBus(1)
