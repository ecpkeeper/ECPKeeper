from tkinter import ttk
import tkinter as tk


class Spinbox(ttk.Spinbox):
    """ Spinbox with validation"""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        validate_command = self.register(self._validate_all)
        invalid_command = self.register(self._invalid_command)
        self.configure(
            validate='all',
            validatecommand=(validate_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V'),
            invalidcommand=(invalid_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V'),
        )

    def _validate_all(self, d, i, P, s, S, v, V):
        """Validate All"""
        print('d:{} i:{} P:{} s:{} S:{} v:{} V:{}'.format(d, i, P, s, S, v, V))
        valid = True
        if V == 'key':
            valid = self._validate_key(d, i, P, s, S)
        return valid

    @staticmethod
    def _validate_key(self, d, i, P, s, S):
        """Validate Key"""
        try:
            int(S)
        except ValueError:
            return False
        if len(P) > 4:
            return False
        return True

    @staticmethod
    def _invalid_command(self, d, i, P, s, S, v, V):
        """Invalid Command"""
        print('Invalid! d:{} i:{} P:{} s:{} S:{} v:{} V:{}'.format(d, i, P, s, S, v, V))