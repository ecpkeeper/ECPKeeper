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
        upper_frame = tk.Frame(wrapper_frame)
        upper_frame.pack(fill=tk.X, side=tk.TOP)
        lower_frame = tk.Frame(wrapper_frame, bg='black')
        lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        left_frame = tk.Frame(lower_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        right_frame = tk.Frame(lower_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/add-24.png')
        delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/file-delete-24.png')

        add_button = ttk.Button(upper_frame,
                                text='Add',
                                image=add,
                                compound=tk.LEFT)

        delete_button = ttk.Button(upper_frame,
                                   text='Delete',
                                   image=delete,
                                   compound=tk.LEFT)

        self.treeview = ttk.Treeview(left_frame, show='headings', height=26)
        self.treeview['columns'] = ('Parameter',
                                    'Min Value',
                                    'Nominal Value',
                                    'Max Value',
                                    'Unit',
                                    'Description')

        self.set_headers(self.treeview['columns'])

        scrollbar = tk.Scrollbar(right_frame, orient=tk.VERTICAL)
        self.treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.treeview.yview())

        # Layout
        add_button.pack(side=tk.LEFT)
        delete_button.pack(side=tk.LEFT)
        self.treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.treeview.insert('',
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
        self.treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.treeview.heading(i, text=col)
            self.treeview.column(i, width=column_width, stretch=True)
