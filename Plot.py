import matplotlib.pyplot as plt
import os
import pandas as pd
import math
import time


total_file = '10seeds_plot'

rang = input()


def list_range(ran):
    if ran == 'log':
        return slice(None, 100)  # Equivalent to ':100'
    elif ran == 'log_2':
        return slice(1, 101)     # Equivalent to '1:101'
    elif ran == 'linear':
        return slice(100, None)  # Equivalent to '100:'
    elif ran == 'linear_2':
        return slice(102, 302)   # Equivalent to '102:302'
    else:
        raise ValueError("Invalid range specified")


def sorting_key(file_name):
    if file_name == 'average.dat':
        return -1
    else:
        parts = file_name.split('_')
        if len(parts) > 2 and parts[2].isdigit():
            return int(parts[2])
        else:
            return float('inf')
         
def linestyle(file_name):
    if file_name in ['ave_-er/sqrt(6)','ave_+er/sqrt(6)']:
        return 'dashed'
    else:
        return 'solid'

def color(file_name):
    if file_name == 'average.dat':
        return 'grey'
    if file_name == 'ave_+er/sqrt(6)':
        return 'magenta'
    if file_name == 'ave_-er/sqrt(6)':
        return 'magenta'
    else:
        parts = file_name.split('_')
        if parts[1] == '4':
            return 'teal'
        elif parts[1] == '5':
            return 'purple'
        elif parts[1] == '6':
            return 'cyan'
        elif parts[1] == '7':
            return 'green'
        elif parts[1] == '14':
            return 'yellow'
        elif parts[1] == '16':
            return 'red'
        elif parts[1] == '17':
            return 'blue'
        elif parts[1] == '18':
            return 'brown'
        elif parts[1] == '19':
            return 'orange'
        elif parts[1] == '20':
            return 'darkblue'
        
#ratio plot
'''
for q_name in os.listdir(total_file):
    if q_name == '.DS_Store':
        continue
    #if q_name not in ['q4.0387239','q3.8486361','q3.6511368','q3.4423248','q3.54827','q3.33302','q2.85422','q2.58174']:
        #continue
    #if q_name != 'q0.860581':
        #continue
    #if q_name != 'q0.46':
        #continue
    q_folder_path = os.path.join(total_file, q_name)
    
    for El_folder in os.listdir(q_folder_path):
        if El_folder == '.DS_Store':
            continue
        #if El_folder != 'El1':
            #continue
        #f El_folder != 'El0':
            #continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        
        file_dict = {}
        
        sorted_file_list = sorted([file_name for file_name in os.listdir(El_folder_path) if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']], key=sorting_key)
        print(sorted_file_list)
    
        for file_name in sorted_file_list:
            file_dict[file_name] = []
            if file_name == 'average.dat':
                with open(os.path.join(El_folder_path, file_name)) as file:
                    lines = file.readlines()[list_range(rang)]
                    for line in lines:
                        try:
                            row = [float(value.replace('D', 'e')) for value in line.split()]
                        except ValueError:
                            continue
                        file_dict[file_name].append(row)
            else:
                with open(os.path.join(El_folder_path, file_name)) as file:
                    lines = file.readlines()[list_range(f'{rang}_2')]#171:271,272:473
                    for line in lines:
                        try:
                            row = [float(value.replace('D', 'e')) for value in line.split()]
                        except ValueError:
                            continue
                        file_dict[file_name].append(row)

        fig, ax = plt.subplots()

        for i in range(len(file_dict[sorted_file_list[0]])):
            if file_dict[sorted_file_list[0]][i][2] == 0:
                continue
            ave_dict = {}
            bin_center = (file_dict[sorted_file_list[0]][i][0] + file_dict[sorted_file_list[0]][i][1]) / 2
            bin_width = file_dict[sorted_file_list[0]][i][1] - file_dict[sorted_file_list[0]][i][0]
            for f in range(1,len(sorted_file_list)):   
                ave_dict[sorted_file_list[f]]=[]
                ave_dict[sorted_file_list[f]].append(file_dict[sorted_file_list[f]][i][2]/file_dict[sorted_file_list[0]][i][2])
            ave_dict['ave_+er/sqrt(6)'] = []
            ave_dict['ave_-er/sqrt(6)'] = []
            ave_dict['ave_+er/sqrt(6)'].append((file_dict[sorted_file_list[0]][i][2]+file_dict[sorted_file_list[0]][i][3])/file_dict[sorted_file_list[0]][i][2])
            ave_dict['ave_-er/sqrt(6)'].append((file_dict[sorted_file_list[0]][i][2]-file_dict[sorted_file_list[0]][i][3])/file_dict[sorted_file_list[0]][i][2])
            min_value = min(ave_dict.values())
            max_value = max(ave_dict.values())
            print(ave_dict)
            print(min_value,max_value)
            ax.set_ylim(0.85, 1.15)
            ax.bar(bin_center, min_value, width=bin_width, color='white', edgecolor='black')
            ax.bar(bin_center, max_value, width=bin_width, color='white', edgecolor='black')
            #ax.bar(bin_center, ave_dict['ave_+er/sqrt(6)'], width=bin_width, color='white', edgecolor='black')
            #ax.bar(bin_center, ave_dict['ave_-er/sqrt(6)'], width=bin_width, color='white', edgecolor='black')
            print(ave_dict)
            for i,j in ave_dict.items():
                #if i not in ['average','ave_-er/sqrt(6)','ave_+er/sqrt(6)']:
                    #continue
                ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2],
                        [j, j],
                        color=color(i), #linestyle=linestyle(i),
                         linewidth=1)

        plt.savefig(os.path.join(El_folder_path, f'{rang}_ratio_plot.png'), dpi=1000)


'''


