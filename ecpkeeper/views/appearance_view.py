from tkinter import ttk
import tkinter as tk


class PreferencesAppearance(tk.Frame):
    def __init__(self, parent, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.inputs = {}
        self.font_size_var = tk.IntVar()
        self.font_size_label = ttk.Label(self, text='Font size')
        self.inputs['font_size'] = tk.Spinbox(self, textvariable=self.font_size_var)
        # Layout
        self.font_size_label.grid(row=0, column=0)
        self.inputs['font_size'].grid(row=0, column=1)
