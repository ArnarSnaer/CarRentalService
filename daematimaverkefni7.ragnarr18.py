class Person(object):
    def __init__(self, name="", userName="", SSN=0):
        self.name = name
        self.userName = userName
        self.SSN = SSN
    
    def getName(self):
        return self.name
    
    def getUserName(self):
        return self.userName

    
    def getSSN(self):
        return self.SSN

class Student(Person):
    def __init__(self, name="", userName="", SSN=0, department=""):
        Person.__init__(self, name="", userName="", SSN=0)
        self.department = department

    def getDepartment(self):
        return self.department


class Professor(Person):
    def __init__(self, name="", userName="", SSN=0, position=""):
        Person.__init__(self, name="", userName="", SSN=0)
        self.position = position

    def getPosition(self):
        return self.position

class Course(object):
    def __init__(self, name="", students=[], professor):
        self.name = name
        self.students = students
        self.professor = professor
    
    def getName(self):
        return self.name.getName

    def getStudents(self):
        return self.students
    
    def getProfessor(self):
        return self.professor