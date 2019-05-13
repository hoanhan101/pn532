# pn532

PN532 NFC/RFID Native Python API for your Raspberry Pi.

## Installing

To install the package, simply issue a git clone:
```sh
git clone https://github.com/hoanhan101/pn532.git
```

## Using

### API

> TODO

### Examples

Setup the device, get the reading and print it to the console.
```python
from pn532.api import PN532


if __name__== "__main__":
    nfc = PN532()

    # setup the device
    nfc.setup()

    # keep reading until a value is returned
    read = nfc.read()
    print(read)
```

## Developing

To install necessary development tools:
```sh
make init
```

To run tests:
```sh
make test
```

## Reference
- [PN532 data sheet](https://www.nxp.com/docs/en/nxp/data-sheets/PN532_C1.pdf)
- [PN532 user manual](https://www.nxp.com/docs/en/user-guide/141520.pdf)
