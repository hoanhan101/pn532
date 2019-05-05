#
# api.py contains a set of core functions
#

import smbus
import time

from pn532.register import *

class PN532(object):
    def __init__(self):
        # i2c device address
        self.address = PN532_DEFAULT_ADDRESS

        # smbus object
        self.bus = smbus.SMBus(1)

    def get_address(self):
        return self.address
    
    def sam_config(self):
        """configure board to read RFID tags"""
        buf = []
        buf.append(PN532_COMMAND_SAMCONFIGURATION)
        buf.append(0x01) # normal mode
        buf.append(0x14) # timeout 1s
        buf.append(0x01) # use IRQ pin

        self.write_cmd(buf, 4)

    def write_cmd(self, cmd, cmdlen):
        """write a command to the device, automatically inserting preamble and
        reqired frame details"""
        checksum = 0

        cmdlen += 1

        time.sleep(2)

        checksum = PN532_PREAMBLE + PN532_PREAMBLE + PN532_STARTCODE2
        self.send_byte(PN532_PREAMBLE)
        self.send_byte(PN532_PREAMBLE)
        self.send_byte(PN532_PREAMBLE)

        self.send_byte(cmdlen)
        self.send_byte(~cmdlen + 1)

        self.send_byte(PN532_HOSTTOPN532)
        checksum += PN532_HOSTTOPN532

        for i in range(0, cmdlen-1):
            self.send_byte(cmd[i])
            checksum += cmd[i]

        self.send_byte(~checksum)
        self.send_byte(PN532_POSTAMBLE)

    def send_byte(self, data):
        """send a byte to my default i2c address"""
        self.write_byte(self.address, data)

    def write_byte(self, reg, data):
        self.bus.write_byte_data(self.address, reg, int(data))

    def read_byte(self, reg):
        read = self.bus.read_byte_data(self.address, reg)

        return read

    def write_block(self, reg, data):
        self.bus.write_i2c_block_data(self.address, reg, data)

    def read_block(self, reg):
        read = self.bus.read_i2c_block_data(self.address, reg)

        return read
