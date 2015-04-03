from snortloader import *
def signature_detection():
	'''signature detection'''
	s=snortloader("test.pcap")
	k=s.scanner()
	k=k.split("\n")
	src_list=[]
	dst_list=[]
	for i in k:
		i=i.split(" ")
		try:
			src_list.append(i[-4])
			dst_list.append(i[-2])
		except IndexError:
			pass
	return src_list,dst_list

	