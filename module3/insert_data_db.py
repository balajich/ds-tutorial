# import sqlite3 package
import sqlite3


def insert_db():
    # sample data
    classroom_data = [(1, "Raj", "M", 70, 84, 92),
                      (2, "Poonam", "F", 87, 69, 93),
                      (3, "Nik", "M", 65, 83, 90),
                      (4, "Rahul", "F", 83, 76, 89)]
    # open connection
    connection = sqlite3.connect("classroomDB.db")
    # open cursor
    cursor = connection.cursor()
    # insert each student record
    for student in classroom_data:
        # formatted query string
        insert_statement = """INSERT INTO classroom 
                          (student_id, name, gender, physics_marks, chemistry_marks, mathematics_marks)
                          VALUES 
                          ({0}, "{1}", "{2}", {3}, {4}, {5});""".format(student[0], student[1], student[2],
                                                                        student[3], student[4], student[5])
        # execute insert query
        cursor.execute(insert_statement)

    # commit the changes
    connection.commit()
    # close the connection
    connection.close()


if __name__ == "__main__":
    print("Creating Data Base")
    insert_db()
