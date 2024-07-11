import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import time


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
        if El_folder == '.DS_Store':
            continue
        El_folder_path = os.path.join(q_folder_path, El_folder)
        
        file_dict = {}
        fig, ax = plt.subplots()
        sorted_file_list = sorted(os.listdir(El_folder_path), key=sorting_key)
        sorted_file_list = [file_name for file_name in sorted_file_list if file_name not in ['.DS_Store', 'linear_plot.png', 'log_plot.png', 'log_ratio_plot.png', 'linear_ratio_plot.png']]

        for file_name in sorted_file_list:
            if file_name == 'average.dat':
                lines = pd.read_csv(os.path.join(El_folder_path, file_name), header=None, skiprows=100, delimiter=r"\s+")
                print(lines)
                for i in range(len(lines)):
                    if lines.iloc[i, 2] == 0:
                        continue
                    bin_center = (lines.iloc[i, 0] + lines.iloc[i, 1]) / 2
                    bin_width = lines.iloc[i, 1] - lines.iloc[i, 0]
                    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2],
                        [lines.iloc[i,2], lines.iloc[i,2]],
                        color=color(file_name), linewidth=1)
            else:
                lines = pd.read_csv(os.path.join(El_folder_path, file_name), header=None, skiprows=272, delimiter=r"\s+", converters={0: replace_D_with_e,1: replace_D_with_e,2: replace_D_with_e, 3: replace_D_with_e})
                for i in range(len(lines)):
                    if lines.iloc[i, 2] == 0:
                        continue
                    bin_center = (lines.iloc[i, 0] + lines.iloc[i, 1]) / 2
                    bin_width = lines.iloc[i, 1] - lines.iloc[i, 0]
                    ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2],
                        [lines.iloc[i,2], lines.iloc[i,2]],
                        color=color(file_name), linewidth=1)
        plt.savefig(os.path.join(El_folder_path, "linear_ratio_plot_test.png"), dpi=1000)

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

'''
b = 0
perci = 1000
for i in range(perci):
    c=0
    for j in range(7):
        a = random.choice([1,0])
        if a == 1:
            c = c+1
    if  c >=5:
        b = b+1
print((b/perci)*100)



