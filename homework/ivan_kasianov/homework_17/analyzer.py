import os
import argparse
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Find logs by text")
    parser.add_argument("path", help="File or directory")
    parser.add_argument("-t", "--text", help="Text to find")
    return parser.parse_args()


args = parse_args()

file_path = args.path
text_to_find = args.text

if os.path.isdir(file_path):
    files = list(
        filter(
            lambda name: name.endswith(".log"),
            os.listdir(file_path)
        )
    )
    files.sort()
    files = list(map(lambda name: os.path.join(file_path, name), files))
else:
    files = [file_path]

data = {}


def get_date_from_line(line_content):
    if len(line_content) >= 23:

        date_candidate = line_content[:23]
        try:
            datetime.fromisoformat(date_candidate)
            return date_candidate
        except ValueError:
            pass
    return None


for file in files:
    with open(file) as log_file:
        for i, line in enumerate(log_file.readlines()[: 35]):
            line_date = get_date_from_line(line)
            if line_date:
                date_key = line_date
                data[date_key] = line
            else:
                data[date_key] += line

for key, entry in data.items():
    if text_to_find in entry:
        line_log = key, entry
        line_log_list = " ".join(line_log).split()
        text_index_in_log = line_log_list.index(text_to_find)
        start = max(0, text_index_in_log - 5)
        end = text_index_in_log + 6
        print(" ".join(line_log_list[start:end]))
