from django.shortcuts import render
from .models import Student, Instructor, Course, StudentCourse


def index(request):
    students = Student.objects.all()

    # The following line creates a list that allows you to examine the data 
    # from a Queryset in an easier to visualize way
    # It is not required for functionality!
    # Place a breakpoint on line 14, then compare 'students' and 'data_visualization'
    data_visualization = [item for item in students]

    context = {
        'students': students
    }
    return render(request, 'school/index.html', context)

def problem_one(request):  #Solved by Chris
    students_with_avg_gpa = Student.objects.filter(gpa__gt=3.0).order_by('gpa')
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    data_visualization = [item for item in students_with_avg_gpa]
    context = {
        'students': students_with_avg_gpa
    }
    return render(request, 'school/one.html', context)

def problem_two(request): #Solved By Cole
    instructors_hired_prior_to_2010 = Instructor.objects.filter(hire_date__lt="2010-1-1").order_by('hire_date')
    # Find all instructors hired prior to 2010
    # Order by hire date
    data_visualization = [item for item in instructors_hired_prior_to_2010]

    context = {
        'instructors': instructors_hired_prior_to_2010
    }
    return render(request, 'school/two.html', context)

def problem_three(request): #solved by both of us, working on a better solution exclude() function WILL NOT WORK, idk why
    students_with_a_plus = StudentCourse.objects.filter(grade='A+')
    students_with_c_plus = StudentCourse.objects.filter(grade='C+')
    empty_array_1 = []
    empty_array_2 = []
    for student in students_with_c_plus.iterator():
        empty_array_1.append(student.student_id)
    for student in students_with_a_plus.iterator():
        empty_array_2.append(student.student_id)
    empty_array_3 = [x for x in empty_array_2 if x not in empty_array_1]
    
    final_student_list = StudentCourse.objects.filter(student_id__in=empty_array_3, grade='A+').order_by('student__first_name')
    # students_with_a_plus.exclude(student_id=empty_array)
    # students_with_a_plus = StudentCourse.objects.filter(grade='A+')
    # students_without_c_plus = students_with_a_plus.exclude(grade='C+').order_by('student__first_name')
    # Find all students who have a A+ in any class and are NOT getting a C+ in any class. 
    # Order the data by student's first name alphabetically.
    data_visualization = [item for item in final_student_list]

    context = {
        'student_courses': final_student_list
    }
    return render(request, 'school/three.html', context)

def problem_four(request): #Solved by both of us
    students_in_programming = StudentCourse.objects.filter(course_id=4).order_by('grade')
    # Find all students who are taking the Programming class. 
    # Order by their grade. 
    data_visualization = [item for item in students_in_programming]
    context = {
        'student_courses': students_in_programming
    }
    return render(request, 'school/four.html', context)

def problem_five(request): #Solved by both of us
    students_programming_a = StudentCourse.objects.filter(course_id=4, grade='A').order_by('student__last_name')
    # Find all students getting an A in the Programming class. 
    # Order by last name.
    data_visualization = [item for item in students_programming_a]
    context = {
        'student_courses': students_programming_a
    }
    return render(request, 'school/five.html', context)

def problem_six(request):
    student_with_low_gpa = Student.objects.filter(gpa__lt=3.0)
    # Find all students with a GPA less than 3.0 who are getting an A in Programming class.
    # Order by GPA.

    context = {
        'student_courses': student_with_low_gpa
    }
    return render(request, 'school/six.html', context)

################## BONUS #################
# These problems will require using Aggregate functions along with annotate()
# https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate

# Create a view function and template for each bonus problem you complete

# BONUS ONE
# Write a query to find any instructors who are only teaching one single course. Display the instructor and the course

# BONUS TWO
# Display all students along with the number of credits they are taking

# BONUS THREE
# Find all students who are getting an A in any course and average their GPAs. Display the number of students and their Average GPA

# BONUS FOUR
# Write a function that will replace student GPAs in the database with an accurate score based only on their current grades
# This may require multiple queries
# See https://www.indeed.com/career-advice/career-development/gpa-scale for a chart of what point value each grade is worth