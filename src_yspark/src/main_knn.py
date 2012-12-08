import sys
import buildDataset
import knn
import knnOneSequence

from numpy import *

###########################################
#	Defines
###########################################
MEASURE_TIME_SEC = 1800
ITERATION = 5
CPU_INTERVAL = 5
NUM_FEATURE = int(MEASURE_TIME_SEC / CPU_INTERVAL)

if CPU_INTERVAL == 5:
	MIN_TEST_FEATURE_SIZE = 60
	MAX_TEST_FEATURE_SIZE = 120
	TEST_FEATURE_SIZE_STEP = 60
else:
	MIN_TEST_FEATURE_SIZE = 60
	MAX_TEST_FEATURE_SIZE = 600
	TEST_FEATURE_SIZE_STEP = 60
#endif
	


###########################################
# Input arguments process
###########################################
if len(sys.argv) >= 7:
	knnMode = int(sys.argv[1])
	movieLabel = int(sys.argv[2])
	testIndex = int(sys.argv[3])
	startOffset = int(sys.argv[4])
	length = int(sys.argv[5])

	candidateList = zeros(len(sys.argv)-6)

	for i in range(6, len(sys.argv)):
		candidateList[i-6] = int(sys.argv[i])
elif len(sys.argv) != 1:
	print('Usage: python Main_knn <No arguments>')
	print('Usage: python Main_knn <KNN Mode> <Movie Label> <Test Index (0~4)> <Start Offset> <Length> <Candidate #1> <Candidate #2> ... ')
	sys.exit()
#end if len(sys.argv) >= 6:



###########################################
# Build data set
# X: each row has 1 full movie sequence
# Y: each row has an index of movie sequence corresponding to the same row of X
###########################################
X, Y = buildDataset.buildDataset(CPU_INTERVAL)
print('buildDataset done');
		
###########################################
# No input arguments
###########################################
if len(sys.argv) == 1:
	for testFeatureSize in range(MIN_TEST_FEATURE_SIZE, MAX_TEST_FEATURE_SIZE+1, TEST_FEATURE_SIZE_STEP):

		for testSetIndex in range(1, ITERATION+1):
			Xtrain = zeros((len(X)*(NUM_FEATURE - testFeatureSize), testFeatureSize), dtype=float)
			Ytrain = zeros((len(X)*(NUM_FEATURE - testFeatureSize)), dtype=float)

			Xtest = zeros((len(X)*(NUM_FEATURE - testFeatureSize), testFeatureSize), dtype=float)
			Ytest = zeros((len(X)*(NUM_FEATURE - testFeatureSize)), dtype=float)

			trainCount = 0
			testCount = 0

			for i in range(len(X)):
				#for j in range(len(X[i]) - testFeatureSize):
				for j in range(0, len(X[i]) - testFeatureSize):
					if ((i+1) % ITERATION) == (testSetIndex % ITERATION):
						Xtest[testCount] = X[i][j:j+testFeatureSize]
						Ytest[testCount] = Y[i]
						testCount += 1
					else:
						Xtrain[trainCount] = X[i][j:j+testFeatureSize]
						Ytrain[trainCount] = Y[i]
						trainCount += 1
					#end if
				#end for j		
			#end for i

			
			Xtrain = Xtrain[0:trainCount]
			Ytrain = Ytrain[0:trainCount]
			Xtest = Xtest[0:testCount]
			Ytest = Ytest[0:testCount]

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
	Xtrain = zeros((len(X)*(NUM_FEATURE - length), length), dtype=float)
	Ytrain = zeros((len(X)*(NUM_FEATURE - length), 1), dtype=float)

	Xtest = X[(movieLabel-1)*5 + testIndex][startOffset:startOffset + length]
	Ytest = zeros(1, dtype=float) 	
	Ytest[0] = movieLabel

	trainCount = 0	
	for i in range(len(X)):
			# Build training set using the given candidate list.
			if knnMode == 1:
				if Y[i] not in candidateList:
					continue
				#end if
			#end if
	
			if i == (movieLabel-1)*5 + testIndex:
				continue
			
			for j in range(len(X[i]) - length):
				Xtrain[trainCount] = X[i][j:j+length]			
				Ytrain[trainCount] = Y[i]
				trainCount+=1
			#end for j		
	#end for i

	Xtrain = Xtrain[0:trainCount]
	Ytrain = Ytrain[0:trainCount]

			
	print('================================================================')
	print('KnnMode:%d MovieLabel:%d Index:%d StartOffset:%d Length:%d\nCandidates:' % (knnMode, movieLabel, testIndex, startOffset, length))
	print(candidateList)
	print('================================================================')
	knnOneSequence.knnOneSequence(3, length, Xtrain, Ytrain, Xtest, Ytest)
#end if len(sys.argv) >= 6:
