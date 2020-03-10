#!/usr/bin/env python3

import MySQLdb


def insert_into_table(table_name, data):
    db = MySQLdb.connect(host="localhost", user="innref", passwd="innref", db="innref")
    cursor = db.cursor()
    try:
        query = "INSERT INTO " + table_name + "("
        values = "VALUES ("
        sep = ""
        for key, value in data.items():
            query = query + sep + key
            values = values + sep + "'" + value + "'"
            sep = ", "
        query = query + ") " + values + ") "
        cursor.execute(query)
        db.commit()
        db.close()
        print("message: success creating {} on {}".format(data, table_name))
        return {'message': "success creating {} on {}".format(data, table_name)}
    except:
        db.close()
        print("error: Missing foreign key")
        return {'error': 'Missing foreign key'}
