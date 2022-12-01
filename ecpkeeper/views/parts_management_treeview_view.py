from tkinter import ttk
import tkinter.font as tk_font
import tkinter as tk


class PartsManagementForm(tk.Frame):
    """Parts Management Form"""
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
        self.treeview = ttk.Treeview(self.left_frame, show='headings', height=35)
        self.treeview['columns'] = ('Name', 'Description', 'Storage Location', 'Status', 'Condition', 'Stock',
                                    'Min. Stock', 'Avg. Price', 'Footprint', 'Internal ID')
=======
        self.callbacks = callbacks

        wrapper_frame = self
        wrapper_frame.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        parts_management_upper_frame = tk.Frame(wrapper_frame)
        parts_management_upper_frame.pack(fill=tk.X, side=tk.TOP)
        parts_management_lower_frame = tk.Frame(wrapper_frame, bg='black')
        parts_management_lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        parts_management_left_frame = tk.Frame(parts_management_lower_frame)
        parts_management_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        parts_management_right_frame = tk.Frame(parts_management_lower_frame)
        parts_management_right_frame.pack(side=tk.LEFT, fill=tk.Y)

        parts_management_add = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/add-24.png')
        parts_management_delete = tk.PhotoImage(
            file=f'{Path.cwd()}/ecpkeeper/ecpkeeper/assets/images/file-delete-24.png')

        parts_management_add_button = ttk.Button(parts_management_upper_frame,
                                                 text='Add',
                                                 image=parts_management_add,
                                                 compound=tk.LEFT)
        parts_management_delete_button = ttk.Button(parts_management_upper_frame,
                                                    text='Delete',
                                                    image=parts_management_delete,
                                                    compound=tk.LEFT)

        self.parts_management_treeview = ttk.Treeview(parts_management_left_frame,
                                                      show='headings',
                                                      height=35)
        self.parts_management_treeview['columns'] = ('Name',
                                                     'Description',
                                                     'Storage Location',
                                                     'Status',
                                                     'Condition',
                                                     'Stock',
                                                     'Min. Stock',
                                                     'Avg. Price',
                                                     'Footprint',
                                                     'Internal ID')
>>>>>>> Stashed changes

        self.set_headers(self.parts_management_treeview['columns'])

<<<<<<< Updated upstream
        self.scrollbar = tk.Scrollbar(self.right_frame, orient=tk.VERTICAL)
        self.treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview())

        # Layout
        self.treeview.pack(fill=tk.BOTH, expand=1)
        self.scrollbar.pack(fill=tk.Y, expand=1)
=======
        scrollbar = tk.Scrollbar(parts_management_right_frame, orient=tk.VERTICAL)
        self.parts_management_treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.parts_management_treeview.yview())

        # Layout
        parts_management_add_button.pack(side=tk.LEFT)
        parts_management_delete_button.pack(side=tk.LEFT)
        self.parts_management_treeview.pack(fill=tk.BOTH, expand=1)
        scrollbar.pack(fill=tk.Y, expand=1)
>>>>>>> Stashed changes

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
<<<<<<< Updated upstream
            self.treeview.insert('', 'end', iid=key, text='Part ID: {}'.format(key),
                                 values=[record['Name'], record['Description'], record['Storage Location'],
                                         record['Status'], record['Condition'], record['Stock'], record['Min. Stock'],
                                         record['Avg. Price'], record['Footprint'], record['Internal ID']])
=======
            self.parts_management_treeview.insert('', 'end',
                                                  iid=key,
                                                  text=f'Part ID: {key}',
                                                  values=[record['Name'],
                                                          record['Description'],
                                                          record['Storage Location'],
                                                          record['Status'],
                                                          record['Condition'],
                                                          record['Stock'],
                                                          record['Min. Stock'],
                                                          record['Avg. Price'],
                                                          record['Footprint'],
                                                          record['Internal ID']])
>>>>>>> Stashed changes

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.parts_management_treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.parts_management_treeview.heading(i, text=col)
            self.parts_management_treeview.column(i, width=column_width, stretch=True)
