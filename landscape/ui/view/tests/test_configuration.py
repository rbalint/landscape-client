import sys

from gi.repository import Gtk

from landscape.tests.helpers import LandscapeTest
from landscape.configuration import LandscapeSetupConfiguration
from landscape.ui.view.configuration import LandscapeClientSettingsDialog
from landscape.ui.controller.configuration import ConfigController


class ConfigurationViewTest(LandscapeTest):

    def setUp(self):
        super(ConfigurationViewTest, self).setUp()
        config = """
[client]
data_path = %s
http_proxy = http://proxy.localdomain:3192
tags = a_tag
url = https://landscape.canonical.com/message-system
account_name = foo
registration_password = bar
computer_title = baz
https_proxy = https://proxy.localdomain:6192
ping_url = http://landscape.canonical.com/ping
""" % sys.path[0]
        self.config_filename = self.makeFile(config)
        class MyLandscapeSetupConfiguration(LandscapeSetupConfiguration):
            default_config_filenames = [self.config_filename]
        self.config = MyLandscapeSetupConfiguration(None)

    def test_init(self):
        """
        Test that we correctly initialise the L{ConfigurationView} correctly
        from the controller.
        """
        controller = ConfigController(self.config)
        dialog = LandscapeClientSettingsDialog(controller)
        content_area = dialog.get_content_area()
        children = content_area.get_children()
        self.assertEqual(len(children), 2)
        box = children[0]
        self.assertIsInstance(box, Gtk.Box)
        
        
        
        
