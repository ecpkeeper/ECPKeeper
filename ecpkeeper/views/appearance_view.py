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
from tkinter import ttk
import tkinter as tk


class PreferencesAppearance(tk.Frame):
    """Preferences - Appearance Form"""
    def __init__(self, parent, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.callbacks = callbacks
        self.inputs = {}
        self.font_size_var = tk.IntVar()
        self.font_size_label = ttk.Label(self, text='Font size')
        self.inputs['font_size'] = tk.Spinbox(self, textvariable=self.font_size_var)
        # Layout
        self.font_size_label.grid(row=0, column=0)
        self.inputs['font_size'].grid(row=0, column=1)
