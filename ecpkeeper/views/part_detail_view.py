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


class PartDetailView(tk.Frame):
    """Part Detail View"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.data = data,
        self.callbacks = callbacks
        tabs = {}

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        upper_frame = tk.Frame(wrapper_frame)
        upper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        lower_frame = tk.Frame(wrapper_frame)
        lower_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.add_stock = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/factory-24.png')
        self.remove_stock = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/file-delete-24.png')
        self.edit_part = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/add-24.png')

        add_stock_button = ttk.Button(upper_frame,
                                      text='Add Stock',
                                      image=self.add_stock,
                                      compound=tk.LEFT)
        remove_stock_button = ttk.Button(upper_frame,
                                         text='Remove Stock',
                                         image=self.remove_stock,
                                         compound=tk.LEFT)
        edit_part_button = ttk.Button(upper_frame,
                                      text='Edit Part',
                                      image=self.edit_part,
                                      compound=tk.LEFT,
                                      command=lambda:
                                      self.callbacks['file--open_edit_part_window'](self, True))

        # Layout
        add_stock_button.pack(side=tk.LEFT)
        remove_stock_button.pack(side=tk.LEFT)
        edit_part_button.pack(side=tk.LEFT)

