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
<<<<<<< Updated upstream
    @staticmethod
    def add_category(name, description, parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
=======
    """Category model with all the calls to handle CRUD for Category"""
    def __init__(self, category_id, name, description, parent_id):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.parent_id = parent_id
        self.db_location = '../ecpkeeper.db'

    def add_category(self):
        """ Add Category data to database"""
        conn = sqlite3.connect(self.db_location)
>>>>>>> Stashed changes
        cur = conn.cursor()
        with conn:
            cur.execute('insert into category values (null,?,?,?,?,null)', (self.parent_id, self.name,
                                                                            self.description, current_dateTime))
        conn.close()
        logging.info('Added Category: {} - {} - {}'.format(self.name, self.description, self.parent_id))

<<<<<<< Updated upstream
    @staticmethod
    def view_category_data():
        conn = sqlite3.connect('../ecpkeeper.db')
=======
    def view_category_data(self):
        """Get all Category data from database"""
        conn = sqlite3.connect(self.db_location)
>>>>>>> Stashed changes
        cur = conn.cursor()
        with conn:
            cur.execute('select * from category')
            rows = cur.fetchall()
        conn.close()
        return rows

<<<<<<< Updated upstream
    @staticmethod
    def delete_category_data(id):
        conn = sqlite3.connect('../ecpkeeper.db')
=======
    def delete_category_data(self):
        """Delete Category from database based on id"""
        conn = sqlite3.connect(self.db_location)
>>>>>>> Stashed changes
        cur = conn.cursor()
        with conn:
            cur.execute('delete from category where id=?', (self.category_id,))
        conn.close()

<<<<<<< Updated upstream
    @staticmethod
    def search_category_data(name="", description="", parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
=======
    def search_category_data(self, name="", description="", parent_id=""):
        """Search for Category in database based on different fields"""
        conn = sqlite3.connect(self.db_location)
>>>>>>> Stashed changes
        cur = conn.cursor()
        with conn:
            cur.execute('select * from category where name = ? or description = ? or parentid = ?',
                        (name, description, parent_id,))
        rows = cur.fetchall()
        conn.close()
        return rows

<<<<<<< Updated upstream
    @staticmethod
    def update_category_data(id, name, description, parent_id=""):
        conn = sqlite3.connect('../ecpkeeper.db')
=======
    def update_category_data(self):
        """Update existing Category using id"""
        conn = sqlite3.connect(self.db_location)
>>>>>>> Stashed changes
        cur = conn.cursor()
        with conn:
            cur.execute('update category set ParentId = ? OR Name = ? AND Description = ? AND DateModified = ?  \
            where id=?', (self.parent_id, self.name, self.description, datemodified, self.category_id))
        conn.close()
