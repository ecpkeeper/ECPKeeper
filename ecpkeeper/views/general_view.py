from tkinter import ttk
import tkinter as tk


class PreferencesGeneral(tk.Frame):
    """Preferences - General Form"""
    def __init__(self, parent, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.placeholder = ttk.Label(self, text='Placeholder for general settings')
        self.placeholder.grid(row=0, column=0)
