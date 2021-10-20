"""
The class GROUP contains a sequence of instances of the class STUDENT. The class STUDENT contains the student's name,
surname, record book number and grades. Determine the required attributes-data and attributes-methods in classes GROUP
 and STUDENT. Find the average score of each student. Output to the standard output stream the five students with the 
 highest average score.
Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.
"""


class Group: 
    def __init__(self, group_name, **students):
        self.group_name = group_name
        self.students = {}
        for key in students:
            if not Group.check(students[key].name, students[key].surname, self.students):
                self.students[key] = students[key]
        self.top5 = {}
        self.find_best()
        
    def __str__(self):  
        return f'Group name: {self.group_name} \nStudents: {" ".join(list(map(str, list(self.top5.values()))))}'

    @staticmethod
    def check(name, surname, students):
        for key, value in students.items():
            if value.name == name and value.surname == surname:
                return True
            return False

    def find_best(self):
        for key, student in sorted(self.students.items(), key = lambda x: x[1].average, reverse = True)[:5]:
            self.top5[key] = student
    
    


class Student:
    def __init__(self, name, surname, number, *grades):
        self.name = name
        self.surname = surname
        self.number = number
        for i in grades: 
            if not isinstance(i, int):
                raise TypeError("Grades must be in integer")
        self.grades = grades
        self.average = sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f'\n\nName:{self.name}\nSurname:{self.surname} \nRecord book number:{self.number} \nGrades:{" ".join(map(str, self.grades))} \nAverage: {self.average}'

    
    
Nikita = Student('Nikita', 'Teleha', 'NT032480', 5, 5 ,5 ,4, 5)
John = Student('John', 'Bobus', 'NT032460', 1, 2 ,2 ,4, 5)
Andrew = Student('Andrew', 'Goncharuk', 'NT032450', 3, 3 ,3 ,4, 5)
Ivan= Student('Ivan', 'Mayorov', 'NT032440', 1, 1 ,1 ,4, 5)
Vanya = Student('Vanya', 'Generalov', 'NT032430', 2, 2 ,3 ,4, 5)
Denis= Student('Denis', 'Fedorov', 'NT032420', 1, 2 ,5 ,4, 5)
Roma = Student('Roma', 'Amor', 'NT032410', 1, 4 ,4 ,4, 5)
Nikolai = Student('Nikolai', 'Sever', 'NT032489', 1, 2 ,3 ,4, 5)
Kolya = Student('Kolya', 'Lopata', 'NT032488', 1, 2 ,2 ,2, 5)
Serzh = Student('Serzh', 'Tankiyan', 'NT032487', 1, 2 ,3 ,2, 5)
Serhei = Student('Serhei', 'Sis', 'NT032486', 2, 2 ,3 ,4, 5)
Sergei = Student('Sergei', '', 'NT032485', 2, 2 ,2,2, 2)
Mitya = Student('Mitya', 'Fomin', 'NT032484', 3, 2 ,3 ,4, 3)
Dima = Student('Dima', 'Dimitriev', 'NT032483', 1, 3 ,3 ,4, 1)
Dimitri = Student('Dimitri', 'Basilaya', 'NT032481', 1, 2 ,3 ,4, 5)
Fima = Student('Fima', 'Voroshilov', 'NT032482', 1, 2 ,3 ,4, 5)


if __name__ == '__main__':

    tv = Group('TV-01', first = Nikita,aaa= Nikita, second = John, third = Andrew,
        fourth = Ivan, fifth = Vanya, 
        sixth = Denis, seventh = Roma, eigth = Nikolai, nineth = Kolya, 
    tenth = Serzh, eleventh = Serhei, twelth = Sergei, 
    thirteenth = Mitya, fourteenth = Dima, fifteenth = Dimitri, sixteenth = Fima)
    print(tv)
