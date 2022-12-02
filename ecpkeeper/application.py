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
from tkinter import ttk, messagebox
import tkinter as tk
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from ecpkeeper import menus
from ecpkeeper import config
from ecpkeeper.controllers.project_controller import ProjectController
from ecpkeeper.views.parts_management_treeview_view import PartsManagementForm
from views.part_detail_view import PartDetailView
from . import gui


class Win(tk.Tk):
    """Main Window container."""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        super().__init__(*kwargs)
        self._appconfig = config.AppConfig()
        self.settings = {}
        self.title('ECPKeeper')
        engine = create_engine('sqlite:///var/ecpkeeper.db', echo=True)
        self.session = sessionmaker(bind=engine)
        self.callbacks = {
            'file--quit': self.quit,
            'file--open_add_part_window': self.open_add_part_window,
            'file--open_edit_part_window': self.open_edit_part_window,
            'edit--open_projects_tab': self.open_projects_tab,
            'edit--open_footprints_tab': self.open_footprints_tab,
            'edit--open_manufacturers_tab': self.open_manufacturers_tab,
            'edit--open_storage_locations_tab': self.open_storage_locations_tab,
            'edit--open_distributors_tab': self.open_distributors_tab,
            'edit--open_users_tab': self.open_users_tab,
            'edit--open_part_measurement_units_tab': self.open_part_measurement_units_tab,
            'edit--open_units_tab': self.open_units_tab,
            'settings--preferences': self.open_preferences_window,
            'part_detail_form': self.open_part_details_window,
            'parts-form--save_parts_form': self.save_parts_form,
            'help--about': self.about
        }
        # Root configuration for minimize, resize support
        self.minsize(1024, 768)
        # Menu
        menu = menus.MainMenu(self, self.callbacks)
        self.configure(menu=menu)

        # First layer of elements
        wrapper_frame = tk.Frame(self)
        wrapper_frame.pack(expand=True, fill=tk.BOTH)
        main_frame = tk.Frame(wrapper_frame)
        main_frame.configure(bg='lightblue')
        main_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)

        status_bar = tk.Frame(wrapper_frame)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        status_bar.configure(relief='ridge', bd=1, bg='white')
        status_bar_label = ttk.Label(status_bar, text='STATUS BAR!')
        status_bar_label.pack(side=tk.LEFT)

        workspace_frame = tk.Frame(main_frame)
        workspace_frame.configure(bg='#5D6D7E')
        workspace_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

        self.custom_notebook = gui.widgets.custom_notebook.CustomNotebook(workspace_frame)
        parts_management_tab = tk.Frame(self.custom_notebook)
        self.custom_notebook.add(parts_management_tab, text="Parts Management")
        self.custom_notebook.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.parts_management = PartsManagementForm(parts_management_tab, {}, self.callbacks)
        self.parts_management.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.part_form_window = None
        self.part_form = None
        self.part_detail_window = None
        self.part_detail_form = None
        self.preferences_form_window = None
        self.preferences_form = None

    def open_preferences_window(self):
        """Open Settings -- Preference window"""
        if self.preferences_form_window is None or not self.preferences_form_window.winfo_exists():
            self.preferences_form_window = tk.Toplevel(self)
            self.preferences_form_window.title('Preferences')
            self.preferences_form_window.minsize(480, 320)
            self.preferences_form_window.rowconfigure(0, weight=1)
            self.preferences_form_window.columnconfigure(0, weight=1)
            self.preferences_form = gui.forms.preferences_form.PreferencesForm(
                self.preferences_form_window,
                self.callbacks
            )
            self.preferences_form.grid(row=0, column=0, sticky="nsew")
        else:
            self.preferences_form_window.lift(self)
        self.preferences_form_window.focus()

    def open_add_part_window(self, called_from=None, model=False):
        """Open Part Window -- Add Part Frame"""
        self.part_form_window = gui.widgets.toplevel.Toplevel(self, called_from, model)
        self.part_form_window.title('Add Part')
        self.part_form_window.minsize(480, 320)
        self.part_form_window.resizable(False, False)
        if model is True:
            self.part_form_window.grab_set()
        self.part_form = gui.forms.part_form.PartForm(
            self.part_form_window,
            {},
            self.callbacks,
            False
        )
        self.part_form.pack()
        self.part_form_window.focus()

    def open_part_details_window(self, called_from=None, model=False):
        """Open Part Detail Window"""
        self.part_detail_window = gui.widgets.toplevel.Toplevel(self, called_from, model)
        self.part_detail_window.title('Part Detail')
        self.part_detail_window.minsize(480, 320)
        self.part_detail_window.resizable(False, False)
        if model is True:
            self.part_detail_window.grab_set()
        self.part_detail_form = gui.forms.part_detail_form.PartDetailForm(
            self.part_detail_window,
            {},
            self.callbacks
        )
        self.part_detail_form.pack()
        self.part_detail_window.focus()

    def open_edit_part_window(self, called_from=None, model=False):
        """Open Part Window -- Edit Part Frame"""
        self.part_form_window = gui.widgets.toplevel.Toplevel(self, called_from, model)
        print(f'This is the part_form_window: {self.part_form_window.model}')
        self.part_form_window.title('Edit Part')
        self.part_form_window.minsize(480, 320)
        self.part_form_window.resizable(False, False)
        if model is True:
            self.part_form_window.grab_set()
        self.part_form = gui.forms.part_form.PartForm(
            self.part_form_window,
            {}, self.callbacks,
            True
        )
        self.part_form.pack()
        self.part_form_window.focus()

    def save_parts_form(self):
        """Part Window -- Save Part Form"""
        previous_form = self.part_form_window.called_from
        print(f'This is the part_form_window: {self.part_form_window.model}')
        if self.part_form.is_valid():
            data = self.part_form.get()
            self.parts_management.load_records(data)
            print(data)
        if previous_form is not None:
            previous_form.focus()
        if self.part_form_window.model is True:
            self.part_form_window.destroy()

    @contextmanager
    def session_scope(self):
        """Session system for sqlalchemy"""
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as exception:
            print(exception)
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def about():
        """About messagebox popup"""
        messagebox.showinfo('PythonGuides',
                            'Python Guides aims at providing best practical tutorials')

    def get_tab_names(self):
        """Get Tab names to stop opening of multiple instances"""
        return [self.custom_notebook.tab(i, option="text") for i in self.custom_notebook.tabs()]

    def open_projects_tab(self):
        """ Open Projects Tab"""
        tab_names = self.get_tab_names()
        print(tab_names)
        if 'Projects' not in tab_names:
            projects_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(projects_tab, text='Projects')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_footprints_tab(self):
        """Open Footprints Tab"""
        tab_names = self.get_tab_names()
        if 'Footprints' not in tab_names:
            footprint_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(footprint_tab, text='Footprints')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_manufacturers_tab(self):
        """ Open Manufacturers Tab"""
        tab_names = self.get_tab_names()
        if 'Manufacturers' not in tab_names:
            manufacturers_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(manufacturers_tab, text='Manufacturers')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_storage_locations_tab(self):
        """Open Storage Locations Tab"""
        tab_names = self.get_tab_names()
        if 'Storage Locations' not in tab_names:
            storage_locations_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(storage_locations_tab, text='Storage Locations')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_distributors_tab(self):
        """Open Distributors Tab"""
        tab_names = self.get_tab_names()
        if 'Distributors' not in tab_names:
            distributors_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(distributors_tab, text='Distributors')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_users_tab(self):
        """Open Users Tab"""
        tab_names = self.get_tab_names()
        if 'Users' not in tab_names:
            users_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(users_tab, text='Users')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_part_measurement_units_tab(self):
        """Open Part Measurement Units Tab"""
        tab_names = self.get_tab_names()
        if 'Part Measurement Units' not in tab_names:
            part_measurement_units_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(part_measurement_units_tab, text='Part Measurement Units')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_units_tab(self):
        """Open Units Tab"""
        tab_names = self.get_tab_names()
        if 'Units' not in tab_names:
            units_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(units_tab, text='Units')
            self.custom_notebook.pack(expand=1, fill="both")
            ProjectController.setup(units_tab)


def main():
    """ Main Loop of Application"""
    app = Win()
    app.mainloop()


if __name__ == "__main__":
    main()