for q_name in os.listdir(total_file):
    if q_name == '.DS_Store':
        continue
    #if q_name not in ['q4.0387239','q3.8486361','q3.6511368','q3.4423248','q3.54827','q3.33302','q2.85422','q2.58174']:
        #continue
    #if q_name != 'q0.46':
        #continue

    q_folder_path = os.path.join(total_file, q_name)
    
    for El_folder in os.listdir(q_folder_path):
        if El_folder == '.DS_Store':
            continue
        #if El_folder != 'El0':
            #continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        
        file_dict = {}
        sorted_file_list = sorted([file_name for file_name in os.listdir(El_folder_path) if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']], key=sorting_key)
        print(sorted_file_list)

        for file_name in sorted_file_list:
            file_dict[file_name] = []
            if file_name == 'average.dat':
                with open(os.path.join(El_folder_path, file_name)) as file:
                    lines = file.readlines()[list_range(rang)]
                    for line in lines:
                        try:
                            row = [float(value) for value in line.split()]
                        except ValueError:
                            continue
                        file_dict[file_name].append(row)
            else:
                print(sorted_file_list)
                with open(os.path.join(El_folder_path, file_name)) as file:
                    lines = file.readlines()[list_range(f'{rang}_2')]#171:271,272:473
                    for line in lines:
                        try:
                            row = [float(value.replace('D', 'e')) for value in line.split()]
                        except ValueError:
                            continue
                        file_dict[file_name].append(row)

        fig, ax = plt.subplots()

        for i in range(len(file_dict[sorted_file_list[0]])):
                    if file_dict[sorted_file_list[0]][i][2] == 0:
                        continue
                    ave_dict = {}
                    bin_center = (file_dict[sorted_file_list[0]][i][0] + file_dict[sorted_file_list[0]][i][1]) / 2
                    bin_width = file_dict[sorted_file_list[0]][i][1] - file_dict[sorted_file_list[0]][i][0]
                    for f in range(len(sorted_file_list)):   
                        ave_dict[sorted_file_list[f]]=[]
                        ave_dict[sorted_file_list[f]].append(file_dict[sorted_file_list[f]][i][2])
                    ave_dict['ave_+er/sqrt(6)'] = []
                    ave_dict['ave_-er/sqrt(6)'] = []
                    ave_dict['ave_+er/sqrt(6)'].append(file_dict[sorted_file_list[0]][i][2]+file_dict[sorted_file_list[0]][i][3])
                    ave_dict['ave_-er/sqrt(6)'].append(file_dict[sorted_file_list[0]][i][2]-file_dict[sorted_file_list[0]][i][3])

                    min_value = min(ave_dict.values())
                    max_value = max(ave_dict.values())
                    print(ave_dict)
                    print(min_value,max_value)
                    ax.bar(bin_center, min_value, width=bin_width, color='white', edgecolor='black')
                    ax.bar(bin_center, max_value, width=bin_width, color='white', edgecolor='black')
                    #ax.bar(bin_center, ave_dict['ave_-er/sqrt(6)'], width=bin_width, color='white', edgecolor='black')
                    #ax.bar(bin_center, ave_dict['ave_+er/sqrt(6)'], width=bin_width, color='white', edgecolor='black')
                    for i,j in ave_dict.items():
                        #if i not in ['average.dat','ave_-er/sqrt(6)','ave_+er/sqrt(6)']:
                            #continue
                        ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2],
                                [j, j],
                                color=color(i), #linestyle=linestyle(i), 
                                linewidth=1)

        plt.savefig(os.path.join(El_folder_path, f"{rang}_plot.png"), dpi=1000)





