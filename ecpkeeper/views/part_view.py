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


class PartView(tk.Frame):
    """Part view to display adding or editing of Parts"""
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-locals
    def __init__(self, parent, data, callbacks, edit, **kwargs):
        super().__init__(parent, **kwargs)

        self.edit = edit
        self.data = data
        self.callbacks = callbacks
        self.fields = {}
        self.labels = {}

        self.needs_review = tk.IntVar()
        self.enable_footprint = tk.IntVar()
        self.price_per_item = tk.IntVar()

        # Part Tab Labels
        self.name_lbl = tk.Label(self, text='Name: ')
        self.description_lbl = tk.Label(self, text='Description: ')
        self.minimum_stock_lbl = tk.Label(self, text='Minimum Stock: ')
        self.measurement_unit_lbl = tk.Label(self, text='Measurement Unit: ')
        self.category_lbl = tk.Label(self, text='Category: ')
        self.storage_location_lbl = tk.Label(self, text='Storage Location: ')
        self.footprint_lbl = tk.Label(self, text='footprint: ')
        self.comment_lbl = tk.Label(self, text='Comment: ')
        self.production_remarks_lbl = tk.Label(self, text='Production Remarks: ')
        self.status_lbl = tk.Label(self, text='Status: ')
        self.condition_lbl = tk.Label(self, text='Condition: ')
        self.internal_part_number_lbl = tk.Label(self, text='Internal Part Number: ')
        if edit is not True:
            self.initial_stock_level_lbl = tk.Label(self, text='Initial Stock Level: ')
            self.stock_user_lbl = tk.Label(self, text="Stock User: ")
            self.price_lbl = tk.Label(self, text='Price: ')

        # Part Tab widgets
        self.fields['name'] = tk.Entry(self)
        self.fields['description'] = tk.Entry(self)
        self.fields['minimum_stock'] = tk.Entry(self)
        self.fields['measurement_unit'] = tk.Entry(self)
        self.fields['category'] = tk.Entry(self)
        self.fields['storage_location'] = tk.Entry(self)
        self.fields['footprint_checkbutton'] = \
            tk.Checkbutton(self,
                           text="None",
                           variable=self.enable_footprint,
                           onvalue=1,
                           offvalue=0)
        self.fields['footprint'] = tk.Entry(self)
        self.fields['comment'] = tk.Text(self, height=10)
        self.fields['production_remarks'] = tk.Entry(self)
        self.fields['status'] = tk.Entry(self)
        self.fields['status_checkbutton'] = \
            tk.Checkbutton(self,
                           text='Needs Review',
                           variable=self.needs_review,
                           onvalue=1,
                           offvalue=0)
        self.fields['condition'] = tk.Entry(self)
        self.fields['internal_part_number'] = tk.Entry(self)
        if edit is not True:
            self.fields['initial_stock_level_spinbox'] = \
                tk.Spinbox(self, from_=0, to=10000000000000)
            self.fields['stock_user'] = tk.Entry(self)
            self.fields['price_spinbox'] = tk.Spinbox(self, from_=0, to=10000000000000)
            self.fields['price_checkbutton'] = \
                tk.Checkbutton(self,
                               text="Per Item",
                               variable=self.price_per_item,
                               onvalue=1,
                               offvalue=0)

        # Part Grid Layout
        self.name_lbl.grid(column=0, row=0,
                           sticky='w',
                           padx=5,
                           pady=5)
        self.description_lbl.grid(column=0, row=1,
                                  sticky='w',
                                  padx=5,
                                  pady=5)
        self.minimum_stock_lbl.grid(column=0, row=2,
                                    sticky='w',
                                    padx=5,
                                    pady=5)
        self.measurement_unit_lbl.grid(column=5, row=2,
                                       sticky='w',
                                       padx=5,
                                       pady=5)
        self.category_lbl.grid(column=0, row=3,
                               sticky='w',
                               padx=5,
                               pady=5)
        self.storage_location_lbl.grid(column=0, row=4,
                                       sticky='w',
                                       padx=5,
                                       pady=5)
        self.footprint_lbl.grid(column=0, row=5,
                                sticky='w',
                                padx=5,
                                pady=5)
        self.comment_lbl.grid(column=0, row=6,
                              sticky='nw',
                              padx=5,
                              pady=5)
        self.production_remarks_lbl.grid(column=0, row=7,
                                         sticky='w',
                                         padx=5,
                                         pady=5)
        self.status_lbl.grid(column=0, row=8,
                             sticky='w',
                             padx=5,
                             pady=5)
        self.condition_lbl.grid(column=0, row=9,
                                sticky='w',
                                padx=5,
                                pady=5)
        self.internal_part_number_lbl.grid(column=0, row=10,
                                           sticky='w',
                                           padx=5,
                                           pady=5)
        if edit is not True:
            self.initial_stock_level_lbl.grid(column=0, row=11,
                                              sticky='w',
                                              padx=5,
                                              pady=5)
            self.stock_user_lbl.grid(column=5, row=11,
                                     sticky='w',
                                     padx=5,
                                     pady=5)
            self.price_lbl.grid(column=0, row=12,
                                sticky='w',
                                padx=5,
                                pady=5)

        self.fields['name'].grid(column=1, row=0,
                                 columnspan=10,
                                 padx=5,
                                 pady=5,
                                 sticky='we')
        self.fields['description'].grid(column=1, row=1,
                                        columnspan=10,
                                        padx=5,
                                        pady=5,
                                        sticky='we')
        self.fields['minimum_stock'].grid(column=1, row=2,
                                          columnspan=4,
                                          padx=5,
                                          pady=5,
                                          sticky='we')
        self.fields['measurement_unit'].grid(column=6, row=2,
                                             columnspan=5,
                                             padx=5,
                                             pady=5,
                                             sticky='we')
        self.fields['category'].grid(column=1, row=3,
                                     columnspan=10,
                                     padx=5,
                                     pady=5,
                                     sticky='we')
        self.fields['storage_location'].grid(column=1, row=4,
                                             columnspan=10,
                                             padx=5,
                                             pady=5,
                                             sticky='we')
        self.fields['footprint_checkbutton'].grid(column=1, row=5,
                                                  columnspan=1,
                                                  padx=5,
                                                  pady=5,
                                                  sticky='we')
        self.fields['footprint'].grid(column=2, row=5,
                                      columnspan=10,
                                      padx=5,
                                      pady=5,
                                      sticky='we')
        self.fields['comment'].grid(column=1, row=6,
                                    columnspan=10,
                                    padx=5,
                                    pady=5,
                                    sticky='nswe')
        self.fields['production_remarks'].grid(column=1, row=7,
                                               columnspan=10,
                                               padx=5,
                                               pady=5,
                                               sticky='we')
        self.fields['status'].grid(column=1, row=8,
                                   columnspan=7,
                                   padx=5,
                                   pady=5,
                                   sticky='we')
        self.fields['status_checkbutton'].grid(column=8, row=8,
                                               columnspan=1,
                                               padx=5,
                                               pady=5,
                                               sticky='e')
        self.fields['condition'].grid(column=1, row=9,
                                      columnspan=10,
                                      padx=5,
                                      pady=5,
                                      sticky='we')
        self.fields['internal_part_number'].grid(column=1, row=10,
                                                 columnspan=10,
                                                 padx=5,
                                                 pady=5,
                                                 sticky='we')
        if edit is not True:
            self.fields['initial_stock_level_spinbox'].grid(column=1, row=11,
                                                            columnspan=4,
                                                            padx=5,
                                                            pady=5,
                                                            sticky='we')
            self.fields['stock_user'].grid(column=6, row=11,
                                           columnspan=5,
                                           padx=5,
                                           pady=5,
                                           sticky='we')
            self.fields['price_spinbox'].grid(column=1, row=12,
                                              columnspan=9,
                                              padx=5,
                                              pady=5,
                                              sticky='we')
            self.fields['price_checkbutton'].grid(column=10, row=12,
                                                  columnspan=1,
                                                  padx=5,
                                                  pady=5,
                                                  sticky='we')

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)
        self.columnconfigure(8, weight=1)
        self.columnconfigure(9, weight=1)
        self.columnconfigure(10, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)
        self.rowconfigure(12, weight=1)
        self.rowconfigure(13, weight=1)
        self.rowconfigure(14, weight=1)

        self.load_records()

    def load_records(self):
        """Load part data from database into the edit Frame"""
        for key, record in self.data.items():
            print(f'Key: {key}, Value: {record}')
            print(f'Values in self.fields: {self.fields.values()}')
            if key == 'footprint_checkbutton':
                self.enable_footprint.set(record)
            elif key == 'status_checkbutton':
                self.needs_review.set(record)
            else:
                self.fields[key].insert(tk.END, record)

    def get(self):
        """Saving data to the database"""
        name = self.fields['name'].get()
        description = self.fields['description'].get()
        minimum_stock = self.fields['minimum_stock'].get()
        measurement_unit = self.fields['measurement_unit'].get()
        category = self.fields['category'].get()
        storage_location = self.fields['storage_location'].get()
        footprint_checkbutton = self.enable_footprint.get()
        footprint = self.fields['footprint'].get()
        production_remarks = self.fields['production_remarks'].get()
        status = self.fields['status'].get()
        status_checkbutton = self.needs_review.get()
        condition = self.fields['condition'].get()
        internal_part_number = self.fields['internal_part_number'].get()
        if self.edit is not True:
            initial_stock_level_spinbox = \
                self.fields['initial_stock_level_spinbox'].get()
            stock_user = self.fields['stock_user'].get()
            price_spinbox = self.fields['price_spinbox'].get()
            price_checkbutton = self.price_per_item.get()

            self.data = {
                'name': name,
                'description': description,
                'minimum_stock': minimum_stock,
                'measurement_unit': measurement_unit,
                'category': category,
                'storage_location': storage_location,
                'footprint_checkbutton': footprint_checkbutton,
                'footprint': footprint,
                'production_remarks': production_remarks,
                'status': status,
                'status_checkbutton': status_checkbutton,
                'condition': condition,
                'internal_part_number': internal_part_number,
                'initial_stock_level_spinbox': initial_stock_level_spinbox,
                'stock_user': stock_user,
                'price_spinbox': price_spinbox,
                'price_checkbutton': price_checkbutton,
            }
        else:
            self.data = {
                'name': name,
                'description': description,
                'minimum_stock': minimum_stock,
                'measurement_unit': measurement_unit,
                'category': category,
                'storage_location': storage_location,
                'footprint_checkbutton': footprint_checkbutton,
                'footprint': footprint,
                'production_remarks': production_remarks,
                'status': status,
                'status_checkbutton': status_checkbutton,
                'condition': condition,
                'internal_part_number': internal_part_number,
            }

        return self.data
