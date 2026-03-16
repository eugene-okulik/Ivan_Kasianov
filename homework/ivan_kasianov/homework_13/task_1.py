import os
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def open_file():
    with open(data_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


for data_line in open_file():
    line_list = []
    for i in data_line.split(". ", 1):
        for o in i.split(" - "):
            line_list.append(o)
    if line_list[0] == "1":
        middle_date = datetime.strptime(
            line_list[1],
            "%Y-%m-%d %H:%M:%S.%f"
        )
        data_finish = middle_date + timedelta(days=7)
        print(data_finish)
    elif line_list[0] == "2":
        date_formatting = datetime.strptime(
            line_list[1],
            "%Y-%m-%d %H:%M:%S.%f"
        )
        print(date_formatting.strftime("%A"))
    elif line_list[0] == "3":
        date_formatting2 = datetime.strptime(
            line_list[1],
            "%Y-%m-%d %H:%M:%S.%f"
        )
        time_left = datetime.now() - date_formatting2
        print(time_left.days)
    else:
        break
