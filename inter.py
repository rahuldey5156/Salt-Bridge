import os
import pandas as pd
import numpy as np

# Create a list to store the sums for each row
file_sums = {}

dat_files = [f for f in os.listdir() if f.endswith('.dat')]

# Iterate through the files in the directory
for filename in dat_files:
    if filename.endswith('.dat'):
        # Read the contents of the file
        with open(filename, 'r') as file:
            lines = pd.read_csv(file, header=None, delim_whitespace=True)

            df = pd.DataFrame(lines)

            addition = np.sum(df.iloc[:,2])/len(df.iloc[:,1])

            file_sums[filename] = addition

            sorted_file_sums = sorted(file_sums.items(), key=lambda x: x[1], reverse=True)

with open('inter.dat', 'w') as f:
    for item in sorted_file_sums:
        f.write(f'{item}\n')
