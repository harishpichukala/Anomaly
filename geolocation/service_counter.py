from collections import Counter
def service_count():
	f=open("services.txt")
	k=f.read()
	l=k.split("\n")
	l=Counter(l)
	print l
	return l
l=service_count()