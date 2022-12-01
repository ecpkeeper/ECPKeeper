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


class PartParametersForm(tk.Frame):
    """Part Parameters Form"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data
        self.callbacks = callbacks

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        part_parameters_upper_frame = tk.Frame(wrapper_frame)
        part_parameters_upper_frame.pack(fill=tk.X, side=tk.TOP)
        part_parameters_lower_frame = tk.Frame(wrapper_frame, bg='black')
        part_parameters_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        part_parameters_left_frame = tk.Frame(part_parameters_lower_frame)
        part_parameters_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        part_parameters_right_frame = tk.Frame(part_parameters_lower_frame)
        part_parameters_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        part_parameters_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/add-24.png')
        part_parameters_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/file-delete-24.png')

        part_parameters_add_button = ttk.Button(part_parameters_upper_frame,
                                                text='Add',
                                                image=part_parameters_add,
                                                compound=tk.LEFT)

        part_parameters_delete_button = ttk.Button(part_parameters_upper_frame,
                                                   text='Delete',
                                                   image=part_parameters_delete,
                                                   compound=tk.LEFT)

        self.part_parameters_treeview = ttk.Treeview(part_parameters_left_frame,
                                                     show='headings',
                                                     height=26)
        self.part_parameters_treeview['columns'] = ('Parameter',
                                                    'Min Value',
                                                    'Nominal Value',
                                                    'Max Value',
                                                    'Unit',
                                                    'Description')

        self.set_headers(self.part_parameters_treeview['columns'])

        scrollbar = tk.Scrollbar(part_parameters_right_frame, orient=tk.VERTICAL)
        self.part_parameters_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.part_parameters_treeview.yview())

        # Layout
        part_parameters_add_button.pack(side=tk.LEFT)
        part_parameters_delete_button.pack(side=tk.LEFT)
        self.part_parameters_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.part_parameters_treeview.insert('',
                                                 'end',
                                                 iid=key,
                                                 text=f'PartParameter ID: {key}',
                                                 values=[record['Parameter'],
                                                         record['Min Value'],
                                                         record['Nominal Value'],
                                                         record['Max Value'],
                                                         record['Unit'],
                                                         record['Description']])

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.part_parameters_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.part_parameters_treeview.heading(i, text=col)
            self.part_parameters_treeview.column(i, width=column_width, stretch=True)
