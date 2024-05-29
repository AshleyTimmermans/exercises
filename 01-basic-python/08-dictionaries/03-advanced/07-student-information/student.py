# Write your code here
def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students

def average_age(data):
    sum = 0
    amount = 0
    for student in data.vlues():
        sum += student['age']
        amount += 1 
    return sum/amount

def courses(data):
    courses = set()
    for student in data.values():
        courses.update(student['coursrs'])
    return courses

def most_common_courses(data):
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    max_count = max(course_counts.values())
    return {
        course
        for course in course_counts.keys()
        if course_counts[course] == max_count
    }
