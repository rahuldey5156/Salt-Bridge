import os

# Create a list to store the sums for each row
sums = []

dat_files = [f for f in os.listdir() if f.endswith('.dat')]

# Iterate through the files in the directory
for filename in dat_files:
    if filename.endswith('.dat'):
        # Read the contents of the file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Extract the third column from each line
        third_column = [float(line.split()[2]) for line in lines]
        
        # Add the values to the sums list
        if not sums:
            sums = third_column
        else:
            sums = [x + y for x, y in zip(sums, third_column)]

# Write the sums to a new .dat file
output_file = 'total_salt_bridge.dat'
with open(output_file, 'w') as file:
    for sum_value in sums:
        file.write(str(sum_value) + '\n')

