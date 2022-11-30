from tkinter import font as tkfont
from tkinter import ttk
from .utils.constants import DEFAULT_CONFIG
from .utils.themes import THEMES
import configparser


class AppConfig:
    """Setup for the settings of the application"""
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.load_themes()
        self.load()

    @staticmethod
    def load_themes():
        """Load Themes"""
        style = ttk.Style()
        for k, v in THEMES.items():
            style.theme_create(k, v['parent'], v['settings'])
        print(style.theme_names())

    def _update_font(self):
        """Update Font Size"""
        for font in ('TkHeadingFont', 'TkTextFont', 'TkDefaultFont'):
            f = tkfont.nametofont(font)
            f.configure(size=int(self.cp['Appearance']['fontsize']))
        return

    def save(self):
        """Save settings"""
        with open('setting.ini', 'w') as configfile:
            self.cp.write(configfile)
        return

    def load(self):
        """Load Settings"""
        self.cp.read_dict(DEFAULT_CONFIG)
        self.cp.read('setting.ini')
        self._update_font()
        return

    def update_settings(self, data):
        """Update Settings"""
        if 'fontsize' in data:
            self.cp.set('Appearance', 'fontsize', data['fontsize'])
            self._update_font()
        self.save()
        return
