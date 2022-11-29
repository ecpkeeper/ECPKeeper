import sqlite3
from datetime import datetime
import logging

# backend

current_dateTime = datetime.now()
datemodified = datetime.now()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')

file_handler = logging.FileHandler('../logs/models/category_model.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class CategoryModel:
    @staticmethod
    def add_category(name, description, parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
        cur = conn.cursor()
        with conn:
            cur.execute('insert into category values (null,?,?,?,?,null)', (parent_id, name,
                                                                            description, current_dateTime))
        conn.close()
        logging.info('Added Category: {} - {} - {}'.format(name, description, parent_id))

    @staticmethod
    def view_category_data():
        conn = sqlite3.connect('../ecpkeeper.db')
        cur = conn.cursor()
        with conn:
            cur.execute('select * from category')
            rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_category_data(id):
        conn = sqlite3.connect('../ecpkeeper.db')
        cur = conn.cursor()
        with conn:
            cur.execute('delete from category where id=?', (id,))
        conn.close()

    @staticmethod
    def search_category_data(name="", description="", parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
        cur = conn.cursor()
        with conn:
            cur.execute('select * from category where name = ? or description = ? or parentid = ?',
                        (name, description, parent_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def update_category_data(id, name, description, parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
        cur = conn.cursor()
        with conn:
            cur.execute('update category set ParentId = ? OR Name = ? AND Description = ? AND DateModified = ?  \
            where id=?', (parent_id, name, description, datemodified, id))
        conn.close()
