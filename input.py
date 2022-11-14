def input_to(table, values, cursor):
    cursor.execute("INSERT INTO {} VALUES({})".format(table, values))

def delete_from(table, att, boolean, result, cursor):
    cursor.execute("DELETE FROM {} WHERE {} {} {}".format(table, att, boolean, result))