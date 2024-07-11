import numpy as np
import matplotlib.pyplot as plt
import os

def process_file(file_name, start, end, replace_D=True):
    file_path = f'average_{average_name}/NNLO4.{file_name}_q1_uh_El0_sam0_ode3.dat' if replace_D else f'average_{average_name}/{file_name}.dat'
    with open(file_path) as file:
        lines = file.readlines()[start:end]
        for line in lines:
            row = [float(value.replace('D', 'e')) if replace_D else float(value) for value in line.split()]
            file_dict[file_name].append(row)


average_name = input("folder#:")

i = input("Log(1)/Linear(2):")

if i == '1':
    start_1, end_1 = (0, 96)
    start_2, end_2 = (171, 267)
elif i == '2':
    start_1, end_1 = (100, 223)
    start_2, end_2 = (272, 395)


name = ['6_6','6_7','6_8','6_9']
name.insert(0,f'average_{average_name}')
file_dict = {n: [] for n in name}
colors = ['orange','green','yellow','red','blue']        

for file_name in name:
    if file_name == name[0]:
        process_file(file_name, start_1, end_1,replace_D=False) 
    else:
        process_file(file_name,start_2, end_2)

fig, ax = plt.subplots()

for i in range(len(file_dict[name[0]])):
    bin_center = (file_dict[name[0]][i][0] + file_dict[name[0]][i][1]) / 2
    bin_width = file_dict[name[0]][i][1] - file_dict[name[0]][i][0]
    
    a = file_dict[name[0]][i][2]
    y_1 = file_dict[name[1]][i][2]
    y_2 = file_dict[name[2]][i][2]
    y_3 = file_dict[name[3]][i][2]
    y_4 = file_dict[name[4]][i][2]

    min_value = min(a/y_1,a/y_2,a/y_3,a/y_4)
    max_value = max(a/y_1,a/y_2,a/y_3,a/y_4)

    ax.bar(bin_center, min_value, width=bin_width, color='white', edgecolor='black')

    ax.bar(bin_center, max_value, width=bin_width, color='white', edgecolor='black')

    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [a/y_1, a/y_1], color=colors[1],linewidth=1)
    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [a/y_2, a/y_2], color=colors[2],linewidth=1)
    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [a/y_3, a/y_3], color=colors[3],linewidth=1)
    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [a/y_4, a/y_4], color=colors[4],linewidth=1)

plt.show()