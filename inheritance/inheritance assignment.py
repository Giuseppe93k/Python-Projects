#creating a parent class
class Teacher:
    name = "Amanda"
    Email = "amanda@gmail.com"
    social_security_number = 123456
    
#creating a child class that inherits attrinutes from Teacher 
class Student(Teacher):
    grade = 56
    course = "Python"
    
#creating a second class that inherits from the Teacher
class Headmaster(Teacher):
    qualication = "Managing and human resoursis"
    contrac_duration = "undefined 
