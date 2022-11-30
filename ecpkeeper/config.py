from tkinter import font as tkfont
from tkinter import ttk
from .utils.constants import DEFAULT_CONFIG
from .utils.themes import THEMES
import configparser


class AppConfig:
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.load_themes()
        self.load()

    @staticmethod
    def load_themes():
        style = ttk.Style()
        for k, v in THEMES.items():
            style.theme_create(k, v['parent'], v['settings'])
        print(style.theme_names())

    def _update_font(self):
        for font in ('TkHeadingFont', 'TkTextFont', 'TkDefaultFont'):
            f = tkfont.nametofont(font)
<<<<<<< Updated upstream
            f.configure(size=self.cp['Appearance']['fontsize'])
        return
=======
            f.configure(size=int(self.cp['Appearance']['fontsize']))
>>>>>>> Stashed changes

    def save(self):
        with open('setting.ini', 'w') as configfile:
            self.cp.write(configfile)

    def load(self):
        self.cp.read_dict(DEFAULT_CONFIG)
        self.cp.read('setting.ini')
        self._update_font()

    def update_settings(self, data):
        if 'fontsize' in data:
            self.cp.set('Appearance', 'fontsize', data['fontsize'])
            self._update_font()
        self.save()
