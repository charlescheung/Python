#!/usr/bin/python
# Filename: cat.py
import sys
def readfile(filename):
    '''Print a file to the standard output.'''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print (line), # notice comma
        f.close()

# Script starts from here
if len(sys.argv) < 2:
    print ('No action specified.')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print ('Version 1.2')
    elif option == 'help':
        print ('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number
--help : Display this help''')
    else:
        print ('Unknown option.')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)


# sys.version
# sys.version_info
# sys模块中其他令人感兴趣的项目有sys.stdin、sys.stdout和sys.stderr它们分别对应你的程序的标准输入、标准输出和标准错误流。