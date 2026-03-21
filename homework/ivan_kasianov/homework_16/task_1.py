import dotenv
import mysql.connector as mysql
import os
import csv

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(
    homework_path,
    "eugene_okulik",
    "Lesson_16",
    "hw_data",
    "data.csv"
)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

cursor = db.cursor(dictionary=True)

query_request_data_by_student_id = """
SELECT
    s.name AS name,
    s.second_name AS second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id = sub.id
"""

cursor.execute(query_request_data_by_student_id)
data_from_db = cursor.fetchall()

with open(data_path, newline="") as csvfile:
    file_data = csv.DictReader(csvfile)
    data_from_csv = []
    for row in file_data:
        data_from_csv.append(row)

for row in data_from_csv:
    if row not in data_from_db:
        print("В базе не хватает", row)

db.close()
