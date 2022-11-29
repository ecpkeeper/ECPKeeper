from ecpkeeper import menus
from ecpkeeper.config import AppConfig
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import ttk, messagebox
import tkinter as tk

from ecpkeeper.controllers.project_controller import ProjectController
from . import gui

class Application(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(*kwargs)
        self._appconfig = AppConfig()
        self.settings = {}
        self.title('ECPKeeper')
        engine = create_engine('sqlite:///var/ecpkeeper.db', echo=True)
        self.Session = sessionmaker(bind=engine)
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
            'parts-form--save_parts_form': self.save_parts_form,
            'help--about': self.about
        }
        # Root configuration for minimize, resize support
        self.minsize(1024, 768)
        # Menu
        menu = menus.MainMenu(self, self.callbacks)
        self.configure(menu=menu)
        # First layer of elements
        self.wrapper_frame = tk.Frame(self)
        self.wrapper_frame.pack(expand=True, fill=tk.BOTH)
        self.main_frame = tk.Frame(self.wrapper_frame)
        self.main_frame.configure(bg='lightblue')
        self.main_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.status_bar = tk.Frame(self.wrapper_frame)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_bar.configure(relief='ridge', bd=1, bg='white')
        self.status_bar_label = ttk.Label(self.status_bar, text='STATUS BAR!')
        self.status_bar_label.pack(side=tk.LEFT)
        self.workspace_frame = tk.Frame(self.main_frame)
        self.right_nav_frame = tk.Frame(self.main_frame, width=300)
        self.workspace_frame.configure(bg='#5D6D7E')
        self.right_nav_frame.configure(bg='#85929E')
        self.workspace_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        self.right_nav_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.custom_notebook = gui.widgets.custom_notebook.CustomNotebook(self.workspace_frame)
        self.parts_management_tab = tk.Frame(self.custom_notebook)
        self.custom_notebook.add(self.parts_management_tab, text="Parts Management")
        self.custom_notebook.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.part_form_window = None
        self.part_form = None
        self.preferences_form_window = None
        self.preferences_form = None

    def open_preferences_window(self):
        if self.preferences_form_window is None or not self.preferences_form_window.winfo_exists():
            self.preferences_form_window = tk.Toplevel(self)
            self.preferences_form_window.title('Preferences')
            self.preferences_form_window.minsize(480, 320)
            self.preferences_form_window.rowconfigure(0, weight=1)
            self.preferences_form_window.columnconfigure(0, weight=1)
            self.preferences_form = gui.forms.preferences_form.PreferencesForm(self.preferences_form_window, self.callbacks)
            self.preferences_form.grid(row=0, column=0, sticky="nsew")
        else:
            self.preferences_form_window.lift(self)
        self.preferences_form_window.focus()

    def open_add_part_window(self, called_from=None, model=False):
        self.part_form_window = gui.widgets.toplevel.Toplevel(self, called_from, model)
        self.part_form_window.title('Add Part')
        self.part_form_window.minsize(480, 320)
        self.part_form_window.resizable(False, False)
        if model is True:
            self.part_form_window.grab_set()
        self.part_form = gui.forms.parts_form.PartForm(self.part_form_window, {}, self.callbacks, False)
        self.part_form.pack()
        self.part_form_window.focus()

    def open_edit_part_window(self, called_from=None, model=False):
        self.part_form_window = gui.widgets.toplevel.Toplevel(self, called_from, model)
        print(f'This is the part_form_window: {self.part_form_window.model}')
        self.part_form_window.title('Edit Part')
        self.part_form_window.minsize(480, 320)
        self.part_form_window.resizable(False, False)
        if model is True:
            self.part_form_window.grab_set()
        self.part_form = gui.forms.parts_form.PartForm(self.part_form_window, {}, self.callbacks, True)
        self.part_form.pack()
        self.part_form_window.focus()

    def save_parts_form(self, edit):
        previous_form = self.part_form_window.called_from
        print(f'This is the part_form_window: {self.part_form_window.model}')
        if self.part_form.is_valid():
            data = self.part_form.get(edit)
            print(data)
        if previous_form is not None:
            previous_form.focus()
        if self.part_form_window.model is True:
            self.part_form_window.destroy()

    @contextmanager
    def session_scope(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def about():
        messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')

    @staticmethod
    def get_tab_names(self):
        return [self.custom_notebook.tab(i, option="text") for i in self.custom_notebook.tabs()]

    def open_projects_tab(self):
        tab_names = self.get_tab_names(self)
        print(tab_names)
        if 'Projects' not in tab_names:
            projects_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(projects_tab, text='Projects')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_footprints_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Footprints' not in tab_names:
            footprint_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(footprint_tab, text='Footprints')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_manufacturers_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Manufacturers' not in tab_names:
            manufacturers_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(manufacturers_tab, text='Manufacturers')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_storage_locations_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Storage Locations' not in tab_names:
            storage_locations_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(storage_locations_tab, text='Storage Locations')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_distributors_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Distributors' not in tab_names:
            distributors_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(distributors_tab, text='Distributors')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_users_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Users' not in tab_names:
            users_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(users_tab, text='Users')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_part_measurement_units_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Part Measurement Units' not in tab_names:
            part_measurement_units_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(part_measurement_units_tab, text='Part Measurement Units')
            self.custom_notebook.pack(expand=1, fill="both")

    def open_units_tab(self):
        tab_names = self.get_tab_names(self)
        if 'Units' not in tab_names:
            units_tab = tk.Frame(self.custom_notebook)
            self.custom_notebook.add(units_tab, text='Units')
            self.custom_notebook.pack(expand=1, fill="both")
            ProjectController.setup(units_tab)

