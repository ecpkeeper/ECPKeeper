"""
Open Source Electronic Component Inventory Management.
Copyright (C) 2022 DOS1986

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from tkinter import font as tkfont
from tkinter import ttk
import configparser
from .utils.constants import DEFAULT_CONFIG
from .utils.themes import THEMES


class AppConfig:
    """Setup for the settings of the application"""
    def __init__(self):
        self.configparser = configparser.ConfigParser()
        self.load_themes()
        self.load()

    @staticmethod
    def load_themes():
        """Load Themes"""
        style = ttk.Style()
        for key, value in THEMES.items():
            style.theme_create(key, value['parent'], value['settings'])
        print(style.theme_names())

    def _update_font(self):
        """Update Font Size"""
        for font in ('TkHeadingFont', 'TkTextFont', 'TkDefaultFont'):
            nametofont = tkfont.nametofont(font)
            nametofont.configure(size=int(self.configparser['Appearance']['fontsize']))

    def save(self):
        """Save settings"""
        with open('setting.ini', 'w', encoding="utf-8") as configfile:
            self.configparser.write(configfile)

    def load(self):
        """Load Settings"""
        self.configparser.read_dict(DEFAULT_CONFIG)
        self.configparser.read('setting.ini')
        self._update_font()

    def update_settings(self, data):
        """Update Settings"""
        if 'fontsize' in data:
            self.configparser.set('Appearance', 'fontsize', data['fontsize'])
            self._update_font()
        self.save()
