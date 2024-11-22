from glob import glob
import os
import shutil
import subprocess
from tqdm import tqdm

dummy_path = '/scratch/nmoreau/tmp.txt'
with open(dummy_path, 'w') as dummy_file:
    dummy_file.write('modification date')

files = glob('/scratch/nmoreau/**', recursive=True)
print(f'{len(files)} files found in /scratch/frose1')

for f in tqdm(files):
    if os.path.exists(f):
        command = f'touch -r {dummy_path} "{f}"'
        rc = subprocess.run(command, shell=True)
print('Done')