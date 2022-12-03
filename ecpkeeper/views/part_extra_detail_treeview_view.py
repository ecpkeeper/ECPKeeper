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


class PartExtraDetailForm(tk.Frame):
    """Part Parameters Form"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data
        self.callbacks = callbacks

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        part_extra_detail_upper_frame = tk.Frame(wrapper_frame)
        part_extra_detail_upper_frame.pack(fill=tk.X, side=tk.TOP)
        part_extra_detail_lower_frame = tk.Frame(wrapper_frame, bg='black')
        part_extra_detail_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        part_extra_detail_left_frame = tk.Frame(part_extra_detail_lower_frame)
        part_extra_detail_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        part_extra_detail_right_frame = tk.Frame(part_extra_detail_lower_frame)
        part_extra_detail_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.part_extra_detail_treeview = ttk.Treeview(part_extra_detail_left_frame,
                                                       height=26)

        scrollbar = tk.Scrollbar(part_extra_detail_right_frame, orient=tk.VERTICAL)
        self.part_extra_detail_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.part_extra_detail_treeview.yview())

        # Layout
        self.part_extra_detail_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.part_extra_detail_treeview.insert('',
                                                   'end',
                                                   iid=key,
                                                   text=f'PartParameter ID: {key}',
                                                   values=[record])
