
import ZODB, ZODB.FileStorage
import persistent
import persistent.list
import transaction

class Course(persistent.Persistent):
    def __init__(self, id, name = "", credit = 0):
        self.name = name
        self.id = id
        self.credit = credit
        self.gradeScheme = persistent.list.PersistentList()
        self.gradeScheme.append({"Grade" : "A", "Min" : 80, "Max" : 100})
        self.gradeScheme.append({"Grade" : "B", "Min" : 70, "Max" : 79})
        self.gradeScheme.append({"Grade" : "C", "Min" : 60, "Max" : 69})
        self.gradeScheme.append({"Grade" : "D", "Min" : 50, "Max" : 59})
        self.gradeScheme.append({"Grade" : "F", "Min" : 0, "Max" : 49})

    def __str__(self):
        return "ID : " + self.id + "\nName : " + self.name + "\nCredit : " + str(self.credit)

    def getCredit(self):
        return self.credit

    def getName(self):
        return self.name

    def getID(self):
        return str(self.id)

    def setName(self, name):
        self.name = name

    def printDetail(self):
        print(self.__str__())

    def scoreGrading(self, score):
        for grade in self.gradeScheme:
            if score >= grade["Min"] and score <= grade["Max"]:
                return grade["Grade"]

    def setGradeScheme(self, gradeScheme):
        if len(gradeScheme) == 5:
            for grade in gradeScheme:
                if "Grade" not in grade or "Min" not in grade or "Max" not in grade:
                    return False
            self.gradeScheme = gradeScheme


class Enrollment(persistent.Persistent):
    def __init__(self, student, course, score = 0):
        self.student = student
        self.course = course
        self.score = score

    def __str__(self):
        return "Student : " + self.student.getName() + "\nCourse : " + self.course.getName() + "\nGrade : " + str(self.getGrade())

    def getCourse(self):
        return self.course

    def getScore (self):
        return self.score

    def getGrade(self):
        return self.course.scoreGrading(self.getScore())

    def setScore(self, score):
        self.score = score


    def printDetail(self):
        print(self.__str__())

class Student(persistent.Persistent):
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.password = ""
        self.enrolls = persistent.list.PersistentList()

    def __str__(self):
        returnn = "Transcript\n"
        returnn += "ID : " + self.getID() + " Name : " + self.name + "\n"
        returnn += "Course List\n"
        # print("Transcript")
        # print("ID : " + self.getID() + " Name : " + self.name)
        # print("Course List")
        gpa = 0
        credits = 0
        for enroll in self.enrolls:
            match enroll.getGrade():
                case "A":
                    gpa += 4 * enroll.getCourse().getCredit()
                case "B":
                    gpa += 3 * enroll.getCourse().getCredit()
                case "C":
                    gpa += 2 * enroll.getCourse().getCredit()
                case "D":
                    gpa += 1 * enroll.getCourse().getCredit()

            credits += enroll.getCourse().getCredit()
            returnn += "ID : " + enroll.getCourse().getID() + " Course : " + enroll.getCourse().getName() + " Credit : " + str(enroll.getCourse().getCredit()) + " Score : " + str(enroll.getScore()) + " Grade : " + enroll.getGrade() + "\n"
        gpa /= credits
        returnn += "GPA : " + str(format(gpa, '.2f'))
        return returnn

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getID(self):
        return str(self.id)


    def enrollCourse(self, course, score = 0):
        enroll = Enrollment(self, course, score)
        print("Enrolling " + enroll.getCourse().getName() + " for " + self.name + "\n")
        self.enrolls.append(enroll)

    def printDetail(self):
        print(self.__str__())

    def printTranscript(self):
        print(self.__str__())

    def getEnrollment(self):
        return self.enrolls

    def login(id, password):
        if self.id == id and self.password == password:
            return True
        return False