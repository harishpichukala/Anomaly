from R_wrapper import *
def process_svm():
	s,c=get_output("summary_svm.txt")
	accuracy,errorrate,sensitivity,specificity,precision,Fvalue=process(c)
	output="%s\naccuracy:%s\nerrorrate:%s\nsensitivity:%s\nspecificity:%s\nprecision:%s\nFvalue:%s" %(s,accuracy,errorrate,sensitivity,specificity,precision,Fvalue)
	#print(output)
	return output

executeR("svm.r")
	