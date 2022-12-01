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
from pathlib import Path

from ecpkeeper.views import part_view
from ecpkeeper.views import distributors_treeview_view
from ecpkeeper.views import manufacturers_treeview_view
from ecpkeeper.views import parts_parameters_treeview_view


class PartForm(tk.Frame):
    """Build Part Form window and load either edit or add Part Frame"""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    def __init__(self, parent, data, callbacks, edit, **kwargs):
        super().__init__(parent, **kwargs)
        self.edit = edit
        self.callbacks = callbacks
        self.data = data
        self.fields = {}
        tabs = {}

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        upper_frame = tk.Frame(wrapper_frame)
        upper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        lower_frame = tk.Frame(wrapper_frame)
        lower_frame.pack(side=tk.BOTTOM, fill=tk.X)
        notebook = ttk.Notebook(upper_frame)
        notebook.pack(expand=1, fill=tk.BOTH)

        tabs['part_data'] = tk.Frame(notebook)
        tabs['distributors_data'] = tk.Frame(notebook)
        tabs['manufacturers_data'] = tk.Frame(notebook)
        tabs['part_parameters_data'] = tk.Frame(notebook)
        tabs['attachments_data'] = tk.Frame(notebook)

        notebook.add(tabs['part_data'], text='Basic Data')
        notebook.add(tabs['distributors_data'], text='Distributors')
        notebook.add(tabs['manufacturers_data'], text='Manufacturers')
        notebook.add(tabs['part_parameters_data'], text='Part Parameters')
        notebook.add(tabs['attachments_data'], text='Attachments')

        self.save = tk.PhotoImage(file=f'{Path.cwd()}/ecpkeeper/assets/images/save-24.png')
        self.cancel = tk.PhotoImage(file=f'{Path.cwd()}/ecpkeeper/assets/images/cancel-24.png')

        save_button = ttk.Button(lower_frame, text='Save', image=self.save, compound=tk.LEFT,
                                 command=lambda: self.callbacks['parts-form--save_parts_form'](edit)
                                 )
        cancel_button = ttk.Button(lower_frame, text='Cancel', image=self.cancel, compound=tk.LEFT)
        save_button.pack(side=tk.LEFT)
        cancel_button.pack(side=tk.LEFT)

        if edit is True:
            self.data = {'name': 'this is a test of the name field',
                         'description': 'This is a test of the description field'}

        self.part_frame = part_view.PartView(
            tabs['part_data'],
            self.data,
            self.callbacks,
            self.edit
        )
        self.distributor_frame = distributors_treeview_view.DistributorsForm(
            tabs['distributors_data'],
            {},
            self.callbacks)
        self.manufacturers_frame = manufacturers_treeview_view.ManufacturersForm(
            tabs['manufacturers_data'],
            {},
            self.callbacks)
        self.part_parameter_frame = parts_parameters_treeview_view.PartParametersForm(
            tabs['part_parameters_data'],
            {},
            self.callbacks)
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
