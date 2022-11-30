from tkinter import ttk
import tkinter as tk
from . import char_entry, combobox, spinbox


class FormField(tk.Frame):
    """Combine Widget with Label and layout"""
    def __init__(self, parent, field_cfg, widget_cls, input_kwargs=None, *args, **kwargs):
        super().__init__(parent, **kwargs)
        input_kwargs = input_kwargs or {}
        self.required = field_cfg['required']
        self.lookups = input_kwargs.get('lookups')
        # Variables
        self.input_var = input_kwargs.get('textvariable')
        if not self.input_var:
            if widget_cls in (char_entry.CharEntry, combobox.Combobox):
                self.input_var = tk.StringVar()
            elif widget_cls in (spinbox.Spinbox,):
                self.input_var = tk.IntVar()
            else:
                self.input_var = tk.StringVar()  # Default
        # Widgets
        if widget_cls == combobox.Combobox:
            self.input = widget_cls(self, lookups=self.lookups)
        else:
            self.input = widget_cls(self)
        self.input.configure(textvariable=self.input_var)

        # Label and Errors
        self.label = ttk.Label(self, text=field_cfg['label'])
        self.error_var = tk.StringVar()
        self.errors = ttk.Label(self, textvariable=self.error_var)
        # Layout
        self.label.grid(row=0, column=0)
        self.input.grid(row=1, column=0)
        self.errors.grid(row=2, column=0)

    def is_valid(self):
        """is Valid"""
        self.input.validate()
        current_value = self.input_var.get()
        if self.required:
            if not current_value:
                self.error_var.set('This field is required')
                return False
        return True

    def get(self):
        """Return data"""
        if self.lookups and self.input_var:
            print(self.lookups)
            return self.lookups[self.input_var.get()]
        elif self.input_var:
            return self.input_var.get()
