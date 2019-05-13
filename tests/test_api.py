# -*- coding: utf-8 -*-

from .context import pn532

import unittest


class TestConstructFrame(unittest.TestCase):
    def test_sam_config(self):
        expected = [0x00, 0x00, 0xff, 0x05, 0xfb, 0xd4, 0x14, 0x01, 0x01, 0x00, 0x16, 0x00]
        self.assertEqual(pn532.construct_frame([pn532.PN532_COMMAND_SAMCONFIGURATION, 0x01, 0x01, 0x00]), expected)

    def test_in_list_passive_target(self):
        expected = [0x00, 0x00, 0xff, 0x04, 0xfc, 0xd4, 0x4a, 0x01, 0x00, 0xe1, 0x00]
        self.assertEqual(pn532.construct_frame([pn532.PN532_COMMAND_INLISTPASSIVETARGET, 0x01, 0x00]), expected)


if __name__ == '__main__':
    unittest.main()
