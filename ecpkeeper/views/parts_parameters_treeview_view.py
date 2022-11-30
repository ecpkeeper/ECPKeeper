from tkinter import ttk
import tkinter.font as tk_font
import tkinter as tk


class PartParametersForm(tk.Frame):
    """Part Parameters Form"""
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.data = data

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
        self.treeview['columns'] = ('Parameter', 'Min Value', 'Nominal Value', 'Max Value', 'Unit', 'Description')

        self.set_headers(self.treeview['columns'])

        self.scrollbar = tk.Scrollbar(self.right_frame, orient=tk.VERTICAL)
        self.treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview())

        # Layout
        self.add_button.pack(side=tk.LEFT)
        self.delete_button.pack(side=tk.LEFT)
        self.treeview.pack(fill=tk.BOTH, expand=1)
        self.scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.treeview.insert('', 'end', iid=key, text='PartParameter ID: {}'.format(key),
                                 values=[record['Parameter'], record['Min Value'], record['Nominal Value'],
                                         record['Max Value'], record['Unit'], record['Description']])

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.treeview.heading(i, text=col)
            self.treeview.column(i, width=column_width, stretch=True)
