import os

# Create empty lists to store x and y values
x_values = []
y_values = []
path = "/home/sumon/CepahloMetric/Dataset_v2/average/"
main_path=  '/home/sumon/CepahloMetric/Dataset_v2/Maindatset/labels/TrainingLabels'
# Iterate over all txt files in the directory
point_data = [(0, 0, 0) for i in range(19)]
counts = {}

# Iterate over all txt files in the directory
for file in os.listdir(main_path):
    if file.endswith('.txt'):
        with open(os.path.join(main_path,file), 'r') as f:
     
            # Read all lines in the file
            lines = f.readlines()
        # Iterate over each line and extract x and y values
            for i, line in enumerate(lines):
                x, y = line.strip().split(',')
                # Add the x and y values to the sum for this point
                point_data[i] = (point_data[i][0] + float(x),
                                    point_data[i][1] + float(y),
                                    point_data[i][2] + 1)

# Calculate average x and y values for each point
averages = []
for i, (x_sum, y_sum, count) in enumerate(point_data):
    avg_x = x_sum / count
    avg_y = y_sum / count
    averages.append((i+1, avg_x, avg_y))

# Save average x and y values for each point to txt file
with open(f'{path}/average_xy.txt', 'w') as f:
    for point in averages:
        f.write(f'{point[0]},{point[1]:.4f},{point[2]:.4f}\n')