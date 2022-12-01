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
import sqlite3

# backend

conn = sqlite3.connect('../var/ecpkeeper.db')


class PartModel:
    """ Part model with all the calls to handle CRUD for Part"""
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-arguments
    def __init__(self, part_id, name, description, category_id,
                 minimum_stock, measurement_unit_id, footprint_id,
                 storage_location_id, comment, production_remarks,
                 status, needs_review, condition, internal_part_number
                 ):
        self.part_id = part_id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.minimum_stock = minimum_stock
        self.measurement_unit_id = measurement_unit_id
        self.footprint_id = footprint_id
        self.storage_location_id = storage_location_id
        self.comment = comment
        self.production_remarks = production_remarks
        self.status = status
        self.needs_review = needs_review
        self.condition = condition
        self.internal_part_number = internal_part_number

    def add_part(self):
        """ Add Part data to database"""
        cur = conn.cursor()
        with conn:
            cur.execute('insert into part values (null, ?,?,?,?,?,?,?,?,?,?,?,?,?)',
                        (self.name, self.description, self.category_id, self.minimum_stock,
                         self.measurement_unit_id, self.footprint_id, self.storage_location_id,
                         self.comment, self.production_remarks, self.status, self.needs_review,
                         self.condition, self.internal_part_number))
        conn.close()

    @staticmethod
    def view_part_data():
        """Get all part data from database"""
        cur = conn.cursor()
        with conn:
            cur.execute('select * from part')
            rows = cur.fetchall()
        conn.close()
        return rows

    def delete_part_data(self):
        """Delete part from database based on id"""
        cur = conn.cursor()
        with conn:
            cur.execute('delete from part where id=?', (self.part_id,))
        conn.close()

    @staticmethod
    def search_part_data(name="", description="", category_id="", minimum_stock="",
                         measurement_unit_id="", footprint_id="", storage_location_id="",
                         comment="", production_remarks="", status="", needs_review="",
                         condition="", internal_part_number=""):
        """Search for part in database based on different fields"""
        cur = conn.cursor()
        with conn:
            cur.execute('select * from part where name = ? or description = ? or \
                        categoryid = ? or minimumstock = ? or measurementunitid = ? \
                        or footprintid = ? or storagelocationid = ? or \
                        comment = ? or productionremarks = ? or status = ? or \
                        needsreview = ? or condition = ? or internalpartnumber = ?',
                        (name, description, category_id, minimum_stock, measurement_unit_id,
                         footprint_id, storage_location_id, comment, production_remarks,
                         status, needs_review, condition, internal_part_number)
                        )
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_part_data(self):
        """Update existing part using id"""
        cur = conn.cursor()
        with conn:
            cur.execute('update part set name = ?, description = ?, categoryid = ?, \
                        minimumstock = ?, measurementunitid = ?, footprintid = ?, \
                        storagelocationid = ?, comment = ?, productionremarks = ?, \
                        status = ?, needsreview = ?, condition = ?, \
                        internalpartnumber = ? where id=?',
                        (self.name, self.description, self.category_id, self.minimum_stock,
                         self.measurement_unit_id, self.footprint_id, self.storage_location_id,
                         self.comment, self.production_remarks, self.status, self.needs_review,
                         self.condition, self.internal_part_number, self.part_id))
        conn.close()
