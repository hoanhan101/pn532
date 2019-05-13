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

    def setup(self):
        """setup the device"""
        self.sam_config()

    def read(self):
        """keep reading until a card is detected, return the reading afterward"""
        self.in_list_passive_target()

        while True:
            read = self.read_addr(BLOCK_SIZE)
            if read[:3] != [0x00, 0x80, 0x80]:
                return read

    def sam_config(self):
        """send SAMConfiguration command"""
        sam_config = [0x00, 0x00, 0xff, 0x05, 0xfb, 0xd4, 0x14, 0x01, 0x01, 0x00, 0x16, 0x00]
        self.write_addr(sam_config)
        self.read_addr(BLOCK_SIZE)

    def in_list_passive_target(self):
        """send InListPassiveTarget command"""
        card_config = [0x00, 0x00, 0xff, 0x04, 0xfc, 0xd4, 0x4a, 0x01, 0x00, 0xe1, 0x00]
        self.write_addr(card_config)
        self.read_addr(BLOCK_SIZE)

    def construct_frame(self, data):
        # begin with 6-bytes frame structure
        buf = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        buf[0] = PN532_PREAMBLE
        buf[1] = PN532_STARTCODE1
        buf[2] = PN532_STARTCODE2
        buf[3] = len(data) + 1          # number of bytes in data and frame identifier field
        buf[4] = (buf[3] & 0xFF) + 0x01 # packet length checksum
        buf[5] = PN532_HOSTTOPN532

        return buf

    def write_addr(self, data):
        """write to its own address with given block data"""
        time.sleep(REST_INTERVAL)

        self.bus.write_i2c_block_data(self.address, self.address, data)
        print("write_addr:", data)

    def read_addr(self, length):
        """read from its own address a given-length of block data"""
        time.sleep(REST_INTERVAL)

        buf = []
        msg = i2c_msg.read(self.address, length)
        self.bus.i2c_rdwr(msg)

        for b in msg:
            buf.append(b)

        print("read_addr:", buf)
        return buf
