"""Tests for the Jddevice class."""

import unittest
from unittest import mock

from myjdapi.myjdapi import (
    Accounts,
    Captcha,
    Config,
    Dialog,
    DownloadController,
    Downloads,
    Extension,
    Jd,
    Jddevice,
    Linkgrabber,
    Reconnect,
    System,
    Toolbar,
    Update,
)


class JddeviceTest(unittest.TestCase):
    def setUp(self):
        myjd = mock.Mock()
        # Avoid the network lookup of direct connections in Jddevice.__init__.
        myjd.get_connection_type.return_value = "remoteapi"
        self.device = Jddevice(myjd, {"name": "Device", "id": "abc", "type": "jd"})

    def test_sub_apis(self):
        expected = {
            "accounts": Accounts,
            "captcha": Captcha,
            "config": Config,
            "dialogs": Dialog,
            "downloadcontroller": DownloadController,
            "downloads": Downloads,
            "extensions": Extension,
            "jd": Jd,
            "linkgrabber": Linkgrabber,
            "reconnect": Reconnect,
            "system": System,
            "toolbar": Toolbar,
            "update": Update,
        }
        for attribute, cls in expected.items():
            with self.subTest(attribute=attribute):
                self.assertIsInstance(getattr(self.device, attribute), cls)

    def test_get_core_revision(self):
        with mock.patch.object(self.device, "action", return_value=50639) as action:
            self.assertEqual(self.device.jd.get_core_revision(), 50639)
        action.assert_called_once_with("/jd/getCoreRevision")


if __name__ == "__main__":
    unittest.main()
