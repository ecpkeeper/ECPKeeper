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


class ProjectController:
    """ Project Controller"""
    @staticmethod
    def setup(footprint_tab):
        """Setup Project Controller"""
        upper_frame = UpperFrame(footprint_tab)
        bottom_frame = BottomFrame(footprint_tab)

        upper_frame.pack(side="top", expand=True, fill="x")
        bottom_frame.pack(side="bottom", expand=True, fill="x")


class UpperFrame(tk.Frame):
    """ Upper Frame"""
    def __init__(self, parent):
        """Setup Upper Frame"""
        tk.Frame.__init__(self, parent)


class BottomFrame(tk.Frame):
    """Bottom Frame"""
    def __init__(self, parent):
        """Setup Bottom Frame"""
        tk.Frame.__init__(self, parent)
