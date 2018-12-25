# import sqlite3 package
import sqlite3


def read_db():
    # open connection
    connection = sqlite3.connect("classroomDB.db")
    # open cursor
    cursor = connection.cursor()
    # query
    query = "SELECT * FROM classroom"
    # execute query
    cursor.execute(query)
    # fetch results
    result = cursor.fetchall()
    # print results
    for row in result:
        print(row)
    # close connection
    connection.close()


if __name__ == "__main__":
    print("Creating Data Base")
    read_db()
