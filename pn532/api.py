#
# api.py contains a set of core functions
#

from .smbus2.smbus2 import SMBus, i2c_msg
import time

from pn532.register import *

class PN532(object):
    def __init__(self):
        # i2c device address
        self.address = PN532_DEFAULT_ADDRESS

        # smbus object
        self.bus = SMBus(1)

    def write(self, data):
        """write to its own address with given block data"""
        self.bus.write_i2c_block_data(self.address, self.address, data)

    def read(self, length):
        """read from its own address a given-length of block data"""
        buf = []
        msg = i2c_msg.read(self.address, length)
        self.bus.i2c_rdwr(msg)

        for b in msg:
            buf.append(b)

        return buf
