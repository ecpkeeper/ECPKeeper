import sqlite3

# backend

conn = sqlite3.connect('../var/ecpkeeper.db')


class PartModel:

    @staticmethod
    def add_part(name, description, category_id, minimum_stock, measurement_unit_id,
                 footprint_id, storage_location_id, comment, production_remarks, status,
                 needs_review, condition, internal_part_number):
        cur = conn.cursor()
        with conn:
            cur.execute('insert into part values (null, ?,?,?,?,?,?,?,?,?,?,?,?,?)', (name, description, category_id,
                        minimum_stock, measurement_unit_id, footprint_id, storage_location_id, comment,
                        production_remarks,
                        status, needs_review, condition, internal_part_number))
        conn.close()

    @staticmethod
    def view_part_data():
        cur = conn.cursor()
        with conn:
            cur.execute('select * from part')
            rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_part_data(part_id):
        cur = conn.cursor()
        with conn:
            cur.execute('delete from part where id=?', (part_id,))
        conn.close()

    @staticmethod
    def search_part_data(name="", description="", category_id="", minimum_stock="", measurement_unit_id="",
                         footprint_id="", storage_location_id="", comment="", production_remarks="", status="",
                         needs_review="", condition="", internal_part_number=""):
        cur = conn.cursor()
        with conn:
            cur.execute('select * from part where name = ? or description = ? or categoryid = ? or \
                        minimumstock = ? or measurementunitid = ? or footprintid = ? or storagelocationid = ? or \
                        comment = ? or productionremarks = ? or status = ? or \
                        needsreview = ? or condition = ? or internalpartnumber = ?', (name, description, category_id,
                                                                                      minimum_stock,
                                                                                      measurement_unit_id,
                                                                                      footprint_id, storage_location_id,
                                                                                      comment, production_remarks,
                                                                                      status, needs_review, condition,
                                                                                      internal_part_number))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def update_part_data(part_id, name="", description="", category_id="", minimum_stock="", measurement_unit_id="",
                         footprint_id="", storage_location_id="", comment="", production_remarks="", status="",
                         needs_review="", condition="", internal_part_number=""):
        cur = conn.cursor()
        with conn:
            cur.execute('update part set name = ?, description = ?, categoryid = ?, minimumstock = ?, \
                        measurementunitid = ?, footprintid = ?, storagelocationid = ?, comment = ?, productionremarks = ?, \
                        status = ?, needsreview = ?, condition = ?, internalpartnumber = ? where id=?',
                        (name, description, category_id, minimum_stock,
                         measurement_unit_id, footprint_id,
                         storage_location_id, comment, production_remarks,
                         status, needs_review, condition,
                         internal_part_number, part_id))
        conn.close()
