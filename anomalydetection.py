from Tkinter import *
from svm_wrapper import *
import knncommand as k
from imageviewer import Viewer
from glob import glob
class Anomaly:
	'''anomaly detection'''
	def reload(self):
		for child in self.frame1.winfo_children():
			child.destroy()
	def svm(self):
		self.reload()
		self.txt=Text(self.frame1)
		self.txt.insert(INSERT,"")
		self.s=Scrollbar(self.frame1)
		self.s1=Scrollbar(self.frame1)
		out=process_svm()
		self.txt.insert(INSERT,out)
		self.s.pack(side=RIGHT,fill=Y)
		self.txt.config(yscrollcommand=self.s.set)
		self.txt.pack(side=LEFT,fill=BOTH)
		self.txt.config(state="disabled")
		self.s.config(command=self.txt.yview)
		self.frame1.pack()
		return
	def knn(self):
		k.get_knn()
		return
	def lof(self):
		self.reload()
		k=glob("*.jpg")
		self.a=Viewer(self.frame1,k)
		self.frame1.pack()
		return 	
	def app(self):
		self.win=Tk()
		self.win.title("Anomaly detection")
		self.win.geometry('600x400')
		self.frame1=Frame(self.win)
		self.f=Frame(self.win)
		self.label=Label(self.f,text="\n")
		self.label.pack()
		self.txt=Text(self.frame1)
		self.Button1=Button(self.f,text="K-Nearest Neighbour",command=self.knn)
		self.Button2=Button(self.f,text="support vector Machine",command=self.svm)
		self.Button3=Button(self.f,text="local outlier factor",command=self.lof)
		self.Button1.pack(side=LEFT)
		self.Button2.pack(side=LEFT)
		self.Button3.pack(side=LEFT)
		self.f.pack(fill=BOTH)
		self.a.title.destroy()
		self.win.mainloop()
