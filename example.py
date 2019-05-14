#!/usr/bin/python3

from pn532.api import PN532


if __name__== "__main__":
    nfc = PN532()

    # setup the device
    nfc.setup(enable_logging=True)

    # keep reading until a value is returned
    while True:
        read = nfc.read()
        print(read)
