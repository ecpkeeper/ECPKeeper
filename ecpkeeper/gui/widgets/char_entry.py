from tkinter import ttk
import tkinter as tk


class CharEntry(ttk.Entry):
    """ Char Entry with validation"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, **kwargs)
        validate_command = self.register(self._validate_all)
        invalid_command = self.register(self._invalid_command)
        self.tk_var = kwargs.get('textvariable') or tk.StringVar()
        self.config(
            validate='all',
            validatecommand=(validate_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V'),
            invalidcommand=(invalid_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V')
        )

    def _validate_all(self, d, i, P, s, S, v, V):
        """Validate All"""
        if V == 'focusout':
            self._validate_focusout(s)
        return True

    def _validate_focusout(self, s):
        """Validate Focus Out"""
        s = s.strip()
        self.tk_var.set(s)

    @staticmethod
    def _invalid_command(self, d, i, P, s, S, v, V):
        """Invalid Command"""
        print('Invalid! d:{} i:{} P:{} s:{} S:{} v:{} V:{}'.format(d, i, P, s, S, v, V))