import os
import re
import shutil


q = ['q0.46','q0.046','q0.0145465','q0.860581','q1','q1.49057','q1.92432','q1.2170456','q1.7511624','q2.27688','q2.58174','q2.85422','q2.1079848','q2.4340912','q2.7213967','q2.9811407','q3.10287','q3.33302','q3.54827','q3.60447','q3.75119','q3.94368','q3.2200000','q3.4423248','q3.6511368','q3.8486361','q4.0387239','q4.1337678']


file_names = os.listdir('10seeds')
for i,file_parts in enumerate(file_names) :
        
        if file_parts == '.DS_Store':
            continue
        #if file_parts.split('_')[2] in ['1','3']:
             #continue
        else:
            q_num = file_parts.split('_')[2]#2 for without NS
            el_num = file_parts.split('_')[4]#4 for without NS

            # Construct the destination folder path
            q_folder = os.path.join(f'10seeds_plot',q_num)
            el_folder = os.path.join(f'10seeds_plot',q_num,el_num)

            # Create the destination folder if it doesn't exist
            os.makedirs(q_folder, exist_ok=True)
            os.makedirs(el_folder, exist_ok=True)

            # Construct the source and target paths

            source_path = os.path.join('10seeds', file_parts)
            target_path = os.path.join(el_folder)


            # Move the file to the destination folder
            shutil.move(source_path, target_path)
