from numpy import *

NUM_MOVIE = 10
NUM_TRIALS = 5

def buildDataset(sec):
	X = []
	Y = []

	for i in range(NUM_MOVIE):
	#for i in range(1):
		for j in range(NUM_TRIALS):
			temp = extractFeature("./android_%dsec/%d_%dsec_0%d_cpu.txt" % (sec, i+1, sec, j+1))

			'''
			if i == 0:
				numFeatures = len(temp)
			else:
				numFeatures = min(len(temp), numFeatures)
			#end if
			'''

			X.append(temp)
			Y.append(i+1)

		#end for j in range(5):
	#end for i in range(NUM_MOVIE):


	
	return X, Y

#end buildDataset():


def extractFeature(fname):
	dataset = []
	f = open(fname, 'r')
	for line in f:
		dataset.append(int(line))

	#end for line in f:

	return array(dataset)
#end def extractFeature():


