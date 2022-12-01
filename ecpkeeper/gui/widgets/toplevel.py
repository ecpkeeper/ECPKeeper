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
import tkinter as tk


class Toplevel(tk.Toplevel):
    """Toplevel Widget adding called_from and model to toplevel"""
    def __init__(self, parent, called_from=None, model=False, **kwargs):
        super().__init__(parent, **kwargs)
        self.called_from = called_from
        self.model = model
