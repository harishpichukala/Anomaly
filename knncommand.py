from knn import compare
from Knndisplay import display_knn
import time
def get_knn():
	start_time=time.time()
	compare()
	display_knn()
	end_time=time.time()
	print end_time-start_time
	