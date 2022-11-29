from tkinter import ttk
import tkinter as tk


class PartsManagementView(tk.Frame):
    def __init__(self, parent, data, callbacks, **kwargs):
        super().__init__(parent, **kwargs)
        self.data = data
        self.treeview = ttk.Treeview(self, columns=('Name', 'Description', 'Storage Location', 'Status', 'Condition',
                                                    'Stock', 'Min. Stock', 'Avg. Price', 'Footprint', 'Internal ID'))
        self.treeview.heading('Name', text='Name')
        self.treeview.heading('Description', text='Description')
        self.treeview.heading('Storage Location', text='Storage Location')
        self.treeview.heading('Status', text='Status')
        self.treeview.heading('Condition', text='Condition')
        self.treeview.heading('Stock', text='Stock')
        self.treeview.heading('Min. Stock', text='Min. Stock')
        self.treeview.heading('Avg. Price', text='Avg. Price')
        self.treeview.heading('Footprint', text='Footprint')
        self.treeview.heading('Internal ID', text='Internal ID')
        # Layout
        self.treeview.grid(row=0, column=0)
        self.load_records()

    def load_records(self):
        for key, record in self.data.items():
            self.treeview.insert('', 'end', iid=key, text='Part ID: {}'.format(key),
                                 values=[record['Name'], record['Description'], record['Storage Location'],
                                         record['Status'], record['Condition'], record['Stock'], record['Min. Stock'],
                                         record['Avg. Price'], record['Footprint'], record['Internal ID']])