'''












def sorting_key(file_name):
    if file_name in ['average.dat', '.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']:
        return 0
    else:
        parts = file_name.split('_')
        if len(parts) > 2 and parts[2].isdigit():
            return int(parts[2])
        else:
            return float('inf') 

def color(file_name):
    if file_name == 'average.dat':
        return 'orange'
    if file_name in ['ave_+er/2', 'ave_-er/2']:
        return 'purple'
    else:
        parts = file_name.split('_')
        if parts[2] == '4':
            return 'green'
        elif parts[2] == '5':
            return 'yellow'
        elif parts[2] == '6':
            return 'red'
        elif parts[2] == '7':
            return 'blue'


def replace_D_with_e(x):
    return float(x.replace('D', 'e')) if isinstance(x, str) else x


for q_name in os.listdir('seeds_q2'):
    if q_name == '.DS_Store':
        continue
    q_folder_path = os.path.join('seeds_q2', q_name)
    
    for El_folder in os.listdir(q_folder_path):
        start = time. time()
        if El_folder == '.DS_Store':
            continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        
        file_dict = {}

        sorted_file_list = sorted(os.listdir(El_folder_path), key=sorting_key)
        sorted_file_list = [file_name for file_name in sorted_file_list if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']]

        for file_name in sorted_file_list:
            if file_name == 'average.dat':
                lines = pd.read_csv(os.path.join(El_folder_path, file_name), header=None, #skiprows=100
                                     delimiter=r"\s+")#171:271,272:473
                file_dict[file_name] = lines
            else:
                lines = pd.read_csv(os.path.join(El_folder_path, file_name), header=None, skiprows=272, delimiter=r"\s+", converters={0: replace_D_with_e,1: replace_D_with_e,2: replace_D_with_e, 3: replace_D_with_e})
                file_dict[file_name] = lines

        fig, ax = plt.subplots()

        for i in range(len(file_dict[sorted_file_list[0]])):
            if file_dict[sorted_file_list[0]].iloc[i, 2] == 0:
                continue
            ave_dict = {}
            bin_center = (file_dict[sorted_file_list[0]].iloc[i, 0] + file_dict[sorted_file_list[0]].iloc[i, 1]) / 2
            bin_width = file_dict[sorted_file_list[0]].iloc[i, 1] - file_dict[sorted_file_list[0]].iloc[i, 0]
            for file_name in sorted_file_list[1:]:
                ave_dict[file_name] = float(file_dict[file_name].iloc[i, 2]) / float(file_dict[sorted_file_list[0]].iloc[i, 2])

            ave_dict['ave_+er/2'] = (float(file_dict[sorted_file_list[0]].iloc[i, 2]) + (float(file_dict[sorted_file_list[0]].iloc[i, 3]) / 2)) / float(file_dict[sorted_file_list[0]].iloc[i, 2])
            ave_dict['ave_-er/2'] = (float(file_dict[sorted_file_list[0]].iloc[i, 2]) - (float(file_dict[sorted_file_list[0]].iloc[i, 3]) / 2)) / float(file_dict[sorted_file_list[0]].iloc[i, 2])
            min_value = min(ave_dict.values())
            max_value = max(ave_dict.values())
            ax.set_ylim(0.95, 1.05)
            ax.bar(bin_center, min_value, width=bin_width, color='white', edgecolor='black')
            ax.bar(bin_center, max_value, width=bin_width, color='white', edgecolor='black')
            for file_name, value in ave_dict.items():
                ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2],
                        [value, value],
                        color=color(file_name), linewidth=1)

        plt.savefig(os.path.join(El_folder_path, "linear_ratio_plot.png"), dpi=1000)

        end = time. time()
        duration = end - start
        print("Time: {} seconds". format(round(duration, 3)))

#q0.0145465
#q1
'''





