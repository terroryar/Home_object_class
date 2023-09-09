def fill_obj(obj,curses,finish):
    if isinstance(obj, Student):
        for curse in curses:
            obj.courses_in_progress+=[curse]
        for curse_finish in finish:
            obj.finished_courses+=[curse_finish]

    if isinstance(obj, Lecturer):

        for curse in curses:
            obj.courses_attached+=[curse]
    if isinstance(obj, Reviewer):

        for curse in curses:
            obj.courses_attached+=[curse]


def midle_mark_for_curs(obj,curse):
    summ_grades=0
    count=0
    for item in obj:
        if isinstance(item, Lecturer) or isinstance(item, Student):
            grade=item.grades.get(curse)
            if grade == None: grade=[0]
            summ_grades+=sum(grade)
            count+=len(grade)
        else:
            return(f'Не то подсовываете')
    return(summ_grades / count)

def mid_grade(obj):
    summ = 0
    count = 0
    for grade in obj.grades.values():
        count = count + len(grade)
        for item in grade:  # self.grades[grade]
            summ = summ + item
    if count==0: return (f'No marks')
    return (summ / count)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        newline = '\n'
        str=','
        return (f'Имя:{self.name}{newline}Фамилия: {self.surname}{newline}'
                f'Средняя оценка за домашние задания:{mid_grade(self)}{newline}'
                f'Курсы в процессе изучения:{str.join(self.courses_in_progress)}{newline}'
                f'Завершенные курсы:{str.join(self.finished_courses)}')

    def __eq__(self, other):
        return (mid_grade(self) == mid_grade(other))

    def __lt__(self, other):
        return (mid_grade(self) < mid_grade(other))

    def __gt__(self, other):
        return (mid_grade(self) > mid_grade(other))

    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached:# and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __eq__(self,other):
        return (mid_grade(self)==mid_grade(other))

    def __lt__(self,other):
        return (mid_grade(self)<mid_grade(other))

    def __gt__(self,other):
        return (mid_grade(self)>mid_grade(other))

    def __str__(self):
        newline = '\n'
        return (f'Имя:{self.name}{newline}Фамилия: {self.surname}{newline}'
                f'Средняя оценка:{mid_grade(self)}')


class Reviewer(Mentor):
    def __str__(self):
        newline = '\n'
        return (f'Имя:{self.name}{newline}Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




stud1=Student('Вова','Путинк','M')
fill_obj(stud1,['Python','java','english','literatura'],['git','linux','history','chemystry'])



stud2=Student('Захар','Захаров','M')
fill_obj(stud2,['Python','java','english','literatura'],['git','linux','history'])


stud3=Student('Жанна','Агузарова','G')
fill_obj(stud3,['Python','java','english','japan'],['git','linux','history'])
#fill_obj(obj,name,surname,gender,curses,finish)

#print(best_student.grades)

#print(rew1.__dir__())
lec1=Lecturer('Bob','Smit')
fill_obj(lec1,['Python','java','english','history','linux'],[545,545])
lec2=Lecturer('Jak','Symson')
fill_obj(lec2,['Python','java','english','japan','linux','literatura'],[545,545])

rew1=Reviewer('Ganibal','Lector')
fill_obj(rew1,['Python','java','english','japan','linux','Russian'],[545,545])
rew2=Reviewer('Jak','Vorobei')
fill_obj(rew2,['Python','Perl','english','japan','linux','Cheenes'],[545,545])



stud1.rate_hw(lec1, 'Python', 10)
stud1.rate_hw(lec1, 'java', 10)
stud1.rate_hw(lec1, 'english', 10)
stud1.rate_hw(lec1, 'japan', 10)
stud1.rate_hw(lec2, 'Python', 10)
stud1.rate_hw(lec2, 'java', 10)
stud1.rate_hw(lec2, 'english', 10)
stud1.rate_hw(lec2, 'japan', 10)

stud2.rate_hw(lec1, 'Python', 7)
stud2.rate_hw(lec1, 'java', 8)
stud2.rate_hw(lec1, 'english', 5)
stud2.rate_hw(lec1, 'japan', 7)
stud2.rate_hw(lec2, 'Python', 6)
stud2.rate_hw(lec2, 'java', 3)
stud2.rate_hw(lec2, 'english', 2)
stud2.rate_hw(lec2, 'japan', 2)

rew1.rate_hw(stud1,'Python',8)
rew1.rate_hw(stud1,'java',10)
rew1.rate_hw(stud1,'Python',2)
rew1.rate_hw(stud1,'english',10)
rew1.rate_hw(stud2,'Russian',10)
rew1.rate_hw(stud2,'Cheenes',11)
rew1.rate_hw(stud2,'linux',12)
rew1.rate_hw(stud2,'literatura',8)
rew1.rate_hw(stud2,'chemystry',10)
rew1.rate_hw(stud2,'java',10)
rew2.rate_hw(stud1,'Python',5)
rew2.rate_hw(stud1,'java',3)
rew2.rate_hw(stud1,'Python',4)
rew2.rate_hw(stud1,'english',6)
rew2.rate_hw(stud2,'Russian',4)
rew2.rate_hw(stud2,'Cheenes',1)
rew2.rate_hw(stud2,'linux',3)
rew2.rate_hw(stud2,'literatura',5)
rew2.rate_hw(stud2,'chemystry',3)
rew2.rate_hw(stud2,'java',5)


print('******lec1*********')
#print(lec1.grades)
#print(lec1.courses_attached)
print(lec1)
print('*******lec1********')
print('******lec2*********')
#print(lec1.grades)
#print(lec1.courses_attached)
print(lec2)
print('*******lec2********')
#print(stud1.grades)
print('******rew1*********')
print(rew1)
print('******rew1*********')

print('*******************stud1**************')
print(stud1)
print('*******************stud1**************')
print('*******************stud2**************')
print(stud2)
print('*******************stud2************')
print('*******************stud3**************')
print(stud3)
print('*******************stud3************')
print(lec1==lec2)
print(lec1>lec2)
print(lec1<lec2)
print(stud1==stud2)
print(stud1>stud2)
print(stud1<stud2)


print(rew2)
print(midle_mark_for_curs([stud1,stud2],'Python'))
print(midle_mark_for_curs([lec1,lec2],'java'))