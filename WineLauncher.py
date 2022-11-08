# PROJECT: Wine Launcher
# DESC: Wine Launcher Main Window Module
# AUTHOR: Erdem Ersoy
# LICENSE: CC0-1.0

import gettext
import locale
import os
import subprocess

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gio", "2.0")
from gi.repository import Gtk

locale.setlocale(locale.LC_ALL, "")
locale.bindtextdomain("wine-launcher", "locale/")
gettext.bindtextdomain("wine-launcher", "locale/")
gettext.textdomain("wine-launcher")
_ = gettext.gettext
gettext.install("wine-launcher", "locale/")


class WineLauncherWindow(object):
    def __init__(self, app):
        self.App = app

        gui_file = "WineLauncher.glade"
        self.builder = Gtk.Builder().new_from_file(gui_file)
        self.builder.connect_signals(self)

        self.WineLauncherWindow = self.builder.get_object("WineLauncherWindow")
        self.WineLauncherWindow.set_application(self.App)
        self.WineLauncherWindow.show()

        self.WineLauncherWindowEntryPrefix = self.builder.get_object("WineLauncherWindowEntryPrefix")
        self.WineLauncherWindowEntryArch = self.builder.get_object("WineLauncherWindowEntryArch")
        self.WineLauncherWindowEntryProgram = self.builder.get_object("WineLauncherWindowEntryProgram")

        self.WineLauncherWindowAboutDialog = self.builder.get_object("WineLauncherWindowAboutDialog")

    def OnClickedLaunchButton(self, button):
        current_env = os.environ.copy()
        current_env["WINEPREFIX"] = self.WineLauncherWindowEntryPrefix.get_text()
        current_env["WINEARCH"] = self.WineLauncherWindowEntryArch.get_text()
        subprocess.run(["wine", self.WineLauncherWindowEntryProgram.get_text()], env=current_env)
        self.WineLauncherWindow.destroy()

    def OnClickedMenuAbout(self, menu_item):
        self.WineLauncherWindowAboutDialog.run()
        self.WineLauncherWindowAboutDialog.hide()