'''
q_num = int(input("q_index#:"))
El_num = int(input("El_index#:"))
q = ['q0.46','q0.046','q0.0145465','q0.860581','q1','q1.49057','q1.92432','q1.2170456','q1.7511624','q2.27688','q2.58174','q2.85422','q2.1079848','q2.4340912','q2.7213967','q2.9811407','q3.10287','q3.33302','q3.54827','q3.60447','q3.75119','q3.94368','q3.2200000','q3.4423248','q3.6511368','q3.8486361','q4.0387239','q4.1337678']
graph_t = input("Log(1)/Linear(2):")
colors = ['orange','green','yellow','red','blue']        
file_list = os.listdir(f'seeds_q/{q[q_num]}/El{El_num}')


def sorting_key(file_name):
    if file_name == 'average.dat':
        return -1
    parts = file_name.split('_')
    if len(parts) > 1 and parts[1].isdigit():
        return int(parts[1])
    else:
        return float('inf') 

sorted_file_list = sorted(file_list, key=sorting_key)
file_dict = {}

for file_name in sorted_file_list:
    file_dict[file_name] = []
    if graph_t == '1':
        if file_name == 'average.dat':
            with open(f'seeds_q/{q[q_num]}/El{El_num}/{file_name}') as file:
                lines = file.readlines()[0:100]
                for line in lines:
                        row = [float(value) for value in line.split()]
                        file_dict[file_name].append(row)
        else:
            with open(f'seeds_q/{q[q_num]}/El{El_num}/{file_name}') as file:
                    lines = file.readlines()[171:271]
                    for line in lines:
                        row = [float(value.replace('D', 'e')) for value in line.split()]
                        file_dict[file_name].append(row)

    elif graph_t == '2':
        if file_name == 'average.dat':
            with open(f'seeds_q/{q[q_num]}/El{El_num}/{file_name}') as file:
                lines = file.readlines()[100:]
                for line in lines:
                        row = [float(value) for value in line.split()]
                        file_dict[file_name].append(row)

        else:
            with open(f'seeds_q/{q[q_num]}/El{El_num}/{file_name}') as file:
                    lines = file.readlines()[272:473]
                    for line in lines:
                        try:
                            row = [float(value.replace('D', 'e')) for value in line.split()]
                        except ValueError:
                            continue
                        file_dict[file_name].append(row)


fig, ax = plt.subplots()

for j in range(len(sorted_file_list)):
    for i in range(len(file_dict[sorted_file_list[0]])):
        if file_dict[sorted_file_list[0]][i][2] == 0:
            break

        bin_center = (file_dict[sorted_file_list[0]][i][0] + file_dict[sorted_file_list[0]][i][1]) / 2
        bin_width = file_dict[sorted_file_list[0]][i][1] - file_dict[sorted_file_list[0]][i][0]

        
        min_value = min(height[i][2] for height in file_dict.values())
        max_value = max(height[i][2] for height in file_dict.values())
        print(max_value)
        print(min_value)

        ax.bar(bin_center, min_value, width=bin_width, color='white', edgecolor='black')
        ax.bar(bin_center, max_value, width=bin_width, color='white', edgecolor='black')

        ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [file_dict[sorted_file_list[j]][i][2], file_dict[sorted_file_list[j]][i][2]], color=colors[j], linewidth=1)
plt.savefig(os.path.join(f'seeds_q/{q[q_num]}/El{El_num}', "linear_plot.png"),dpi = 1000)
'''
