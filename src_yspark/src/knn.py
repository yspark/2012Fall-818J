from numpy import *
import math


def knn(k, epsilon, Xtrain, Ytrain, Xtest, Ytest):

	correct = zeros(11)
	wrong = zeros(11)
	precision = zeros(11, float)


	for testIndex in range(testInteration):
		#print testIndex, len(Xtest)

		nearestNeighbors = zeros((k,2), dtype=float)

		for trainIndex in range(len(Xtrain)):
			# normalize
			#test[testIndex] -= (mean(Xtest[testIndex]) - mean(Xtrain[trainIndex]))
			dist = linalg.norm(Xtest[testIndex]-Xtrain[trainIndex])
		
			# Apply epsilon-ball
			if dist > epsilon:
				continue				

			minDist = nearestNeighbors[:,1].min()
			minIndex = argmin(nearestNeighbors[:,1]) 
			
			maxDist = nearestNeighbors[:,1].max()
			maxIndex = argmax(nearestNeighbors[:,1]) 
			
			if minDist == 0 and nearestNeighbors[minIndex,0] == 0:
				nearestNeighbors[minIndex,0] = Ytrain[trainIndex]
				nearestNeighbors[minIndex,1] = dist
			elif maxDist > dist:
				nearestNeighbors[maxIndex,0] = Ytrain[trainIndex]
				nearestNeighbors[maxIndex,1] = dist
			#end if			
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

		#print prediction[0]

		#print nearestNeighbors
		#print prediction[0]
		#print precision
		
	#end for testIndex

	print precision

#endn def knn()
	


