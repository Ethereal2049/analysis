import os
import math

'''
def sorting_key(file_name):
    if file_name == 'average.dat':
        return -1
    parts = file_name.split('_')
    if len(parts) > 1 and parts[1].isdigit():
        return int(parts[1])
    else:
        return float('inf') 

for q_name in os.listdir(f'seeds4567_redone_plot'):
    if q_name == '.DS_Store':
        continue
    #if q_name != 'q0.46':
        #continue

    q_folder_path = os.path.join(f'seeds4567_redone_plot', q_name)
    
    for El_folder in os.listdir(q_folder_path):
        if El_folder == '.DS_Store':
            continue
        #if El_folder != 'El0':
            #continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        sorted_file_list = sorted([file_name for file_name in os.listdir(El_folder_path) if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']], key=sorting_key)

        file_dict = {}
        average_list = []

        if '.DS_Store' in sorted_file_list:
            sorted_file_list.remove('.DS_Store')

        for file_name in sorted_file_list:
            file_dict[file_name] = []
            with open(os.path.join(El_folder_path, file_name)) as file:
                lines = file.readlines()[1:101]
                for line in lines:
                    try:
                        row = [float(value.replace('D', 'e')) for value in line.split()]
                    except ValueError:
                        continue
                    file_dict[file_name].append(row)
            with open(os.path.join(El_folder_path, file_name)) as file: 
                lines_2 = file.readlines()[102:302]
                for line in lines_2:
                    try:
                        row = [float(value.replace('D', 'e')) for value in line.split()]
                    except ValueError:
                        continue
                    file_dict[file_name].append(row)
        for i,j in file_dict.items():
                print(i)

        for j in range(len(file_dict[sorted_file_list[0]])):
                average = round(sum(file_dict[f'{k}'][j][2] for k in sorted_file_list) / len(file_dict),16)
                error = round(sum(file_dict[f'{k}'][j][3] for k in sorted_file_list) / len(file_dict),20)
                average_plus_error = round(average + error/math.sqrt(4),20)
                average_minus_error = round(average - error/math.sqrt(4),20)
                average_list.append([file_dict[sorted_file_list[0]][j][0],file_dict[sorted_file_list[0]][j][1],average,average_plus_error,average_minus_error])


        average_file = os.path.join(El_folder_path, 'average.dat')

        with open(average_file, 'w') as file:
            for inner_list in average_list:
                line = '    '.join(str(item) for item in inner_list) + '\n'
                file.write(line)
'''


def sorting_key(file_name):
    if file_name == 'average.dat':
        return -1
    parts = file_name.split('_')
    if len(parts) > 1 and parts[1].isdigit():
        return int(parts[1])
    else:
        return float('inf') 

for q_name in os.listdir(f'10seeds_plot'):
    if q_name == '.DS_Store':
        continue
    #if q_name != 'q0.46':
        #continue

    q_folder_path = os.path.join(f'10seeds_plot', q_name)
    
    for El_folder in os.listdir(q_folder_path):
        if El_folder == '.DS_Store':
            continue
        #if El_folder != 'El0':
            #continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        sorted_file_list = sorted([file_name for file_name in os.listdir(El_folder_path) if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']], key=sorting_key)

        file_dict = {}
        average_list = []

        if '.DS_Store' in sorted_file_list:
            sorted_file_list.remove('.DS_Store')

        for file_name in sorted_file_list:
            file_dict[file_name] = []
            with open(os.path.join(El_folder_path, file_name)) as file:
                lines = file.readlines()[1:101]
                for line in lines:
                    try:
                        row = [float(value.replace('D', 'e')) for value in line.split()]
                    except ValueError:
                        continue
                    file_dict[file_name].append(row)
            with open(os.path.join(El_folder_path, file_name)) as file: 
                lines_2 = file.readlines()[102:302]
                for line in lines_2:
                    try:
                        row = [float(value.replace('D', 'e')) for value in line.split()]
                    except ValueError:
                        continue
                    file_dict[file_name].append(row)
        for i,j in file_dict.items():
                print(i)

        for j in range(len(file_dict[sorted_file_list[0]])):
                average = round(sum(file_dict[f'{k}'][j][2] for k in sorted_file_list) / len(file_dict),30)
                error = round((sum(file_dict[f'{k}'][j][3] for k in sorted_file_list) / len(file_dict))/math.sqrt(len(file_dict)),30)
                average_list.append([file_dict[sorted_file_list[0]][j][0],file_dict[sorted_file_list[0]][j][1],average,error])


        average_file = os.path.join(El_folder_path, 'average.dat')

        with open(average_file, 'w') as file:
            for inner_list in average_list:
                line = '    '.join(str(item) for item in inner_list) + '\n'
                file.write(line)

'''
if file_name == 'average.dat':
                        file_to_delete = os.path.join(el_path, file_name)
                        os.remove(file_to_delete)
'''







