# !/usr/bin/python
# Filename: pickling.py
# import cPickle as p
# import pickle as p
# shoplistfile = 'shoplist.data'
# # the name of the file where we will store the object
# shoplist = ['apple', 'mango', 'carrot']
# # Write to the file
# f = open(shoplistfile, 'w')
# p.dump(shoplist, f) # dump the object to a file
# f.close()
# del shoplist # remove the shoplist
# # Read back from the storage
# f = open(shoplistfile)
# storedlist = p.load(f)
# print(storedlist)


# import pickle
# object = ['apple', 'mango', 'carrot']
#
# file   = open('test.txt', 'wb')     # Create external file
# pickle.dump(object, file)         # Save object in file
# import pickle
# file   = open('test.txt', 'rb')
# object = pickle.load(file)        # Fetch it back later
# print(object)

import shelve
object = ['apple', 'mango', 'carrot']
dbase  = shelve.open('test1.txt')
dbase['key'] = object             # Save under key
import shelve
dbase1 = shelve.open('test1.txt')
object1 = dbase1['key']             # Fetch it back later
print(object1)



