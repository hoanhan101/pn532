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

    def write_byte(self, reg, data):
        self.bus.write_byte_data(self.address, reg, data)

    def read_byte(self, reg):
        read = self.bus.read_byte_data(self.address, reg)

        return read

    def read_block(self, reg):
        read = self.bus.read_i2c_block_data(self.address, reg)

        return read
