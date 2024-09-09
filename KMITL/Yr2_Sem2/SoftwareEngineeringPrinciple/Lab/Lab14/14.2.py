
class Program:
    def __init__(self, name, level, start, courses):
        self.level = level
        self.name = name
        self.start = start
        self.courses = {}
        for c in courses:
            self.courses[c.id] = c

    def addCourse(self, course):
        self.courses[course.id] = course

    def getCourse(self, id):
        return self.courses[id]

class Course:
    def __init__(self, idd, name, credit, semester, lecturer, student_list, takes):
        self.credit = credit
        self.id = idd
        self.lecturer = lecturer
        self.name = name
        self.semester = semester
        self.student_list = student_list
        self.takes = takes

    def enroll(self, student):
        self.student_list.append(student)

    def getCredit(self):
        return self.credit

    def getLecturer(self):
        return self.lecturer

    def getStudents(self):
        return self.student_list


class Lecturer:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def getCourse(self):
        return self.courses

class Student:
    def __init__(self, name, status, id, takes):
        self.name = name
        self.status = status
        self.id = id
        self.takes = takes

class University:
    def __init__(self, name, student_list, program_list):
        self.name = name
        self.student_list = {}
        for s in student_list:
            self.student_list[s.id] = s
        self.program_list = program_list

    def getStudent(self, id):
        return self.student_list[id]

class Takes:
    def __init__(self, student, course, grade, score, transcript):
        self.student = student
        self.course = course
        self.grade = grade
        self.score = score
        self.transcript = transcript

class Transcript:
    def __init__(self, complete, issue_date):
        self.complete = complete
        self.issue_date = issue_date

    def printTranscript(self):
        print("Complete status: ", self.complete)
        print("Issue date: ", self.issue_date)

if __name__ == "__main__":
    pass