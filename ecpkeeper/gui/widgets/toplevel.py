from tkinter import ttk
import tkinter as tk


class Toplevel(tk.Toplevel):
    """Toplevel Widget adding called_from and model to toplevel"""
    def __init__(self, parent, called_from=None, model=False, *args, **kwargs):
        super().__init__(parent, **kwargs)
        self.called_from = called_from
        self.model = model
