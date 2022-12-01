from tkinter import ttk
import tkinter.font as tk_font
import tkinter as tk


class ManufacturersForm(tk.Frame):
    """Manufacturers Form"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        manufacturers_upper_frame = tk.Frame(wrapper_frame)
        manufacturers_upper_frame.pack(fill=tk.X, side=tk.TOP)
        manufacturers_lower_frame = tk.Frame(wrapper_frame, bg='black')
        manufacturers_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        manufacturers_left_frame = tk.Frame(manufacturers_lower_frame)
        manufacturers_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        manufacturers_right_frame = tk.Frame(manufacturers_lower_frame)
        manufacturers_right_frame.pack(side=tk.LEFT, fill=tk.Y)

<<<<<<< Updated upstream
        self.add = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\add-24.png")
        self.delete = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\file-delete-24.png")

        self.add_button = ttk.Button(self.upper_frame, text='Add', image=self.add, compound=tk.LEFT)
        self.delete_button = ttk.Button(self.upper_frame, text='Delete', image=self.delete, compound=tk.LEFT)
=======
        manufacturers_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/add-24.png')
        manufacturers_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/assets/images/file-delete-24.png')

        manufacturers_add_button = ttk.Button(manufacturers_upper_frame,
                                              text='Add',
                                              image=manufacturers_add,
                                              compound=tk.LEFT)
        manufacturers_delete_button = ttk.Button(manufacturers_upper_frame,
                                                 text='Delete',
                                                 image=manufacturers_delete,
                                                 compound=tk.LEFT)
>>>>>>> Stashed changes

        self.manufacturers_treeview = ttk.Treeview(manufacturers_left_frame,
                                                   show='headings',
                                                   height=26)
        self.manufacturers_treeview['columns'] = (' Manufacturer  ', ' Part Number  ')

        self.set_headers(self.manufacturers_treeview['columns'])

        scrollbar = tk.Scrollbar(manufacturers_right_frame, orient=tk.VERTICAL)
        self.manufacturers_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.manufacturers_treeview.yview())

        # Layout
        manufacturers_add_button.pack(side=tk.LEFT)
        manufacturers_delete_button.pack(side=tk.LEFT)
        self.manufacturers_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
<<<<<<< Updated upstream
            self.treeview.insert('', 'end', iid=key, text='Manufacturer ID: {}'.format(key),
                                 values=[record['Manufacturer'], record['Part Number']])
=======
            self.manufacturers_treeview.insert('',
                                               'end',
                                               iid=key,
                                               text=f'Manufacturer ID: {key}',
                                               values=[record['Manufacturer'],
                                                       record['Part Number']])
>>>>>>> Stashed changes

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.manufacturers_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.manufacturers_treeview.heading(i, text=col)
            self.manufacturers_treeview.column(i, width=column_width, stretch=True)
