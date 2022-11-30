from tkinter import ttk
import tkinter.font as tk_font
import tkinter as tk


class PartsManagementForm(tk.Frame):
    """Parts Management Form"""
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
        self.treeview = ttk.Treeview(self.left_frame, show='headings', height=35)
        self.treeview['columns'] = ('Name', 'Description', 'Storage Location', 'Status', 'Condition', 'Stock',
                                    'Min. Stock', 'Avg. Price', 'Footprint', 'Internal ID')

        self.set_headers(self.treeview['columns'])

        self.scrollbar = tk.Scrollbar(self.right_frame, orient=tk.VERTICAL)
        self.treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.treeview.yview())

        # Layout
        self.treeview.pack(fill=tk.BOTH, expand=1)
        self.scrollbar.pack(fill=tk.Y, expand=1)

        self.load_records()

    def load_records(self):
        """Load records into the form"""
        for key, record in self.data.items():
            self.treeview.insert('', 'end', iid=key, text='Part ID: {}'.format(key),
                                 values=[record['Name'], record['Description'], record['Storage Location'],
                                         record['Status'], record['Condition'], record['Stock'], record['Min. Stock'],
                                         record['Avg. Price'], record['Footprint'], record['Internal ID']])

    def set_headers(self, columns):
        """Set headers of the Treeview"""
        self.treeview.configure(columns=columns)
        for i, col in enumerate(columns):
            column_width = tk_font.Font().measure(col.title())
            self.treeview.heading(i, text=col)
            self.treeview.column(i, width=column_width, stretch=True)
