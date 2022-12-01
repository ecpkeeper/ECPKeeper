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


class PartsManagementForm(tk.Frame):
    """Parts Management Form"""

    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data
        self.callbacks = callbacks

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        parts_management_upper_frame = tk.Frame(wrapper_frame)
        parts_management_upper_frame.pack(fill=tk.X, side=tk.TOP)
        parts_management_lower_frame = tk.Frame(wrapper_frame, bg='black')
        parts_management_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        parts_management_left_frame = tk.Frame(parts_management_lower_frame)
        parts_management_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        parts_management_right_frame = tk.Frame(parts_management_lower_frame)
        parts_management_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.parts_management_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/add-24.png')
        self.parts_management_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/file-delete-24.png')

        parts_management_add_button = ttk.Button(parts_management_upper_frame,
                                                 text='Add',
                                                 image=self.parts_management_add,
                                                 compound=tk.LEFT)
        parts_management_delete_button = ttk.Button(parts_management_upper_frame,
                                                    text='Delete',
                                                    image=self.parts_management_delete,
                                                    compound=tk.LEFT)

        self.parts_management_treeview = ttk.Treeview(parts_management_left_frame,
                                                      show='headings',
                                                      height=35)
        self.parts_management_treeview['columns'] = ('Name',
                                                     'Description',
                                                     'Storage Location',
                                                     'Status',
                                                     'Condition',
                                                     'Stock',
                                                     'Min. Stock',
                                                     'Avg. Price',
                                                     'Footprint',
                                                     'Internal ID')

        self.set_headers(self.parts_management_treeview['columns'])

        scrollbar = tk.Scrollbar(parts_management_right_frame, orient=tk.VERTICAL)
        self.parts_management_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.parts_management_treeview.yview())

        # Layout
        parts_management_add_button.pack(side=tk.LEFT)
        parts_management_delete_button.pack(side=tk.LEFT)
        self.parts_management_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.parts_management_treeview.insert('', 'end',
                                                  iid=key,
                                                  text=f'Part ID: {key}',
                                                  values=[record['Name'],
                                                          record['Description'],
                                                          record['Storage Location'],
                                                          record['Status'],
                                                          record['Condition'],
                                                          record['Stock'],
                                                          record['Min. Stock'],
                                                          record['Avg. Price'],
                                                          record['Footprint'],
                                                          record['Internal ID']])

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.parts_management_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.parts_management_treeview.heading(i, text=col)
            self.parts_management_treeview.column(i, width=column_width, stretch=True)
