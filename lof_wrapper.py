from R_wrapper  import *
from imageviewer import *
def lof():
	print "after execution of R script"
	k=get_files_list()
	print k
	viewfiles(k)

executeR("lofd.r")
	
