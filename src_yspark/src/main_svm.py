import buildDataset
import knn

from numpy import *


MEASURE_TIME_SEC = 1800
ITERATION = 5
CPU_INTERVAL = 5
NUM_FEATURE = int(MEASURE_TIME_SEC / CPU_INTERVAL)

MIN_TEST_FEATURE_SIZE = 12
MAX_TEST_FEATURE_SIZE = 36
TEST_FEATURE_SIZE_STEP = 6

TESTSET_INDEX = 5


X, Y = buildDataset.buildDataset(CPU_INTERVAL)


for testFeatureSize in range(MIN_TEST_FEATURE_SIZE, MAX_TEST_FEATURE_SIZE+1, TEST_FEATURE_SIZE_STEP):
	for testSetIndex in range(1, ITERATION+1):
		Xtrain = zeros(testFeatureSize, dtype=float)
		Ytrain = zeros(1, dtype=float)

		Xtest = zeros(testFeatureSize, dtype=float)
		Ytest = zeros(1, dtype=float)

		for i in range(len(X)):
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




###################################
# supervised
###################################
'''
f_tr = "tool.train"
f_tm = "tool.test"
f_mm = "tool.model"
f_pm = "tool.predict"

Xtr, Ytr, Xte, Yte = util.splitTrainTest(X0, Y0, 5)


print "###### running megam ######"
runClassifier.dumpMegamFormat(f_tr, f_tm, Xtr, Ytr, Xte, Yte)
os.system("megam -fvals binary %s > %s" % (f_tr, f_mm))
os.system("megam -fvals -predict %s binary %s > %s" % (f_mm, f_tm, f_pm))

print "###### running SVM ######"
runClassifier.dumpSVMFormat(f_tr, f_tm, Xtr, Ytr, Xte, Yte)
os.system("svm-train -t 2 -g 0.01 -h 0 %s %s" % (f_tr, f_mm))
os.system("svm-predict %s %s %s" % (f_tm, f_mm, f_pm))
'''
