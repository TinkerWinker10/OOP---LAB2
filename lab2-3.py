

class Group: 
    """
    Class, instance of which contains a sequance of instances of the class Student
    """
    def __init__(self, group_name, *students):
        self.group_name = group_name
        if len(students)>20:
            raise OverflowError("More than 20 students")
        self.students = list(students)

        
       
    def add_student(self, student):
        if len(self.students)>20:
            raise OverflowError("More than 20 students")
        
        self.students.append(student)
   
    def remove_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Not instance of class Student")
        self.students.remove(student)




    def __str__(self):  
        """
        Return string with arguments
        """
        return f'Group name: {self.group_name} \nStudents:{" ".join(map(str, self.students))}'



    def top5(self):
        """
        Method, which find first 5 students, who has higher marks
        Using for cycle function to reverse sort students in group by average
        After sort, function return first five students
        """
       
        return sorted(self.students, key = lambda student: student.average(), reverse=True)[:5]
    


class Student:
    """
    Class, instance of which contains student's name,
    surname, record book number and grades
    """
    def __init__(self, name, surname, number, *grades):
        self.name = name
        self.surname = surname
        self.number = number
        for i in grades: 
            if not isinstance(i, int):
                raise TypeError("Grades must be in integer")
        self.grades = grades
        self.average = sum(self.grades) / len(self.grades)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        if not isinstance(data, str):
            raise TypeError("Name must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__name = data

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, data):
        if not isinstance(data, str):
            raise TypeError("Surame must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__surname = data

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, data):
        if not isinstance(data, str):
            raise TypeError("Code must be a string")
        if not data:
            raise ValueError("Field cannot be empty")

        self.__number = data

    
    def __str__(self):
        """
        Return string with attributes
        """
        return f'\n\nName:{self.name}\nSurname:{self.surname} \nRecord book number:{self.number} \nGrades:{" ".join(map(str, self.grades))} \nAverage: {self.average}'

    
    
Nikita = Student('Nikita', 'Teleha', 'NT032480', 5, 5 ,5 ,4, 5)
John = Student('John', 'Bobus', 'NT032460', 1, 2 ,2 ,4, 5)
Andrew = Student('Andrew', 'Goncharuk', 'NT032450', 3, 3 ,3 ,4, 5)
Ivan= Student('Ivan', 'Mayorov', 'NT032440', 1, 1 ,1 ,4, 5)
Vanya = Student('Vanya', 'Generalov', 'NT032430', 2, 2 ,3 ,4, 5)
Denis= Student('Denis', 'Fedorov', 'NT032420', 1, 2 ,5 ,4, 5)
Roma = Student('Roma', 'Amor', 'NT032410', 1, 4 ,4 ,4, 5)
Nikolai = Student('Nikolai', 'Sever', 'NT032489', 1, 2 ,3 ,4, 5)


if __name__ == '__main__':

    tv = Group('TV-01', Nikita, Ivan, Vanya, John, Andrew, Roma, Denis)
    tv.add_student(Nikolai)
    tv.remove_student(Denis)
    
    print(tv)
    print(tv.top5())


    

