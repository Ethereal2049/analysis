import os 

'''
for folder_name in os.listdir('seeds_q'):
    print(folder_name)

def process_file(file_name,q_number,start_1, end_1, start_2, end_2):
    for folder_name in os.listdir('seeds_q'):
        for El in folder_name:
            for files in El:
                print(files)

'''


for folder_name_qs in os.listdir('10seeds_plot'):
    if folder_name_qs == '.DS_Store':
        continue
    else:
        folder_path_qs = os.path.join('10seeds_plot', folder_name_qs)
        for el_num in os.listdir(folder_path_qs):
            file_dict = {}
            average_list = []
            if el_num == '.DS_Store':
                continue
            else:
                el_path = os.path.join(folder_path_qs, el_num)
                for i,file_name in enumerate(os.listdir(el_path)):
                    if file_name == '.DS_Store':
                        continue
                    else:
                        path = os.path.join(el_path,file_name)
                        if file_name == 'log_ratio_plot.png':
                            file_to_delete = os.path.join(el_path, file_name)
                            os.remove(file_to_delete)
'''
                        key = f"{i}"
                        file_dict[key] = []
                        print(i,file_name)
                        with open(path) as file:
                            lines = file.readlines()[171:271]
                            for line in lines:
                                row = [float(value.replace('D', 'e')) for value in line.split()]
                                file_dict[key].append(row)
                        with open(path) as file:
                            lines_2 = file.readlines()[272:473]
                            for line in lines_2:
                                try:
                                    row = [float(value.replace('D', 'e')) for value in line.split()]
                                except ValueError:
                                    continue
                                file_dict[key].append(row)
                                
            for j in range(len(file_dict['0'])):
                    average = sum(file_dict[f'{k}'][j][2] for k in range(len(file_dict))) / len(file_dict)
                    error = sum(file_dict[f'{k}'][j][3] for k in range(len(file_dict))) / len(file_dict)
                    average_list.append([file_dict['0'][j][0],file_dict['1'][j][1],round(average, 16),round(error, 20)])

                    
            average_file = os.path.join(el_path, 'average.dat')

            with open(average_file, 'w') as file:
                for inner_list in average_list:
                    line = '    '.join(str(item) for item in inner_list) + '\n'
                    file.write(line)
'''
'''
                    for j in range(len(file_dict[0])):
                        average = (file_dict[0][j][2]+file_dict[1][j][2]+file_dict[2][j][2]+file_dict[3][j][2])/4
                        error = (file_dict[0][j][3]+file_dict[1][j][3]+file_dict[2][j][3]+file_dict[3][j][3])/4
                        average_list.append([file_dict[0][j][0],file_dict[0][j][1],round(average,16),round(error,20)])
            average_file= os.path.join(f'seeds_q',q_num)
            os.makedirs(q, exist_ok=True)
'''
 
                    




























                
'''
q = ['q0.46','q0.046','q0.860581','q1.49057','q1.92432','q1.2170456','q1.7511624','q2.27688','q2.58174','q2.85422','q2.1079848','q2.4340912','q2.7213967','q2.9811407','q3.10287','q3.33302','q3.54827','q3.60447','q3.75119','q3.94368','q3.2200000','q3.4423248','q3.6511368','q3.8486361','q4.0387239','q4.1337678']
average_name = input("folder#: ")
name = ['6_6', '6_7', '6_8', '6_9']
file_dict = {n: [] for n in name}
average_list = []
for i in name:
    process_file(i, 171, 271, 272, 473)

for j in range(len(file_dict[name[0]])):
    average = (file_dict[name[0]][j][2]+file_dict[name[1]][j][2]+file_dict[name[2]][j][2]+file_dict[name[3]][j][2])/4
    error = (file_dict[name[0]][j][3]+file_dict[name[1]][j][3]+file_dict[name[2]][j][3]+file_dict[name[3]][j][3])/4
    average_list.append([file_dict[name[0]][j][0],file_dict[name[0]][j][1],round(average,16),round(error,20)])

with open(f'average_{average_name}.dat', 'w') as file:
    for inner_list in average_list:
        line = '    '.join(str(item) for item in inner_list) + '\n'
        file.write(line)
'''





'''
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

'''

'''
data_2= np.genfromtxt('NNLO4.6_7_q1_uh_El0_sam0_ode3.dat',skip_header=1,converters={i: replace_d_with_e for i in range(4)}, names=['s', 'e', 'h', 'er'])
data_3= np.genfromtxt('NNLO4.6_8_q1_uh_El0_sam0_ode3.dat', skip_header=1,converters={i: replace_d_with_e for i in range(4)},names=['s', 'e', 'h', 'er'])
data_4= np.genfromtxt('NNLO4.6_9_q1_uh_El0_sam0_ode3.dat', skip_header=1,converters={i: replace_d_with_e for i in range(4)},names=['s', 'e', 'h', 'er'])
data_a= np.genfromtxt('average.dat',names=['s', 'e', 'h', 'er'])
'''
#test method
'''
def replace_d_with_e(value):
    return value.replace('D', 'e')

data_1= np.genfromtxt('NNLO4.6_6_q1_uh_El0_sam0_ode3.dat', converters={i: replace_d_with_e for i in range(4)},names=['s', 'e', 'h', 'er'])
data_2= np.genfromtxt('NNLO4.6_7_q1_uh_El0_sam0_ode3.dat',converters={i: replace_d_with_e for i in range(4)}, names=['s', 'e', 'h', 'er'])
data_3= np.genfromtxt('NNLO4.6_8_q1_uh_El0_sam0_ode3.dat', converters={i: replace_d_with_e for i in range(4)},names=['s', 'e', 'h', 'er'])
data_4= np.genfromtxt('NNLO4.6_9_q1_uh_El0_sam0_ode3.dat', converters={i: replace_d_with_e for i in range(4)},names=['s', 'e', 'h', 'er'])
data_a= np.genfromtxt('average.dat',names=['s', 'e', 'h', 'er'])
'''

#method 2
'''

# Replace 'D' with 'e' and append the modified lines to the list
for line in lines:
    modified_line_1 = ''.join(['20' if c.isalpha() and c.upper() != 'D' else c for c in line])
    modified_line_2 = modified_line_1.replace('D', 'e')
    modified_line = modified_line_2.replace('\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '20')


    modified_data_list.append([modified_line.strip()])
'''







'''
def fit_function(x, a, b, c, d,e,f,g,h,j,z,l):
    return a * np.log(x)/x+ b * x**6 + c*x**5+ d*x**4 + e*x**3 + f*x**2+ g*x +h*x**7+j+z*x**8+l/x

params, covariance = curve_fit(fit_function, x, y)
a_fit, b_fit, c_fit, d_fit,e_fit,f_fit,g_fit,h_fit,j_fit,z_fit,l_fit= params

y_fit = fit_function(x, a_fit, b_fit, c_fit, d_fit,e_fit,f_fit,g_fit,h_fit,j_fit,z_fit,l_fit)
print("Optimized parameters:")
print(f"a_fit: {a_fit}")
print(f"b_fit: {b_fit}")
print(f"b_fit: {c_fit}")
print(f"b_fit: {d_fit}")
print(f"b_fit: {e_fit}")
print(f"b_fit: {f_fit}")
print(f"b_fit: {g_fit}")
print(f"b_fit: {h_fit}")

plt.plot(x, y_fit, color='red', label='Best Fit Line')
plt.scatter(x, y, color='blue', label='Data points')
plt.show()
'''