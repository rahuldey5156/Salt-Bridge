import os
import pandas as pd
import numpy as np

# Create a list to store the sums for each row
file_sums = {}

files_to_read = [f for f in os.listdir() if f.endswith('.dat') and f != 'total_salt_bridge.dat']

# Iterate through the files in the directory
for filename in files_to_read:
    if filename.endswith('.dat'):
        # Read the contents of the file
        with open(filename, 'r') as file:
            lines = pd.read_csv(file, header=None, delim_whitespace=True)

            df = pd.DataFrame(lines)

            addition = np.sum(df.iloc[:,2])

            file_sums[filename] = addition

            sorted_file_sums = sorted(file_sums.items(), key=lambda x: x[1], reverse=True)

with open('move_files.sh', 'w') as f:
    for item in sorted_file_sums[:40]:  #This will fetch the names of 40 datafiles with highest value of salt bridge
        f.write(f'cp {item[0]} final_salt_bridge/\n')

            
