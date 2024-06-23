from abc import ABC, abstractmethod


class Person():
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self.yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name : {self.name} - YoB: {self.yob} - Grade: {self.__grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name : {self.name} - YoB: {self.yob} - Specialist: {self.__specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name : {self.name} - YoB: {self.yob} - Subject: {self.__subject}")


student_1 = Student('Luan', 1999, 9)
student_1.describe()

doctor_1 = Doctor('Dr. Luan', 1992, 'Eyes')
doctor_1.describe()

teacher_1 = Teacher('Luan', 1996, 'Math')
teacher_1.describe()


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_yob(self):
        self.__list_people.sort(key=lambda x: x.get_yob())

    def compute_average_yob(self):
        sum_yob = 0
        for p in self.__list_people:
            sum_yob += p.get_yob()
        return sum_yob/len(self.__list_people)

    def compute_average_yob_teacher(self):
        sum_yob = 0
        count = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                sum_yob += p.get_yob()
                count += 1
        return sum_yob/count


ward_1 = Ward('Ward A')

ward_1.add_person(student_1)
ward_1.describe()

ward_1.add_person(doctor_1)
ward_1.describe()

ward_1.add_person(teacher_1)
ward_1.describe()

ward_1.sort_yob()
ward_1.describe()

print(ward_1.compute_average_yob())
print(ward_1.compute_average_yob_teacher())
