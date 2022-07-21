#creating a class for student
class Student():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = (first + '.' + last + '@stutern.com').lower()

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.email) 


#creating a class that inherits from our students class
class GroupLeader(Student):
# intializing the class to take an argument of list os student
    def __init__(self, first, last, students = []):
        super().__init__(first, last)
        self.students = students

# Defining a method that adds to the list of students under the group leader
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

# Definging a method that removes students from the list of students under the group leader
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student) 

# Defining a function that prints out the full name of students in the list under the group leader
    def print_students(self):
        for student in self.students:
            print(student.fullname())

# creating 3 more instance for the parent class, defined from the session
stud_1 = Student(first='Bukola', last='Saraki')
stud_2 = Student(first='Tina', last='Bakumo')
stud_3 = Student(first='Temitope', last='Babajide')
stud_4 = Student(first='Mary', last='Johnson')
stud_5 = Student(first='John', last='Afolabi')


# creating 2 instance for the sub class
leader1 = GroupLeader(first='Mark', last='job', students=[])
leader2 = GroupLeader(first='joel', last='saint', students=[])


# print(leader1.fullname())
# print(leader2.fullname())

# adding  students to the list of instances for my subclass
leader1.add_student(stud_1)
leader1.add_student(stud_2)

leader2.add_student(stud_4)
leader2.add_student(stud_5)


# leader1.print_students()
# leader2.print_students()

# removing students from the list under the instance of my subclass
leader1.remove_student(stud_2)
leader2.remove_student(stud_5)

# leader1.print_students()
# leader2.print_students()


#printing the fullname of the students in the list under my subclass

leader1.print_students()
leader2.print_students()


#printing the email of the instances in my subclass
print(leader1.email)
print(leader2.email)
