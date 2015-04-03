import os
def executeR(file_path):
	'''executes the R script'''
	os.system("Rscript "+file_path)
	return 0
def get_output(k):
	'''gets the plots'''
	f=open(k)
	content=f.read()
	content=content.split("\n")
	supportvectors=content[11]
	confusionmatrix=content[-5:]
	return supportvectors,confusionmatrix
def getMetrics(tp,tn,fp,fn):
	p=tp+fn
	n=fp+tn
	p1=tp+fp
	n1=fn+tn
	accuracy=(tp+tn)/float(p+n)
	errorrate=(fp+fn)/float(p+n)
	sensitivity=tp/float(p)
	specificity=tn/float(n)
	precision=tp/float(tp+fp)
	Fvalue=(2*precision*sensitivity)/float(precision+sensitivity)
	return accuracy,errorrate,sensitivity,specificity,precision,Fvalue
def process(confusionmatrix):
	tn=int(confusionmatrix[0].split(']')[1])
	fp=int(confusionmatrix[1].split(']')[1])
	fn=int(confusionmatrix[2].split(']')[1])
	tp=int(confusionmatrix[3].split(']')[1])
	return getMetrics(tp,tn,fp,fn)
	