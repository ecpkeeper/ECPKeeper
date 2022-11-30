from tkinter import ttk
import tkinter as tk

from ecpkeeper.views.appearance_view import PreferencesAppearance
from ecpkeeper.views.general_view import PreferencesGeneral


class PreferencesForm(tk.Frame):
    def __init__(self, parent, callbacks, **kwargs):
        """"""
        super().__init__(parent, **kwargs)
        self.callbacks = callbacks
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        left_frame = tk.Frame(self, bg='bisque')
        right_frame = tk.Frame(self, bg='lightblue')
        left_frame.grid(row=0, column=0, sticky='NSEW')
        right_frame.grid(row=0, column=1, sticky='NSEW')
        left_frame.columnconfigure(0, weight=1)
        # placeholder label
        self.pref_tree = ttk.Treeview(left_frame)
        self.pref_tree.bind('<<TreeviewSelect>>', self.treeview_select)
        self.pref_tree.insert('', 'end', iid='appearance', text='Appearance!')
        self.pref_tree.insert('', 'end', iid='general', text='General Settings!')
        self.pref_tree.grid(row=0, column=0)

        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)
        self.appearance_frame = PreferencesAppearance(right_frame, self.callbacks)
        self.general_frame = PreferencesGeneral(right_frame, self.callbacks)
        self.appearance_frame.grid(row=0, column=0, sticky='NSEW')
        self.general_frame.grid(row=0, column=0, sticky='NSEW')

    def treeview_select(self, event):  # Don't forget event!
        """"""
        selection = self.pref_tree.selection()
        iid = selection[0]  # first value in the tuple
        if iid == 'appearance':
            self.appearance_frame.lift()
        elif iid == 'general':
            self.general_frame.lift()
