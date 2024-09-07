import ZODB, ZODB.FileStorage
import transaction
import BTrees.OOBTree
import persistent
import persistent.list
from classes import Course, Student, Enrollment

def initialize_database():
    # Open or create a ZODB database file 'mydata.fs'
    storage = ZODB.FileStorage.FileStorage('D:\Main\Work\KMITL\Yr2_Sem1\WebProgramming\lab\lab11\mydata\mydata.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    # Create and store objects in the database
    if 'courses' not in root:
        root['courses'] = BTrees.OOBTree.BTree()
        root['courses'][101] = Course(101, "Computer Programming", 4)
        root['courses'][201] = Course(201, "Web Programming", 4)
        root['courses'][202] = Course(202, "Software Engineering Principles", 5)
        root['courses'][301] = Course(301, "Artificial Intelligence", 3)

    if 'students' not in root:
        root['students'] = BTrees.OOBTree.BTree()

        root['students'][1101] = Student(1101, "Alice")
        root['students'][1101].enrollCourse(root['courses'][101], 3.5)
        root['students'][1101].enrollCourse(root['courses'][201], 4.0)
        root['students'][1101].enrollCourse(root['courses'][301], 3.0)

        root['students'][1102] = Student(1102, "Zhong")
        root['students'][1102].enrollCourse(root['courses'][101], 3.0)
        root['students'][1102].enrollCourse(root['courses'][201], 3.5)
        root['students'][1102].enrollCourse(root['courses'][202], 4.0)

        root['students'][1103] = Student(1103, "Dvalinn")
        root['students'][1103].enrollCourse(root['courses'][101], 4.0)
        root['students'][1103].enrollCourse(root['courses'][201], 3.5)
        root['students'][1103].enrollCourse(root['courses'][202], 3.0)

    # Commit the transaction to save changes
    transaction.commit()

    return connection, root

if __name__ == "__main__":
    connection, root = initialize_database()

    # Retrieve and print course details
    courses = root['courses']
    for course_id, course in courses.items():
        print(f"Course ID: {course_id}, Name: {course.name}, Credit: {course.credit}")

    # Retrieve and print student details
    students = root['students']
    for student in students.values():
        print("\n")
        student.printTranscript()

    # Close the database connection
    connection.close()
