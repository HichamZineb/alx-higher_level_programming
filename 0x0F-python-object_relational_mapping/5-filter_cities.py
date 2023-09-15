#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (arv[4],)
    )

    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
