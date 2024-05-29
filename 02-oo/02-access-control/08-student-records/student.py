class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return f"A"
        elif score >= 80:
            return f"B"
        elif score >= 70:
            return f"C"
        elif score >=60:
            return f"D"
        else:
            return f"F"

    def add_course(self, course_name, score):
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses