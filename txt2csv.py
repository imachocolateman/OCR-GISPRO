import pandas as pd
import numpy as np
from os import listdir
import sys

if len(sys.argv) < 2:
    print("Must specify path of Text folder")
    print("exiting...")
    sys.exit(1)

txt_path = sys.argv[1]
target_dir = txt_path + "../csv/"
no_columns = 60

onlyfiles = [f for f in listdir(txt_path) if '.txt' in f]

def txt_to_pd_to_csv(file, no_columns=no_columns):
	print(f"Loading File: {file}")
	columns = [index for index in range(no_columns)]
	df = pd.DataFrame(columns = columns)
	with open(txt_path + file, 'r', encoding='utf-8') as f:
		for i, line in enumerate(f):
			row = line.replace(" (m)", "(m)").split()
			if len(row) != 0:
				row_array = np.array(row)
				df = df.append(
					pd.Series(
						row_array, name=("line" + str(i))
					))
				df.to_csv(target_dir + file.strip('.txt') + '.csv')
		print(f"Saved: {file}")
		print("--------------")
	return

for file in range(len(onlyfiles)):
	txt_to_pd_to_csv(onlyfiles[file])

