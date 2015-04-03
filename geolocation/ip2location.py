import MySQLdb as m
import sys
class ip2location:
	'''using this class we can get the geographical info. of the ip address in octet format'''
	def __init__(self,ip):
		self.ip=ip
		self.ip_list=[]
		self.results_list=[]
		self.locations_list=[]
	def connect(self):
		'''connection to the mysql database where geographical information is saved'''
		c=m.connect(host="127.0.0.1",port=3306,user="root",passwd="password",db="ip2location")
		return c
	def convert_ip_to_integer(self):
		'''converts the ip in octet format into integer'''
		for i in self.ip:
			ipaddress=i
			ip_octets=ipaddress.split('.')
			k=ip_octets
			a=int(k[0])
			b=int(k[1])
			c=int(k[2])
			d=int(k[3])
			self.ip_list.append(a*16777216+b*65536+c*256+d)
		return self.ip_list
	def get_from_db(self):
		'''retrieves the info. from database'''
		c=self.connect()
		cur=c.cursor()
		for ip_int in self.ip_list:
			self.ip_int=ip_int
			sql="select * from ip2location_db11 where ip_from<"+str(self.ip_int)+" and ip_to>="+str(self.ip_int)
			#print sql
			cur.execute(sql)
			self.results=cur.fetchall()
			self.results_list.append(self.results[0])
		c.close()
		return self.results_list

	def get_location_info(self):
		'''returns the locations info'''
		for  r in self.results_list:
			print "country:"+r[3]
			print "region name:"+r[4]
			print "city:"+str(r[5])
			print "latitude:"+str(r[6])
			print "longitude:"+str(r[7])
			print "zipcode:"+str(r[8])
			print "timezone:"+str(r[9])
			l=(str(r[6]),str(r[7]))
			self.locations_list.append(l)
		return self.locations_list
	
			
		