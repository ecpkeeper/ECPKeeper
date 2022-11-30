from tkinter import ttk
import tkinter as tk


class Combobox(ttk.Combobox):
    """ Combobox with validation"""
    def __init__(self, parent, lookups=None, *args, **kwargs):
        super().__init__(parent, **kwargs)
        self.lookups = lookups or {}
        validate_command = self.register(self._validate_all)
        invalid_command = self.register(self._invalid_command)
        self.configure(
            validate='all',
            validatecommand=(validate_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V'),
            invalidcommand=(invalid_command, '%d', '%i', '%P', '%s', '%S', '%v', '%V'),
            values=['', *sorted(self.lookups)]
        )

    def _validate_all(self, d, i, P, s, S, v, V):
        """Validate All"""
        print('d:{} i:{} P:{} s:{} S:{} v:{} V:{}'.format(d, i, P, s, S, v, V))
        if V == 'focusout':
            self._validate_focusout(s)
        elif V == 'key':
            self._validate_key(d, i, P, s, S)
        return True

    def _validate_key(self, d, i, P, s, S):
        """Validate key"""
        if P and d == '1':
            for key in self.lookups:
                if key.casefold().startswith(P.casefold()):
                    autocomplete = key
                    n = len(S)
                    new_index = int(i) + n
                    self.set(autocomplete)
                    self.select_range(new_index, tk.END)
                    self.icursor(new_index)
                    break

    @staticmethod
    def _validate_focusout(s):
        """Validate Focus Out"""
        s = s.strip()
        return True

    @staticmethod
    def _invalid_command(d, i, P, s, S, v, V):
        """Invalid Command"""
        print('Invalid! d:{} i:{} P:{} s:{} S:{} v:{} V:{}'.format(d, i, P, s, S, v, V))