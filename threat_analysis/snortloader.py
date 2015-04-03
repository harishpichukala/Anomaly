import os
class snortloader:
	'''loads the snort to scan pcap file with predefined signatures'''
	def __init__(self,pcapfile):
		self.pcap=pcapfile
		self.log="log\\alert.ids"
		self.clear_alerts()
	def scanner(self):
			self.query()
			os.system(self.query)
			f=open(self.log)
			content=f.read()
			f.close()
			alerts=content.split("\n\n")
			self.alerts_count=len(alerts)
			alert_dict={}
			count=0
			for alert in alerts:
				lines=[]
				for line in alert.split("\n"):
						lines.append(line)
				alert_dict[count]=lines
				count=count+1
			#print alert_dict
			out=''
			try:
				for i in range(0,len(alert_dict)):
						out+="%s-%s \n"%(alert_dict[i][0],alert_dict[i][2])
			except IndexError:
					pass
			return out							
	def query(self):
		'''generates query for the snort loader'''
		self.rules="myrules.rules"
		self.command="snort"
		self.query="%s  -r %s  -c  %s" %(self.command,self.pcap,self.rules)
	def clear_alerts(self):
		'''clears the alerts file'''
		f=open(self.log,'w')
		f.close()
		
	
	