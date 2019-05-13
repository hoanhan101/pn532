#
# api.py contains a set of core functions
#

from .smbus2.smbus2 import SMBus, i2c_msg
import time

from pn532.register import *

REST_INTERVAL = 0.5
BLOCK_SIZE = 20

class PN532(object):
    def __init__(self):
        # i2c device address
        self.address = PN532_DEFAULT_ADDRESS

        # smbus object
        self.bus = SMBus(1)

    def sam_config(self):
        """send samconfig command"""
        sam_config = [0x00, 0x00, 0xff, 0x05, 0xfb, 0xd4, 0x14, 0x01, 0x01, 0x00, 0x16, 0x00]
        self.write(sam_config)
        self.read(BLOCK_SIZE)

    def write(self, data):
        """write to its own address with given block data"""
        time.sleep(REST_INTERVAL)

        self.bus.write_i2c_block_data(self.address, self.address, data)
        print("write:", data)

    def read(self, length):
        """read from its own address a given-length of block data"""
        time.sleep(REST_INTERVAL)

        buf = []
        msg = i2c_msg.read(self.address, length)
        self.bus.i2c_rdwr(msg)

        for b in msg:
            buf.append(b)

        print("read:", buf)
        return buf
