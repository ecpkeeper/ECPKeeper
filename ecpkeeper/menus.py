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


class MainMenu(tk.Menu):
    """Setup for the Main menu of the application"""
    def __init__(self, parent, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.callbacks = callbacks

        # add menu items to the File menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")
        file_menu.add_separator()
        # add a submenu
        sub_menu = tk.Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Preferences', command=self.callbacks['settings--preferences'])
        # add the File menu to the menubar
        file_menu.add_cascade(label="Settings", menu=sub_menu)
        # add Exit menu item
        file_menu.add_separator()
        file_menu.add_command(label="Exit", underline=1, command=self.callbacks['file--quit'])
        self.add_cascade(label="File", underline=0, menu=file_menu)
        # create the Edit menu
        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label="Projects",
                              command=self.callbacks['edit--open_projects_tab'])
        edit_menu.add_command(label="Footprints",
                              command=self.callbacks['edit--open_footprints_tab'])
        edit_menu.add_command(label="Manufacturers",
                              command=self.callbacks['edit--open_manufacturers_tab'])
        edit_menu.add_command(label="Storage Locations",
                              command=self.callbacks['edit--open_storage_locations_tab'])
        edit_menu.add_command(label="Distributors",
                              command=self.callbacks['edit--open_distributors_tab'])
        edit_menu.add_command(label="Users",
                              command=self.callbacks['edit--open_users_tab'])
        edit_menu.add_command(label="Part Measurement Units",
                              command=self.callbacks['edit--open_part_measurement_units_tab'])
        edit_menu.add_command(label="Units",
                              command=self.callbacks['edit--open_units_tab'])
        self.add_cascade(label="Edit", menu=edit_menu)
        # create the View menu
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label="System Information")
        view_menu.add_command(label="System Notices")
        view_menu.add_command(label="Stock History")
        self.add_cascade(label="View", menu=view_menu)
        # create the Help menu
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="About", command=self.callbacks['help--about'])
        self.add_cascade(label="Help", menu=help_menu)