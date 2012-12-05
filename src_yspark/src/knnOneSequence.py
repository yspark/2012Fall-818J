from numpy import *
import math


def knnOneSequence(k, epsilon, Xtrain, Ytrain, Xtest, Ytest):

	correct = zeros(11)
	wrong = zeros(11)
	precision = zeros(11, float)

	nearestNeighbors = zeros((k,2), dtype=float)

	maxDist = -1;
	maxIndex = -1;
	numNeighbor = 0;
	
	for trainIndex in range(len(Xtrain)):
		# normalize
		#test[testIndex] -= (mean(Xtest[0]) - mean(Xtrain[trainIndex]))
		dist = linalg.norm(Xtest-Xtrain[trainIndex])
	
		# Apply epsilon-ball
		#if dist > epsilon:
		#	continue				

		if numNeighbor < 3:
			nearestNeighbors[numNeighbor,0] = Ytrain[trainIndex]
			nearestNeighbors[numNeighbor,1] = dist
			numNeighbor+=1

			if numNeighbor == 3:							
				maxDist = nearestNeighbors[:,1].max()
				maxIndex = argmax(nearestNeighbors[:,1]) 
			#end if numNeighbor == 3:						
		elif maxDist > dist:
				nearestNeighbors[maxIndex,0] = Ytrain[trainIndex]
				nearestNeighbors[maxIndex,1] = dist

				maxDist = nearestNeighbors[:,1].max()
				maxIndex = argmax(nearestNeighbors[:,1]) 								
		#end if numNeighbor < 3:
	#end for trainIndex


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

	'''
	if Ytest[0] == prediction[0]:
		correct[Ytest[0]] += 1
	else:
		wrong[Ytest[0]] += 1

	precision = correct / (correct + wrong)
	'''
	
	print ('%d-Nearest Neighbors' % k)
	print nearestNeighbors
	print ('\nPrediction: %d Answer: %d' % (prediction[0], Ytest[0]))
	if prediction[0] == Ytest[0]:
		print ('Correct')
	else:
		print ('Wrong')
		
	
#endn def knn()
	


