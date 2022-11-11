import sqlite3 as sql
from ChromosomeDB.create_tables import create_tables

if __name__ == "__main__":
    conn = sql.connect('database.db')
    cursor = conn.cursor()

    # create_tables(cursor)
    # conn.commit()

    cursor.execute("""SELECT * from gene;""")

    print("Table: {}".format(cursor.fetchall()))

    conn.close()