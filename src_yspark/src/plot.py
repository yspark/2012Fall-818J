from numpy import *
import pylab

NUM_MOVIE = 10
NUM_TRIALS = 5

def extractFeature(fname):
	dataset = []
	f = open(fname, 'r')
	for line in f:
		dataset.append(int(line))

	#end for line in f:

	return array(dataset)
#end def extractFeature():


sec = 1

for i in range(NUM_MOVIE):
#for i in range(1):		
	for j in range(NUM_TRIALS):
		temp = extractFeature("./android_%dsec/%d_%dsec_0%d_cpu.txt" % (sec, i+1, sec, j+1))

	 	x_axis = arange(0,len(temp))
	 	pylab.plot(x_axis, temp)

		pylab.xlabel('time (%d sec)' % sec)
		pylab.ylabel('CPU Usage')
		pylab.title('Movie #%d' % (i+1))
		pylab.savefig('./figures/fig_%d' % (i+1))
	#end for j in range(5):

	pylab.show()
#end for i in range(NUM_MOVIE):






'''
t = numpy.arange(0.0, 1.0+0.01, 0.01)
s = numpy.cos(2*2*numpy.pi*t)
pylab.plot(t, s)

pylab.xlabel('time (s)')
pylab.ylabel('voltage (mV)')
pylab.title('About as simple as it gets, folks')
pylab.grid(True)
pylab.savefig('simple_plot')

pylab.show()
'''
