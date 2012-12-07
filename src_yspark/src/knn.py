from numpy import *
import math
import sys

def knn(k, epsilon, Xtrain, Ytrain, Xtest, Ytest):

	correct = zeros(11)
	wrong = zeros(11)
	precision = zeros(11, float)

	for testIndex in range(0, len(Xtest)):
		#print('Processing %d/%d' % (testIndex, len(Xtest)))

		nearestNeighbors = zeros((k,2), dtype=float)

		maxDist = -1;
		maxIndex = -1;
		numNeighbor = 0;

		for trainIndex in range(len(Xtrain)):
			# normalize
			#Xtest[testIndex] -= (mean(Xtest[testIndex]) - mean(Xtrain[trainIndex]))

			dist = linalg.norm(Xtest[testIndex]-Xtrain[trainIndex])

			# Apply epsilon-ball
			#if dist > epsilon:
			#	continue				

			if numNeighbor < k:
				nearestNeighbors[numNeighbor,0] = Ytrain[trainIndex]
				nearestNeighbors[numNeighbor,1] = dist
				numNeighbor+=1

				if numNeighbor == k:							
					maxDist = nearestNeighbors[:,1].max()
					maxIndex = argmax(nearestNeighbors[:,1]) 
				#end if numNeighbor == k:						
			elif maxDist > dist:
					nearestNeighbors[maxIndex,0] = Ytrain[trainIndex]
					nearestNeighbors[maxIndex,1] = dist

					maxDist = nearestNeighbors[:,1].max()
					maxIndex = argmax(nearestNeighbors[:,1]) 								
			#end if numNeighbor < k:		
		#end for trainIndex

		'''
		# remove rows with (0,0)
		nearestNeighbors = nearestNeighbors[nearestNeighbors.all(1)]		
		counts = bincount(array(nearestNeighbors2[:,0], dtype=int))
		countsArgsort = argsort(counts)

		print nearestNeighbors2
		'''

		# remove rows with (0,0)
		nearestNeighbors = nearestNeighbors[nearestNeighbors.all(1)]		

		#							id, 	count, mean, min
		prediction = [-1,	-1,		-1, 	-1]

		for i in range(len(nearestNeighbors)):
			if nearestNeighbors[i,0] == 0 and nearestNeighbors[i,1] == 0:
				continue
			#end if

			tempArr = nearestNeighbors[nearestNeighbors[:,0] == nearestNeighbors[i,0]]				

			if (prediction[0] == -1) or (prediction[1] < len(tempArr)) or (prediction[1] == len(tempArr) and prediction[2] > mean(tempArr[:,1])):
				prediction = [nearestNeighbors[i,0], len(tempArr), mean(tempArr[:,1]), min(tempArr[:,1])]
			#end if
		#end for

		if Ytest[testIndex] == prediction[0]:
			correct[Ytest[testIndex]] += 1
		else:
			wrong[Ytest[testIndex]] += 1

		precision = correct / (correct + wrong)
	#end for testIndex

	for i in range(1,11):
		sys.stdout.write('%f\t' % precision[i])
	#end for
	sys.stdout.write('\n')
		
#endn def knn()	