#!/usr/bin/env python

import os

file_path = 'housing.data'

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('housing.data')

corrected_file = []
for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(' ')
    corrected_line = []
    print(line_values)
    for value in line_values:
        value = float(value)
        corrected_line.append(value)
    corrected_file.append(corrected_line)
    print(corrected_line)
print('***************************************************************NEW FILE*********************************************************')
print(corrected_file)

file.close()