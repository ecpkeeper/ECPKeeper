from tkinter import ttk
import tkinter as tk

from ecpkeeper.views.part_view import PartView
from ecpkeeper.views.distributors_treeview_view import DistributorsForm
from ecpkeeper.views.manufacturers_treeview_view import ManufacturersForm
from ecpkeeper.views.parts_parameters_treeview_view import PartParametersForm


class PartForm(tk.Frame):
    def __init__(self, parent, data, callbacks, edit, **kwargs):
        """Build Part Form window and load either edit or add Part Frame"""
        super().__init__(parent, **kwargs)
        self.edit = edit
        self.callbacks = callbacks
        self.data = data
        self.fields = {}

        self.wrapper_frame = self
        self.wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.upper_frame = tk.Frame(self.wrapper_frame)
        self.upper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.lower_frame = tk.Frame(self.wrapper_frame)
        self.lower_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.notebook = ttk.Notebook(self.upper_frame)
        self.notebook.pack(expand=1, fill=tk.BOTH)

        part_data = tk.Frame(self.notebook)
        distributors_data = tk.Frame(self.notebook)
        manufacturers_data = tk.Frame(self.notebook)
        part_parameters_data = tk.Frame(self.notebook)
        attachments_data = tk.Frame(self.notebook)

        self.notebook.add(part_data, text='Basic Data')
        self.notebook.add(distributors_data, text='Distributors')
        self.notebook.add(manufacturers_data, text='Manufacturers')
        self.notebook.add(part_parameters_data, text='Part Parameters')
        self.notebook.add(attachments_data, text='Attachments')

        self.save = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\save-24.png")
        self.cancel = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\cancel-24.png")

        self.save_button = ttk.Button(self.lower_frame, text='Save', image=self.save, compound=tk.LEFT,
                                      command=lambda: self.callbacks['parts-form--save_parts_form'](edit))
        self.cancel_button = ttk.Button(self.lower_frame, text='Cancel', image=self.cancel, compound=tk.LEFT)
        self.save_button.pack(side=tk.LEFT)
        self.cancel_button.pack(side=tk.LEFT)

        if edit is True:
            self.data = {'name': 'this is a test of the name field',
                         'description': 'This is a test of the description field'}

        self.part_frame = PartView(part_data, self.data, self.callbacks, self.edit)
        self.distributor_frame = DistributorsForm(distributors_data, {}, self.callbacks)
        self.manufacturers_frame = ManufacturersForm(manufacturers_data, {}, self.callbacks)
        self.part_parameter_frame = PartParametersForm(part_parameters_data, {}, self.callbacks)
        self.part_frame.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.distributor_frame.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.manufacturers_frame.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        self.part_parameter_frame.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.focus()
        self.grab_set()

    def is_valid(self):
        """Are widgets in self.fields Valid"""
        valid = True
        for key, widget in self.fields.items():
            if not widget.is_valid():
                valid = False
        return valid

    def get(self):
        """ Get Data From Part Form"""
        data = {
                'part': [
                    self.part_frame.get()
                ]
            }
        return data


