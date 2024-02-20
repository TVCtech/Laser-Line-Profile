import numpy as np


# Define the path to your file
file_path = 'testweld.lpd'

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process each line
data = []
for line in lines:
    # Split the line by commas
    split_line = line.strip().split(',')
    # Convert each part to float and append to the data list
    data.append([float(value) for value in split_line])

# Convert the list to a NumPy array
data_array = np.array(data)