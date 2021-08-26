import os
import pathlib
import glob
import shutil

# Can use isdir, islink etc as well
print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))

# os.rename('test.txt', 'renamed.txt')
# os.symlink('renamed.txt', 'synlink.txt')

os.mkdir('test_dir')
os.rmdir('test_dir')

# Since Python3
pathlib.Path('empty.txt').touch()
os.remove('empty.txt')

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))
pathlib.Path('test_dir/test_dir2/empty.txt').touch()
shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')

# ['test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt']
print(glob.glob('test_dir/test_dir2/*'))

# 사용할 때 주의!
shutil.rmtree('test_dir')

# /Users/woohyeok.kim/Desktop/study/python ... project home
print(os.getcwd())
