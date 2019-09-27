
import os

path = '/---file dir----'

# you can get the filename and folder name
files = os.listdir(path)

# If you want to get only filename, you should use the following func.

files = []
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        files.append(filename)

print(files)







import glob

path = '/-----file name -----'

files = glob.glob(os.path.join(path, '*'))


# If you want to get only filename, you should use the following func.

os.chdir(path)
files = glob.glob('*.txt')





import os
path = '/----file name----'
for d, s, f in os.walk(path):
    print('')
    print('--{}'.format(d))
    print(' |--{}'.format(s))
    print('    |--{}'.format(f))

