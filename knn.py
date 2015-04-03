import csv
import random
import math
import operator
import time
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(41):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getConfusionMatrix(testSet, predictions):
	tp = 0
	tn = 0
	fp = 0
	fn = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			if predictions[x]=='normal':
				tp=tp+1
			else:
				tn=tn+1
		else:
			if testSet[x][-1] == 'normal':
				fn=fn+1
			else:
				fp=fp+1
			
	#print "tp:%d,tn:%d,fp:%d,fn:%d" %(tp,tn,fp,fn)
	return tp,tn,fp,fn
def getMetrics(tp,tn,fp,fn):
	accuracy=0
	errorrate=0
	sensitivity=0
	specificity=0
	precision=0
	Fvalue=0
	p=tp+fn
	n=fp+tn
	p1=tp+fp
	n1=fn+tn
	#print p
	#print n
	try:
		accuracy=(tp+tn)/float(p+n)
		errorrate=(fp+fn)/float(p+n)
		sensitivity=tp/float(p)
		specificity=tn/float(n)
		precision=tp/float(tp+fp)
		Fvalue=(2*precision*sensitivity)/float(precision+sensitivity)
	except:
		pass
	
	return accuracy,errorrate,sensitivity,specificity,precision,Fvalue
		
def run(n,data):
	# prepare data
	l=[]
	trainingSet=[]
	testSet=[]
	split = 0.66
	loadDataset(data, split, trainingSet, testSet)
	#print 'Train set: ' + repr(len(trainingSet))
	#print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	k = n
	t1=time.time()
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	t2=time.time()
	tp,tn,fp,fn = getConfusionMatrix(testSet, predictions)
	totaltime=t2-t1
	a,b,c,d,e,f=getMetrics(tp,tn,fp,fn)	
	l.append(a)
	l.append(b)
	l.append(c)
	l.append(d)
	l.append(e)
	l.append(f)
	return l
	
def compare():
	k=[]
	for i in [1,3,5,7,9,11,13,17]:
		k.append(run(i,"knn_dataset.csv"))
	with open('metrics.csv','wb') as csvfile:
			rowwriter=csv.writer(csvfile,delimiter=',')
			for j in k:
				rowwriter.writerow(j);
				