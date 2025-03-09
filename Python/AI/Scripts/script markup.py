import os
import csv

path_file = 'C:\\Users\\zvezd\\Документы\\Датасет чемпионата\\archive-3\\Original Images\\Original Images\\Billie Eilish'

name_file = os.listdir(path_file)
name_file.insert(0, 'ID')
name_file.insert(1, 'LABELS')

result = [(x,) for x in name_file]
with open('output.csv', 'w', newline='') as f:
    csv.writer(f).writerows(result)
