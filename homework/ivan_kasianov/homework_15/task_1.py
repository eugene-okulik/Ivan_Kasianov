import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

name = "Ivan"
second_name = "Kasianov"
query_create_student = """
INSERT INTO students (name, second_name)
VALUES (%s, %s)
"""
values = (name, second_name)
cursor.execute(query_create_student, values)
student_id = cursor.lastrowid

query_create_books = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
book_1 = "The Hobbit"
book_2 = "The little prince"
book_3 = "Brave new world"
values = [
    (book_1, student_id),
    (book_2, student_id),
    (book_3, student_id)
]
cursor.executemany(query_create_books, values)

query_create_group = """
INSERT INTO `groups` (title, start_date, end_date)
VALUES (%s, %s, %s)
"""
course_title = "Python AQA 2026"
course_start_date = "feb 2026"
course_end_date = "apr 2026"
values = (
    course_title,
    course_start_date,
    course_end_date
)
cursor.execute(query_create_group, values)
group_id = cursor.lastrowid

query_update_students_group = """
UPDATE students
SET group_id = %s
WHERE id = %s
"""
values = (group_id, student_id)
cursor.execute(query_update_students_group, values)

query_create_subject = """
INSERT INTO subjects (title)
VALUES (%s)
"""
subject_1_title = "Python for AQA"
cursor.execute(query_create_subject, (subject_1_title,))
subject_1_id = cursor.lastrowid

subject_2_title = "SQL for AQA"
cursor.execute(query_create_subject, (subject_2_title,))
subject_2_id = cursor.lastrowid

query_create_lesson = """
INSERT INTO lessons (title, subject_id)
VALUES (%s, %s)
"""
lesson_python_1_title = "Python for AQA lesson 1"
cursor.execute(query_create_lesson, (lesson_python_1_title, subject_1_id))
lesson_python_1_id = cursor.lastrowid

lesson_python_2_title = "Python for AQA lesson 2"
cursor.execute(query_create_lesson, (lesson_python_2_title, subject_1_id))
lesson_python_2_id = cursor.lastrowid

lesson_sql_1_title = "SQL for AQA lesson 1"
cursor.execute(query_create_lesson, (lesson_sql_1_title, subject_2_id))
lesson_sql_1_id = cursor.lastrowid

lesson_sql_2_title = "SQL for AQA lesson 2"
cursor.execute(query_create_lesson, (lesson_sql_2_title, subject_2_id))
lesson_sql_2_id = cursor.lastrowid

query_create_marks = """
INSERT INTO marks (value, lesson_id, student_id)
VALUES (%s, %s, %s)
"""
mark_1 = 5
mark_2 = 4
mark_3 = 5
mark_4 = 5
values = [
    (mark_1, lesson_python_1_id, student_id),
    (mark_2, lesson_python_2_id, student_id),
    (mark_3, lesson_sql_1_id, student_id),
    (mark_4, lesson_sql_2_id, student_id)
]
cursor.executemany(query_create_marks, values)

query_request_marks_by_student_id = """
SELECT * FROM marks
WHERE student_id = %s
"""
values = (student_id,)
cursor.execute(query_request_marks_by_student_id, values)
print(cursor.fetchall())

query_request_books_by_student_id = """
SELECT * FROM books
WHERE taken_by_student_id = %s
"""
values = (student_id,)
cursor.execute(query_request_books_by_student_id, values)
print(cursor.fetchall())

query_request_data_by_student_id = """
SELECT
s.name,
s.second_name,
g.title,
b.title,
m.value,
l.title,
sub.title
FROM students s
join `groups` g on s.group_id = g.id
join books b on s.id = b.taken_by_student_id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id  = l.id
join subjects sub on l.subject_id = sub.id
WHERE s.id = %s
"""
values = (student_id,)
cursor.execute(query_request_data_by_student_id, values)
print(cursor.fetchall())

db.commit()
db.close()
