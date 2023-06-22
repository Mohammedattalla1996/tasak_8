class Student:

    def __init__(self, name, age, city):
        self.f_name = name
        self.f_age = age
        self.f_city = city

        print(f'Hello  {self.f_name},\n'
              f'your age is {self.f_age} \n'
              f' your are from {self.f_city}.')


    def add_mark(self, *mark):
        print(f'your marks:{mark}')



    def calc_avg(self, *marks):
        sum = 0
        for mark in marks:
            sum += mark
        my_avg = sum // len(marks)
        print(f'your Avg: {my_avg}')




student_1 = Student("mohammed", 85, "Dair el Balah")
student_1.add_mark(5, 7, 9)
student_1.calc_avg(8, 8, 8)