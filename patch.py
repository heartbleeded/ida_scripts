## Patch dylibs binaries to allow IDApython running with self-installed python.
## I use default brew python as follow
## phdphuc 2018

from os import listdir
from os.path import isfile, join
def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print '"{old_string}" not found in {filename}.'.format(**locals())
            return
    with open(filename, 'w') as f:
        print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)

dir = ['./python/lib/python2.7/lib-dynload/ida_64', './python/lib/python2.7/lib-dynload/ida_32', './plugins']
for d in dir:        
	onlyfiles = [f for f in listdir(d) if isfile(join(d, f))]
	for file in onlyfiles:
		inplace_change(join(d, file), "/System/Library/Frameworks/Python.framework/", "/usr/local//////Frameworks/Python.framework/")