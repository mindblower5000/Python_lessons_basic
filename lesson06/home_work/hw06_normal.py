# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
print('Task 1')


class Person (object):
    __counter_person = -1
    _persons_ptr = []

    def __init__(self, name, *args, **kwargs):
        self.name = name
        Person.__counter_person += 1
        self.person_id = Person.__counter_person
        Person._persons_ptr.append(self)

    def __str__(self):
        return '({},{}'.format(self.person_id, self.name)

    def __hash__(self):
        return hash(self.person_id)

    def __eq__(self, other):
        return self.person_id == other.person_id and isinstance(other, Person)


class Parent(Person):
    __counter_parent = -1
    _parents_ptr = []

    def __init__(self, name):
        super().__init__(name)
        Parent.__counter_parent += 1
        self.parent_id = Parent.__counter_parent
        Parent._parents_ptr.append(self)

    def __hash__(self):
        return hash((self.person_id, self.parent_id))

    def __eq__(self, other):
        return self.parent_id == other.parent_id and isinstance(other, Parent)

    def __str__(self):
        return '{}({})'.format(self.name, self.parent_id)


class Student(Person):
    __counter_student = -1
    _students_ptr = []

    def __init__(self, name, mother: Parent, father: Parent):
        super().__init__(name)
        Student.__counter_student += 1
        self.student_id = Student.__counter_student
        self.the_class = None
        Student._students_ptr.append(self)

        if not mother == father:
            self.mother = mother
            self.father = father
        else:
            # raise ValueError('Student::init error. Parents are not distinct.', mother, father)
            print('Student::init error. Parents are not distinct. ({} = {})'.format(mother, father))
            self.mother = 'BAD DATA'
            self.father = 'BAD DATA'

    def set_assign_class(self, the_class):
        self.the_class = the_class

    def get_assigned_class(self):
        return self.the_class

    def __hash__(self):
        return hash(self.student_id)

    def __eq__(self, other):
        return self.student_id == other.student_id and isinstance(other, Parent) and super() == other.super()

    def __str__(self):
        return '[{}({}), {}, {}]'.format(self.name, self.student_id, self.mother, self.father)

    def get_name(self):
        return self.name


class Subject(object):
    __counter_subject = -1
    _subjects_ptr = []

    def __init__(self, subjname, *args, **kwargs):
        self.subjname = subjname
        Subject.__counter_subject += 1
        self.subject_id = Subject.__counter_subject
        Subject._subjects_ptr.append(self)

    def __hash__(self):
        return hash(self.subject_id)

    def __eq__(self, other):
        return self.subject_id == other.id and isinstance(other, Subject)

    def __str__(self):
        return '(id{}:{})'.format(self.subject_id, self.subjname)


class Teacher(Person):
    __counter_teacher = -1
    _teachers_ptr = []

    def __init__(self, name, subject: Subject):
        super().__init__(name=name)
        Teacher.__counter_teacher += 1
        self.teacher_id = Teacher.__counter_teacher
        self.subject = subject
        Teacher._teachers_ptr.append(self)

    def __hash__(self):
        return hash(self.subject.subject_id)

    def __eq__(self, other):
        return self.subject.subject_id == other.subject.subject_id

    def __eq_full__(self, other):
        return self.teacher_id == other.teacher_id and self.subject.subject_id == other.subject.subject_id \
               and isinstance(other, Parent) and super() == other.super(Person)

    def __str__(self):
        return '{}({}) = {}({})'.format(self.name, self.teacher_id, self.subject.subjname, self.subject.subject_id)


class Class:
    __counter_class = -1
    _classes_ptr = []

    def __init__(self, class_name):
        self.class_name = class_name
        Class.__counter_class += 1
        self.class_id = Class.__counter_class
        self.students = []
        self.teachers = []
        Class._classes_ptr.append(self)
        self.school = None

    def add_student(self, student: Student, force):
        if student not in self.students:
            if not student.get_assigned_class():
                student.set_assign_class(self)
                self.students.append(student)
            else:
                if force:
                    for c in Class._classes_ptr:
                        if student in c.students:
                            c.students.remove(student)
                            print('Class warning :: add_student forced. Removed student {} from class {} to class {}'
                                  .format(student, c, self))
                            self.students.append(student)
                else:
                    print('Class error :: add_student. Student {} attends class {}'.format(student, student.get_assigned_class()))

        else:
            print('Class error :: add_student. Student', student, 'already exists in', self)

    def add_teacher(self, teacher: Teacher):
        if teacher not in self.teachers:  # subjects checking indeed
            self.teachers.append(teacher)
        else:
            print('Class error :: add_teacher subject conflict. Cant use {} in class {}'.format(teacher, self))

    def __hash__(self):
        return hash(self.class_id)

    def __str__(self):
        return '{}({})'.format(self.class_name, self.class_id)


class School:
    __school_counter = -1
    _school_ptr = []
    def __init__(self, name):
        self.name = name
        self.school_classes = []
        School.__school_counter += 1
        self.school_id = School.__school_counter
        School._school_ptr.append(self)

    def add_class(self, new_class: Class):
        if new_class not in self.school_classes:
            new_class.school = self
            self.school_classes.append(new_class)
        else:
            print('School error :: add_class. Class', new_class, ' already exists.')

    def __hash__(self):
        return hash(self.school_id)

    def __str__(self):
        return '({}){}'.format(self.school_id, self.name)

    def print_all(self):
        for cla in self.school_classes:
            print(' CLASS: ', cla)
            print('     Teachers: ')
            for t in cla.teachers:
                print('         ', t)
            print('     Students: ')
            for s in cla.students:
                print('         ', s)

    def print_classes(self):
        print(' Classes: ')
        for cla in self.school_classes:
            print('       ', cla)


