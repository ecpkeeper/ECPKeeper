import tkinter as tk


class MainMenu(tk.Menu):
    def __init__(self, parent, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.callbacks = callbacks

        # add menu items to the File menu
        file_menu = tk.Menu(self, tearoff=False)
        file_menu.add_command(label="New", command=lambda: self.callbacks['file--open_add_part_window'](self, True))
        file_menu.add_command(label="Open", command=lambda: self.callbacks['file--open_edit_part_window'](self, True))
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
        edit_menu.add_command(label="Projects", command=self.callbacks['edit--open_projects_tab'])
        edit_menu.add_command(label="Footprints", command=self.callbacks['edit--open_footprints_tab'])
        edit_menu.add_command(label="Manufacturers", command=self.callbacks['edit--open_manufacturers_tab'])
        edit_menu.add_command(label="Storage Locations", command=self.callbacks['edit--open_storage_locations_tab'])
        edit_menu.add_command(label="Distributors", command=self.callbacks['edit--open_distributors_tab'])
        edit_menu.add_command(label="Users", command=self.callbacks['edit--open_users_tab'])
        edit_menu.add_command(label="Part Measurement Units",
                              command=self.callbacks['edit--open_part_measurement_units_tab'])
        edit_menu.add_command(label="Units", command=self.callbacks['edit--open_units_tab'])
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
