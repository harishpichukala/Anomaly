from mapper import mapper
from  ip2location import ip2location
class DisplayGeoIP(mapper,ip2location):
	'''Displays Geographical location of the ip address on the google map and inheritef from mapper,ip2location classes'''
	def __init__(self,ip_list,locations=[]):
		ip2location.__init__(self,ip_list)
		mapper.__init__(self,locations)
	def show(self):
		'''shows the locations'''
		self.convert_ip_to_integer()
		self.get_from_db()
		self.locations=self.get_location_info()
		self.displaylocations()
