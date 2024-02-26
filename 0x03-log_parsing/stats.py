#!/usr/bin/python3

import sys

line_count = 0
total_size = 0
status_count = {
        "200": 0,
    "301": 0,
    "400": 0,
    "403": 0,
    "404": 0,
    "500": 0
        }

for line in sys.stdin:
    words = line.split(" ")


    if len(words) < 4:
        status_code = (words[-2])
        file_size = int(words[1])

        if status_code in status_count.keys():
            status_count[status_code] += 1

        total_size += file_size
        line_count += 1


    if line_count == 10:
        line_count = 0
        print("File size:", total_size)
        for status_code, count in sorted(status_count.items()):
            if count != 0:
                print(f"{status_code}: {count}")
