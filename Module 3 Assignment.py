
class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email  # Private attribute (Encapsulation)
        self.age = age
        self.department = department

    # Getter method for private email
    def get_email(self):
        return self.__email

    # Setter method for private email
    def set_email(self, email):
        self.__email = email

    # Display student information
    def display_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Email:", self.__email)
        print("Age:", self.age)
        print("Department:", self.department)

    # Method Overloading using *args
    def calculate_result(self, *marks):
        if len(marks) == 0:
            return 0

        total = sum(marks)
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

        return average

    # Student type
    def get_student_type(self):
        return "General Student"


# Undergraduate Student Class
class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age,
                 department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    # Overriding display_info()
    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)
        print("Student Type:", self.get_student_type())


# Graduate Student Class
class GraduateStudent(Student):

    def __init__(self, name, student_id, email, age,
                 department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    # Overriding display_info()
    def display_info(self):
        super().display_info()
        print("Research Topic:", self.research_topic)
        print("Student Type:", self.get_student_type())


# Creating Objects (Class & Object)
student1 = Student(
    "Rahim Ahmed",
    "101",
    "rahim@gmail.com",
    20,
    "CSE"
)

student2 = UndergraduateStudent(
    "Karim Hasan",
    "102",
    "karim@gmail.com",
    21,
    "CSE",
    "5th Semester"
)

student3 = GraduateStudent(
    "Nusrat Jahan",
    "103",
    "nusrat@gmail.com",
    25,
    "CSE",
    "Artificial Intelligence"
)


# Displaying Student Information
student1.display_info()
student2.display_info()
student3.display_info()


# Calculating Results
print("\n--- Student Results ---")

print("\nGeneral Student:")
student1.calculate_result(80, 85, 90)

print("\nUndergraduate Student:")
student2.calculate_result(75, 80, 85, 90)

print("\nGraduate Student:")
student3.calculate_result(88, 92)


# Polymorphism
print("\n--- Polymorphism Demonstration ---")

students = [student1, student2, student3]

for student in students:
    print(student.name, ":", student.get_student_type())


# Encapsulation Demonstration
print("\n--- Encapsulation Demonstration ---")

print("Old Email:", student1.get_email())

student1.set_email("newrahim@gmail.com")

print("Updated Email:", student1.get_email())
