#!/usr/bin/python3

import time

from pn532.api import PN532


if __name__== "__main__":
    nfc = PN532()
    nfc_address = nfc.get_address()
    print(nfc_address)
