from cStringIO import StringIO
import Image
import sys
import Tkinter
import ImageTk
import urllib
class mapper:
	'''Mapper displays the maps the latitude,longitude pairs in the google map'''
	def __init__(self):
		self.locations=None		
	def __init__(self,locations):
		self.locations=locations
	def urlgenerator(self,pattern):
		'''generates the url for  latitude,longitude '''
		self.pattern=pattern
		starting_url="https://maps.googleapis.com/maps/api/staticmap?center="
		middle_url="&zoom=12&size=400x400&markers="
		new_url=starting_url+self.pattern+middle_url+self.pattern
		return new_url
	def urlgenerator_many(self,pattern):
		'''generates the url for multiple latitude and longitude pairs'''
		self.pattern=pattern
		starting_url="http://maps.google.com/maps/api/staticmap?"
		middle_url="size=1800x800&markers="
		new_url=starting_url+middle_url+self.pattern+"&sensor=false"
		return new_url
	def geturl(self):
		'''returns the url generated'''
		locations=self.locations[0]
		latitude=locations[0]
		longitude=locations[1]
		pattern=latitude+","+longitude;
		url=self.urlgenerator(pattern)
		return url
	def getstaticimage(self,url):
		'''gets the static image from google maps'''
		self.url=url
		buffer=StringIO(urllib.urlopen(url).read())
		self.map=Image.open(buffer)
		return self.map
	def geturl_many(self):
		'''gets the url generated for multiple latitude and longitude pairs'''
		marker_list=[]
		for i in self.locations:
			marker_list.append(i[0]+","+i[1])
		pattern=''
		for j in marker_list:
			pattern+=j+'|'
		pattern=pattern[0:len(pattern)-1]
		url=self.urlgenerator_many(pattern)
		return url
	
	def getmap(self):
		'''displays the map to the user'''
		root=Tkinter.Tk()
		mapimage=ImageTk.PhotoImage(self.map)
		panel=Tkinter.Label(root,image=mapimage)
		panel.pack()
		root.mainloop()
	def displaylocations(self):
		'''displays the locations on the google maps to the corresponding latitude and longitide pairs'''
		if len(self.locations)==1:
			url=self.geturl()
		elif len(self.locations)>1:
			url=self.geturl_many()
		else:
			sys.exit(0)
		self.getstaticimage(url)	
		self.getmap()
		
		