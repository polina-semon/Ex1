with open("D:\МФТИ\Информатика\Students1.txt", "w") as file1:
    pass

def write_in_file(line):
    with open("D:\МФТИ\Информатика\Students1.txt", "a") as file1:
        if line[:8] == 'Student:':
            file1.write(line)
        elif line[:7] == 'Course:':
            file1.write(line)
        elif line[:6] == 'Group:':
            file1.write(line)
        elif line[:8] == 'Headmen:':
            file1.write(line)
        elif line[:9] == 'Subjects:':
            file1.write(line)
        elif line[:7] == 'Grades:':
            file1.write(line)
        elif line[:17] == 'Elective courses:':
            file1.write(line)


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

    def set_new_grade(self):
        print("Write subject:")
        sub = input()
        self.subjects.append(sub)
        print("Write grade:")
        gra = int(input())
        self.grades.append(gra)
        return self.subjects, self.grades


if __name__ == '__main__':
    print("Write the name of the student:")
    name1 = input()
    with open("D:\МФТИ\Информатика\Students.txt", "r") as file:
        for line in file:
            if line[:8] == 'Student:':
                name = line[9:]
                name = name[:(len(name)-1)]
            if name == name1:
                if line[:7] == 'Course:':
                    course = line[8:]
                    course = course[:(len(course) - 1)]
                if line[:6] == 'Group:':
                    group = line[7:]
                    group = group[:(len(group) - 1)]
                if line[:8] == 'Headmen:':
                    a = line[9:]
                    a = a[:(len(a) - 1)]
                    if a == 'True':
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
            else:
                write_in_file(line)
        with open("D:\МФТИ\Информатика\Students1.txt", "a") as file1:
            file1.write("\n")

    # print(name1, course, group, headmen, subjects, grades, ec)
    s = Student(name1, course, group, headmen, subjects, grades, ec)
    print("Write 'ag' to get an average grade, write 'ng' to set a new grade, write end if you end your work")
    a = input()
    while a != "end":
        if a == 'ag':
            print(s.get_average_grade())
        if a == 'ng':
            v, w = s.set_new_grade()
            with open("D:\МФТИ\Информатика\Students1.txt", "a") as file1:
                file1.write("Student: " + " " + name1 + "\n")
                file1.write("Course: " + " " + course + "\n")
                file1.write("Group: " + " " + group + "\n")
                file1.write("Headmen: " + " " + str(headmen) + "\n")
                file1.write("Subjects: ")
                for i in v:
                    file1.write(" " + str(i))
                file1.write("\n")
                file1.write("Grades: ")
                for j in w:
                    file1.write(" " + str(j))
                file1.write("\n")
                file1.write("Elective courses: ")
                for m in ec:
                    file1.write(" " + str(m))
                file1.write("\n")
                file1.write("\n")
        print("Write 'ag' to get an average grade, write 'ng' to set a new grade, write end if you end your work")
        a = input()
    else:
        print("Have a nice day!")
    # with open("D:\МФТИ\Информатика\Students1.txt", "r") as file1, open("D:\МФТИ\Информатика\Students.txt", "w") as file:
    #     file.write(file1.read())

# небольшое пояснение: когда мы запускаем программу в косоли, надо чётко вводить фамилию и имя студента, которые
# написаны в файле "Students.txt". За одну консольную сессию можно выбрать лишь одного студента, можно один раз
# посмотреть его среднюю оценку по предметам (только по тем предметам, которые уже есть в списке), можно один раз
# добавить новую оценку за предмет. Чтобы сделать какое-либо из действий несколько раз, надо запустить
# программу несколько раз (да, это большая недоработка, но я пока больше не могу думать). Если делать что-то не по
# пояснению, то в базе данных будут возникать повторы, а среднее арифметическое будет оставаться тем же самым.

