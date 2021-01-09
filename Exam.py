class Student:

    def __init__(self, name, course, group, headmen, subjects, grades, ec):
        self.name = name
        self.course = course
        self.group = group
        self.headmen = headmen
        self.subjects = subjects
        self.grades = grades
        self.ec = ec

    def get_average_grade(self):
        s = k = 0
        for i in self.grades:
            s += int(i)
            k += 1
        return s/k


if __name__ == '__main__':
    with open("D:\МФТИ\Информатика\Students.txt", "r") as file:
        for line in file:
            if line[:8] == 'Student:':
                name = line[9:]
                name = name[:(len(name)-1)]
            if line[:7] == 'Course:':
                course = line[8:]
                course = course[:(len(course) - 1)]
            if line[:6] == 'Group:':
                group = line[7:]
                group = group[:(len(group) - 1)]
            if line[:8] == 'Headmen:':
                a = line[9:]
                a = a[:(len(a) - 1)]
                if a == 'yes':
                    headmen = True
                else:
                    headmen = False
            if line[:9] == 'Subjects:':
                b = line[10:]
                b = b[:(len(b) - 1)]
                subjects = b.split()
            if line[:7] == 'Grades:':
                c = line[8:]
                c = c[:(len(c) - 1)]
                grades = c.split()
            if line[:17] == 'Elective courses:':
                d = line[18:]
                d = d[:(len(d) - 1)]
                ec = d.split()
            if line == '':
                pass
    # print(name, course, group, headmen, subjects, grades, ec)
    s = Student(name, course, group, headmen, subjects, grades, ec)
    print(s.get_average_grade())