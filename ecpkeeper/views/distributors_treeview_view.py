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
import tkinter.font as tk_font
import tkinter as tk
from pathlib import Path


class DistributorsForm(tk.Frame):
    """Distributors Form"""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data
        self.callbacks = callbacks

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        distributors_upper_frame = tk.Frame(wrapper_frame)
        distributors_upper_frame.pack(fill=tk.X, side=tk.TOP)
        distributors_lower_frame = tk.Frame(wrapper_frame, bg='black')
        distributors_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        distributors_left_frame = tk.Frame(distributors_lower_frame)
        distributors_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        distributors_right_frame = tk.Frame(distributors_lower_frame)
        distributors_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        distributors_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/add-24.png')
        distributors_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/file-delete-24.png')

        distributors_add_button = ttk.Button(distributors_upper_frame,
                                             text='Add',
                                             image=distributors_add,
                                             compound=tk.LEFT)
        distributors_delete_button = ttk.Button(distributors_upper_frame,
                                                text='Delete',
                                                image=distributors_delete,
                                                compound=tk.LEFT)

        self.distributors_treeview = ttk.Treeview(distributors_left_frame,
                                                  show='headings',
                                                  height=26)
        self.distributors_treeview['columns'] = ('Distributor',
                                                 'Order Number',
                                                 'Packaging Unit',
                                                 'Status',
                                                 'Price Per Item',
                                                 'Currency',
                                                 'Package Price',
                                                 'SKU',
                                                 'Pricing')

        self.set_headers(self.distributors_treeview['columns'])

        scrollbar = tk.Scrollbar(distributors_right_frame, orient=tk.VERTICAL)
        self.distributors_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.distributors_treeview.yview())

        # Layout
        distributors_add_button.pack(side=tk.LEFT)
        distributors_delete_button.pack(side=tk.LEFT)
        self.distributors_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.distributors_treeview.insert('',
                                              'end',
                                              iid=key,
                                              text=f'Distributor ID: {key}',
                                              values=[record['Distributor'],
                                                      record['Order Number'],
                                                      record['Packaging Unit'],
                                                      record['Status'],
                                                      record['Price Per Item'],
                                                      record['Currency'],
                                                      record['Package Price'],
                                                      record['SKU'],
                                                      record['Pricing']]
                                              )

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.distributors_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.distributors_treeview.heading(i, text=col)
            self.distributors_treeview.column(i, width=column_width, stretch=True)
