import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(user='victoriaa127',
                                         password='230826075',
                                         host='10.8.37.226',
                                         database='victoriaa127_db')
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()
    return results


def get_schedule(type_u):
    if type_u == "s":
        results = get_stud_schedule()
        for row in results:
            print("")
            print("Period: " + str(row[1]))
            print("Course: " + row[2])
            print("Room: " + row[3])
            print("Teacher: " + row[4])
    else:
        results = get_teach_schedule()
        for row in results:
            print("")
            print("Period: " + str(row[2]))
            print("Course: " + row[3])
            print("Room: " + row[4])


def get_stud_schedule():
    return execute_query(get_db_connection(), "CALL select_student_schedule (" + user_id + ");")


def get_teach_schedule():
    return execute_query(get_db_connection(), "CALL select_teacher_schedule (" + user_id + ");")


def get_grades():
    total = 0.0
    for i in range(1, 11):
        grade = calc_grade(i)[0]
        if calc_grade(i)[1]:
            print(grade)
            grade = grade
            print(grade)
        total += grade
    return total/10
def calc_grade(period):
    ap=False
    results = execute_query(get_db_connection(), "CALL get_avg (" + user_id + ", " + str(period) + ");")
    if results[0][3] == 2:
        ap=True
    return (float(results[0][0]) * 0.3) + (float(results[1][0]) * 0.7), ap


user_type = input("Are you a teacher(t) or student(s)? ")
user_id = input("What is your ID? ")
option = 99
if user_type == "s":
    while option != 0:
        print("1. View Schedule")
        print("2. View grades")
        print("0. Quit")
        option = int(input("Select a number: "))
        if option == 1:
            get_schedule(user_type)
        elif option == 2:
            print("1. Specific period")
            print("2. Overall average")
            option = int(input("Select a number: "))
            if option == 1:
                option = input("Enter period: ")
                print(f"period {option}: {calc_grade(option)[0]}")
            elif option == 2:
                print(f"Overall average: {get_grades()}")

# calculate student grade
#CALL get_avg(student_id, period)
#avg | assignment_type_id | period | course_type_id

# teacher assignment
#CALL get_assignments(course_id)
# assignment_id | assignment_name
#CALL get_assignments_grade(assignment_id)
# student_id | name | grade
