import sqlite3 as sql

def display(table, cursor):
    cursor.execute("SELECT * FROM {}".format(table))
    # print("{}: {}".format(table, cursor.fetchall()))
    for row in cursor.fetchall():
        print("{}: {}".format(table, row))

def display_att(table, att, boolean, result, cursor):
    cursor.execute("SELECT * FROM {} WHERE {} {} {}".format(table, att, boolean, result))
    for row in cursor.fetchall():
        print("{}: {}".format(table, row))