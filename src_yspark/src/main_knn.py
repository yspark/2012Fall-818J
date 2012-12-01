import sys
import buildDataset
import knn
import knnOneSequence

from numpy import *


MEASURE_TIME_SEC = 1800
ITERATION = 5
CPU_INTERVAL = 5
NUM_FEATURE = int(MEASURE_TIME_SEC / CPU_INTERVAL)

MIN_TEST_FEATURE_SIZE = 12
MAX_TEST_FEATURE_SIZE = 36
TEST_FEATURE_SIZE_STEP = 6

TESTSET_INDEX = 5

###########################################
# Input arguments process
###########################################
if len(sys.argv) >= 6:
	movieLabel = int(sys.argv[1])
	testIndex = int(sys.argv[2])
	startOffset = int(sys.argv[3])
	length = int(sys.argv[4])

	candidateList = zeros(len(sys.argv)-5)

	for i in range(5, len(sys.argv)):
		candidateList[i-5] = int(sys.argv[i])
elif len(sys.argv) != 1:
	print('Usage: python Main_knn <No arguments>')
	print('Usage: python Main_knn <Movie Label> <Test Index (1-5)> <Start Offset> <Length> <Candidate #1> <Candidate #2> ... ')
	sys.exit()
#end if len(sys.argv) >= 6:



###########################################
# Build data set
# X: each row has 1 full movie sequence
# Y: each row has an index of movie sequence corresponding to the same row of X
###########################################
X, Y = buildDataset.buildDataset(CPU_INTERVAL)

		
###########################################
# No input arguments
###########################################
if len(sys.argv) == 1:
	for testFeatureSize in range(MIN_TEST_FEATURE_SIZE, MAX_TEST_FEATURE_SIZE+1, TEST_FEATURE_SIZE_STEP):

		for testSetIndex in range(1, ITERATION+1):
			Xtrain = zeros(testFeatureSize, dtype=float)
			Ytrain = zeros(1, dtype=float)

			Xtest = zeros(testFeatureSize, dtype=float)
			Ytest = zeros(1, dtype=float)

			for i in range(len(X)):
				#for j in range(NUM_FEATURE):
				for j in range(len(X[i]) - testFeatureSize):
					if ((i+1) % ITERATION) == (testSetIndex % ITERATION):
						Xtest = vstack((Xtest, X[i][j:j+testFeatureSize]))
						Ytest = concatenate((Ytest, [Y[i]]), axis=1)
					else:
						Xtrain = vstack((Xtrain, X[i][j:j+testFeatureSize]))	
						Ytrain = concatenate((Ytrain, [Y[i]]), axis=1)
					#end if
				#end for j		
			#end for i

			
			Xtrain = Xtrain[1:len(Xtrain)]
			Ytrain = Ytrain[1:len(Ytrain)]
			Xtest = Xtest[1:len(Xtest)]
			Ytest = Ytest[1:len(Ytest)]

			'''
			dataset.X = Xtrain
			dataset.Y = Ytrain
			dataset.Xte = Xtest
			dataset.Yte = Ytest
			'''

			#print len(Xtrain), len(Ytrain), len(Xtest), len(Ytest)

			print('================================================================')
			print('KNN (Feature %d, TestSet %d)' % (testFeatureSize, testSetIndex))
			print('================================================================')
			knn.knn(3, testFeatureSize, Xtrain, Ytrain, Xtest, Ytest)
		#end for testSetIndex
	#end for testFeatureSize
#end 	if len(sys.argv) == 1:

	

###########################################
# Full input arguments
###########################################
if len(sys.argv) >= 6:
		Xtrain = zeros(length, dtype=float)
		Ytrain = zeros(1, dtype=float)

		Xtest = X[(movieLabel-1)*5 + testIndex][startOffset:startOffset + length]
		Ytest = zeros(1, dtype=float) 	
		Ytest[0] = movieLabel

		for i in range(len(X)):
			if i == (movieLabel-1)*5 + testIndex:
				continue
			
			for j in range(len(X[i]) - length):
				Xtrain = vstack((Xtrain, X[i][j:j+length]))	
				Ytrain = concatenate((Ytrain, [Y[i]]), axis=1)
			#end for j		
		#end for i

		print('================================================================')
		print('MovieLabel:%d Index:%d StartOffset:%d Length:%d\nCandidates:' % (movieLabel, testIndex, startOffset, length))
		print(candidateList)
		print('================================================================')
		knnOneSequence.knnOneSequence(3, length, Xtrain, Ytrain, Xtest, Ytest)
#end if len(sys.argv) >= 6:
