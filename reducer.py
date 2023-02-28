# /usr/bin/env python3
import sys
import csv

counts = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    specific_resource_type, date = line.strip().split()
    # increase counters
    if specific_resource_type not in counts:
        counts[specific_resource_type] = {}
    if date not in counts[specific_resource_type]:
        counts[specific_resource_type][date] = 0
    counts[specific_resource_type][date] += 1


for specific_resource_type in counts:
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['specific_resource_type', 'date', 'count'])
        for date in counts[specific_resource_type]:
            writer.writerow([specific_resource_type, date, counts[specific_resource_type][date]])