# PROJECT: Wine Launcher
# DESC: Wine Launcher Main Window Module
# AUTHOR: Erdem Ersoy
# LICENSE: CC0-1.0

import gettext
import locale

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gio", "2.0")
from gi.repository import Gtk

locale.setlocale(locale.LC_ALL, "")
locale.bindtextdomain("python-gtk-hello-world", "locale/")
gettext.bindtextdomain("python-gtk-hello-world", "locale/")
gettext.textdomain("python-gtk-hello-world")
_ = gettext.gettext
gettext.install("python-gtk-hello-world", "locale/")


class WineLauncherWindow(object):
    def __init__(self, app):
        self.App = app

        gui_file = "WineLauncher.glade"
        self.builder = Gtk.Builder().new_from_file(gui_file)
        self.builder.connect_signals(self)

        self.WineLauncherWindow = self.builder.get_object("WineLauncherWindow")
        self.WineLauncherWindow.set_application(self.App)
        self.WineLauncherWindow.show()

        self.WineLauncherWindowAboutDialog = self.builder.get_object("WineLauncherWindowAboutDialog")

    def OnClickedMenuAbout(self, menu_item):
        self.WineLauncherWindowAboutDialog.run()
        self.WineLauncherWindowAboutDialog.hide()
