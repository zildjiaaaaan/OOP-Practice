# Create a class called Student with the following attributes:

# name (a string representing the student's name)
# age (an integer representing the student's age)
# major (a string representing the student's major)
# courses (a list of strings representing the courses the student is taking)
# The Student class should have the following methods:

# add_course(course_name): adds a new course to the courses list
# remove_course(course_name): removes a course from the courses list
# display_courses(): displays the list of courses the student is taking
# Create a subclass of Student called GraduateStudent that has an additional attribute called advisor (a string representing the graduate student's advisor's name). The GraduateStudent class should also have the following method:

# change_advisor(new_advisor): changes the graduate student's advisor to the new advisor provided as an argument.
# Test your implementation by creating instances of the Student and GraduateStudent classes and calling their methods.

class Student:
    def __init__(self, name, age, major, courses):
        self.name = name
        self.age = age
        self.major = major
        self.courses = courses
    
    def add_course(self, course_name):
        self.courses.append(course_name)
    
    def remove_course(self, course_name):
        self.courses.remove(course_name)
    
    def display_courses(self):
        print(f"{self.name}'s courses: {', '.join(self.courses)}")
        

class GraduateStudent(Student):
    def __init__(self, name, age, major, courses, advisor):
        super().__init__(name, age, major, courses)
        self.advisor = advisor
        
    def change_advisor(self, new_advisor):
        self.advisor = new_advisor


# Example usage
s1 = Student("Alice", 20, "Computer Science", ["Intro to Programming", "Data Structures"])
s1.add_course("Algorithms")
s1.display_courses()  # Alice's courses: Intro to Programming, Data Structures, Algorithms
s1.remove_course("Intro to Programming")
s1.display_courses()  # Alice's courses: Data Structures, Algorithms

gs1 = GraduateStudent("Bob", 25, "Mathematics", ["Algebra", "Topology"], "Dr. Smith")
gs1.display_courses()  # Bob's courses: Algebra, Topology
gs1.change_advisor("Dr. Johnson")
print(f"{gs1.name}'s advisor: {gs1.advisor}")  # Bob's advisor: Dr. Johnson
