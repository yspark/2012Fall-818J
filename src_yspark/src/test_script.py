import os

for i in range(0,1200):
	cmd = 'python main_knn.py 1 0 %d 60 1 2 3' % (i)
	os.system(cmd)
#end for



