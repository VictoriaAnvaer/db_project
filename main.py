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
    stud_id = input("Enter student ID: ")
    return execute_query(get_db_connection(), "CALL select_student_schedule (" + stud_id + ");")


def get_teach_schedule():
    teach_id = input("Enter teacher ID: ")
    return execute_query(get_db_connection(), "CALL select_teacher_schedule (" + teach_id + ");")


user_type = input("Are you a teacher(t) or student(s)? ")

get_schedule(user_type)

# calculate student grade
#CALL get_avg(student_id, period)
#avg | assignment_type_id | period | course_type_id

# teacher assignment
#CALL get_assignments(course_id)
# assignment_id | assignment_name
#CALL get_assignments_grade(assignment_id)
# student_id | name | grade
