import pandas as pd
import os

path = "/home/sumon/CepahloMetric/Dataset_v2/predicted_csv/datapredicts_patch0_ref.csv"
dest = "/home/sumon/CepahloMetric/Dataset_v2/patchMainImages/ForHrnet/predicted_txt/patch_0_ref"

if not os.path.exists(dest):
    os.makedirs(dest)
# Read the CSV file into a pandas dataframe
df = pd.read_csv(path)

# Iterate over the rows and save each xy pair in a separate text file
i =151
for index, row in df.iterrows():
    x = row['original_0_x']
    y = row['original_0_y']
    print(x,y)
    with open(f'{dest}/{i}.txt', 'w') as f:
        f.write(f'{x},{y}')
    i =i+1
