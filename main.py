#!/usr/bin/python3

import time

from pn532.api import PN532


if __name__== "__main__":
    nfc = PN532()

    # setup the device
    nfc.setup()

    # keep reading until a value is returned
    read = nfc.read()
    print(read)
