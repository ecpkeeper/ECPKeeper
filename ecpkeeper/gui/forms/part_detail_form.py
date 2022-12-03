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

from views import part_extra_detail_treeview_view, part_stock_history_treeview_view


class PartDetailForm(tk.Frame):
    """Build Part Detail Form window"""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
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

        tabs['part_details'] = tk.Frame(notebook)
        tabs['stock_history'] = tk.Frame(notebook)
        tabs['part_parameters'] = tk.Frame(notebook)
        tabs['attachments'] = tk.Frame(notebook)
        tabs['images'] = tk.Frame(notebook)

        notebook.add(tabs['part_details'], text='Part Details')
        notebook.add(tabs['stock_history'], text='Stock History')
        notebook.add(tabs['part_parameters'], text='Part Parameters')
        notebook.add(tabs['attachments'], text='Attachments')
        notebook.add(tabs['images'], text='Images')

        self.part_frame = part_extra_detail_treeview_view.PartExtraDetailForm(
            tabs['part_details'],
            self.data,
            self.callbacks
        )
        self.distributor_frame = part_stock_history_treeview_view.PartStockHistoryForm(
            tabs['stock_history'],
            {},
            self.callbacks)

