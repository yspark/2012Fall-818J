from numpy import *


arr = array([[1, 11.5],[1,5.3],[10,11.2]])

print (arr[arr[:,0] == 1], axis=0)

print arr[:,0].count(1)

#arr2 = concatenate( (arr[arr[:,0] == 1], 