parent0 = Parent('Mother0')
parent1 = Parent('Mother1')
parent2 = Parent('Mother2')
parent3 = Parent('Mother3')
parent4 = Parent('Mother4')
parent5 = Parent('Mother5')
parent6 = Parent('Mother6')
parent7 = Parent('Mother7')
parent8 = Parent('Mother8')
parent9 = Parent('Mother9')

parent10 = Parent('Father10')
parent11 = Parent('Father11')
parent12 = Parent('Father12')
parent13 = Parent('Father13')
parent14 = Parent('Father14')
parent15 = Parent('Father15')
parent16 = Parent('Father16')
parent17 = Parent('Father17')
parent18 = Parent('Father18')
parent19 = Parent('Father19')

student0 = Student('Student0 N.SN.', parent0, parent10)  # test : causes error
student0 = Student('Student0 N.SN.', parent0, parent10)
student1 = Student('Student1 N.SN.', parent1, parent11)
student2 = Student('Student2 N.SN.', parent2, parent12)
student3 = Student('Student3 N.SN.', parent3, parent13)
student4 = Student('Student4 N.SN.', parent4, parent14)
student5 = Student('Student5 N.SN.', parent5, parent15)
student6 = Student('Student6 N.SN.', parent6, parent16)
student7 = Student('Student7 N.SN.', parent7, parent17)
student8 = Student('Student8 N.SN.', parent8, parent18)
student9 = Student('Student9 N.SN.', parent9, parent19)

subject0 = Subject('Subject0')
subject1 = Subject('Subject1')
subject2 = Subject('Subject2')
subject3 = Subject('Subject3')
subject4 = Subject('Subject4')
subject5 = Subject('Subject5')
subject6 = Subject('Subject6')
subject7 = Subject('Subject7')
subject8 = Subject('Subject8')
subject9 = Subject('Subject9')

teacher0 = Teacher('teacher0', subject0)
teacher1 = Teacher('teacher1', subject1)
teacher2 = Teacher('teacher2', subject2)
teacher3 = Teacher('teacher3', subject3)
teacher4 = Teacher('teacher4', subject4)
teacher5 = Teacher('teacher5', subject5)
teacher6 = Teacher('teacher6', subject6)
teacher7 = Teacher('teacher7', subject7)
teacher8 = Teacher('teacher8', subject8)
teacher9 = Teacher('teacher9', subject9)
teacher10 = Teacher('teacher9', subject9)  # test : not an error

class0 = Class('class0')
class1 = Class('class1')
class2 = Class('class2')
class3 = Class('class3')
class4 = Class('class4')

class0.add_student(student0, False)
class0.add_student(student1, False)
class1.add_student(student2, False)
class1.add_student(student3, False)
class2.add_student(student4, False)
class2.add_student(student5, False)
class3.add_student(student6, False)
class3.add_student(student7, False)
class4.add_student(student8, False)
class4.add_student(student9, False)
class4.add_student(student9, False)  # test : causes error
class3.add_student(student9, False)  # test : causes error
class3.add_student(student9, True)   # force student transfer

class0.add_teacher(teacher0)
class0.add_teacher(teacher0)  # test : causes subject error
class0.add_teacher(teacher1)
class1.add_teacher(teacher2)
class1.add_teacher(teacher3)
class2.add_teacher(teacher4)
class2.add_teacher(teacher5)
class3.add_teacher(teacher6)
class3.add_teacher(teacher7)
class4.add_teacher(teacher8)
class4.add_teacher(teacher9)
class4.add_teacher(teacher10)  # test : causes subject error

school1 = School('School_1')
school1.add_class(class0)
school1.add_class(class1)
school1.add_class(class2)
school1.add_class(class3)
school1.add_class(class4)
school1.add_class(class4)  # test : causes error

print('\n\nTask 2')
print('# Выбранная и заполненная данными структура должна решать следующие задачи:')
print('# 1. Получить полный список всех классов школы')
print('\nSCHOOL:', school1)
print('1.1')
school1.print_classes()
print('1.2')
classes_by_school =  'School_1'
print([s.__str__() for s in [s.school_classes for s in School._school_ptr if s.name == classes_by_school][0]])
# for c in aa:
#     print(c.class_name.__str__())
# print(aa)
# print([c.class_name for c in aa])

print('\n# 2. Получить список всех учеников в указанном классе')
#  (каждый ученик отображается в формате "Фамилия И.О.")

find_students_by_class = [c for c in Class._classes_ptr if c.class_name == 'class1'][0]  # if c.class == class1
print([s.get_name() for s in Student._students_ptr if s.get_assigned_class() == find_students_by_class ])


print('# 3. Получить список всех предметов указанного ученика')
#  (Ученик --> Класс --> Учителя --> Предметы)
student__ = [s for s in Student._students_ptr if s.name == 'Student2 N.SN.'][0]
get_subjects_for_student = student__
students_class = [c for c in Class._classes_ptr if get_subjects_for_student in c.students][0]
print([t.subject.subjname for t in students_class.teachers])


print('# 4. Узнать ФИО родителей указанного ученика')
get_parents_by_student = 'Student2 N.SN.'
print([(s.mother.__str__(), s.father.__str__()) for s in Student._students_ptr if s.name == get_parents_by_student])

print('# 5. Получить список всех Учителей, преподающих в указанном классе')
teachers = [c.teachers for c in Class._classes_ptr if c.class_name == 'class1'][0]
print([t.__str__() for t in teachers])


