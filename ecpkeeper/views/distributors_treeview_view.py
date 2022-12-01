from tkinter import ttk
import tkinter.font as tk_font
import tkinter as tk


class DistributorsForm(tk.Frame):
    """Distributors Form"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)

        self.data = data

<<<<<<< Updated upstream
        self.wrapper_frame = self
        self.wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.upper_frame = tk.Frame(self.wrapper_frame)
        self.upper_frame.pack(fill=tk.X, side=tk.TOP)
        self.lower_frame = tk.Frame(self.wrapper_frame, bg='black')
        self.lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        self.left_frame = tk.Frame(self.lower_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.right_frame = tk.Frame(self.lower_frame)
        self.right_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.add = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\add-24.png")
        self.delete = tk.PhotoImage(
            file=r"C:\code\python\src\github.com\DOS1986\ECPKeeper\ecpkeeper\assets\images\file-delete-24.png")

        self.add_button = ttk.Button(self.upper_frame, text='Add', image=self.add, compound=tk.LEFT)
        self.delete_button = ttk.Button(self.upper_frame, text='Delete', image=self.delete, compound=tk.LEFT)

        self.treeview = ttk.Treeview(self.left_frame, show='headings', height=26)
        self.treeview['columns'] = ('Distributor', 'Order Number', 'Packaging Unit', 'Status',
                                    'Price Per Item', 'Currency', 'Package Price', 'SKU', 'Pricing')
=======
        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        distributors_upper_frame = tk.Frame(wrapper_frame)
        distributors_upper_frame.pack(fill=tk.X, side=tk.TOP)
        distributors_lower_frame = tk.Frame(wrapper_frame, bg='black')
        distributors_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        distributors_left_frame = tk.Frame(distributors_lower_frame)
        distributors_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        distributors_right_frame = tk.Frame(distributors_lower_frame)
        distributors_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        distributors_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/add-24.png')
        distributors_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/file-delete-24.png')

        distributors_add_button = ttk.Button(distributors_upper_frame,
                                             text='Add',
                                             image=distributors_add,
                                             compound=tk.LEFT)
        distributors_delete_button = ttk.Button(distributors_upper_frame,
                                                text='Delete',
                                                image=distributors_delete,
                                                compound=tk.LEFT)

        self.distributors_treeview = ttk.Treeview(distributors_left_frame,
                                                  show='headings',
                                                  height=26)
        self.distributors_treeview['columns'] = ('Distributor',
                                                 'Order Number',
                                                 'Packaging Unit',
                                                 'Status',
                                                 'Price Per Item',
                                                 'Currency',
                                                 'Package Price',
                                                 'SKU',
                                                 'Pricing')
>>>>>>> Stashed changes

        self.set_headers(self.distributors_treeview['columns'])

<<<<<<< Updated upstream
        self.scrollbar = tk.Scrollbar(self.right_frame, orient=tk.VERTICAL)
        self.treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview())

        # Layout
        self.add_button.pack(side=tk.LEFT)
        self.delete_button.pack(side=tk.LEFT)
        self.treeview.pack(fill=tk.BOTH, expand=1)
        self.scrollbar.pack(fill=tk.Y, expand=1)
=======
        scrollbar = tk.Scrollbar(distributors_right_frame, orient=tk.VERTICAL)
        self.distributors_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.distributors_treeview.yview())

        # Layout
        distributors_add_button.pack(side=tk.LEFT)
        distributors_delete_button.pack(side=tk.LEFT)
        self.distributors_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)
>>>>>>> Stashed changes

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
<<<<<<< Updated upstream
            self.treeview.insert('', 'end', iid=key, text='Distributor ID: {}'.format(key),
                                 values=[record['Distributor'], record['Order Number'], record['Packaging Unit'],
                                         record['Status'], record['Price Per Item'], record['Currency'],
                                         record['Package Price'], record['SKU'], record['Pricing']])
=======
            self.distributors_treeview.insert('',
                                              'end',
                                              iid=key,
                                              text=f'Distributor ID: {key}',
                                              values=[record['Distributor'],
                                                      record['Order Number'],
                                                      record['Packaging Unit'],
                                                      record['Status'],
                                                      record['Price Per Item'],
                                                      record['Currency'],
                                                      record['Package Price'],
                                                      record['SKU'],
                                                      record['Pricing']]
                                              )
>>>>>>> Stashed changes

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.distributors_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
<<<<<<< Updated upstream
            self.treeview.heading(i, text=col)
            self.treeview.column(i, width=column_width, stretch=True)
=======
            self.distributors_treeview.heading(i, text=col)
            self.distributors_treeview.column(i, width=column_width, stretch=True)
>>>>>>> Stashed changes
