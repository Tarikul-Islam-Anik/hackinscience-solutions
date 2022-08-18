class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_exam(self, mark):
        self.marks.append(float(mark))

    def get_mean(self):
        return float(sum(self.marks)) / max(len(self.marks), 1)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_mean(self):
        if len(self.students) == 0:
            return None
        means_of_each_student = []
        for student in self.students:
            means_of_each_student.append(student.get_mean())
        return sum(means_of_each_student) / len(means_of_each_student)

    def get_best_student(self):
        best_student_mean = 0
        best_student = None
        for student in self.students:
            if student.get_mean() > best_student_mean:
                best_student_mean = student.get_mean()
                best_student = student
        return best_student


class City:
    def __init__(self, name):
        self.name = name
        self.schools = []

    def add_school(self, school):
        self.schools.append(school)

    def get_mean(self):
        if len(self.schools) == 0:
            return None
        means_of_each_school = []
        for school in self.schools:
            if len(school.students) == 0:
                return None
            for student in school.students:
                means_of_each_school.append(student.get_mean())
        return sum(means_of_each_school) / len(means_of_each_school)

    def get_best_school(self):
        best_school_mean = 0
        best_school = None
        if len(self.schools) == 0:
            return None
        for school in self.schools:
            if school.get_mean() > best_school_mean:
                best_school_mean = school.get_mean()
                best_school = school
        return best_school

    def get_best_student(self):
        best_student_mean = 0
        best_student = None
        for school in self.schools:
            if len(school.students) == 0:
                return None
            for student in school.students:
                if student.get_mean() > best_student_mean:
                    best_student_mean = student.get_mean()
                    best_student = student
        return best_student
