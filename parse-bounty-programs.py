import json
import os
import requests
# TO-DO:
# [x] Implement automatic downloading of data.
# []  Implement as module in BH-Framework
# []  Add new bug bounty programs


# Get current directory
curdir=os.getcwd()



def parse_bugcrowd():
	print '########################################################################'
	print '############        PARSING      DATA      FROM             ############'
	print '############                   BUGCROWD                     ############'
	print '########################################################################'
	
	with open(curdir + '/data/bugcrowd_data.json') as json_file:  
	    data = json.load(json_file)
	    
	    # Parse json file and create folders and files for 
	    # bug bounties in-scope & out-of-scope items.
	    for x in data:
		print ''
		print '[+] Creating directory structure for: ' + x['name']
	
		directory = '/root/Documents/Bug-Bounties/BugCrowd/' + x['name']
		tfolder =    '/root/Documents/Bug-Bounties/BugCrowd/' + x['name'] + '/targets/'     
		if not os.path.exists(directory):
			os.mkdir(directory)
			os.mkdir(tfolder)
		bounty_targets = x['targets']
		in_scope = bounty_targets['in_scope']
		out_of_scope = bounty_targets['out_of_scope']	
		print "[i] Finding IN SCOPE targets: "
		print "=================================="
	 	for scope in in_scope:
			print scope['target']
			inscp=directory + "/targets/in-scope.txt"
			if os.path.exists(inscp):
				append_write = 'a'
			else:
				append_write = 'w'
			
			targetfile=open(inscp,append_write)
			targetfile.write(scope['target'].encode("utf-8")+"\n")
			targetfile.close()	
				
	
		print ''
		print ''
	
		print "[i] Finding OUT OF SCOPE targets: "
		print "=================================="	
		for scope in out_of_scope:
			print scope['target']
			outscp=directory + "/targets/out-of-scope.txt"
			if os.path.exists(outscp):
				append_write = 'a'
			else:
				append_write = 'w'
			
			oosfile = open(outscp,append_write)
			oosfile.write(scope['target'].encode("utf-8")+"\n")
			oosfile.close()	
	
			
		print '----------------------------------------------------------------------------'
	

def parse_hackerone():
	print '########################################################################'
	print '############        PARSING      DATA      FROM             ############'
	print '############                  HACKERONE                     ############'
	print '########################################################################'
	
	
	
	with open(curdir + '/data/hackerone_data.json') as json_file:  
	    data = json.load(json_file)
	    
	    # Parse json file and create folders and files for 
	    # bug bounties in-scope & out-of-scope items.
	    for x in data:
		print ''
		print '[+] BOUNTY TARGET: ' + x['name']
	
		directory = '/root/Documents/Bug-Bounties/HackerOne/' + x['name']
		tfolder =    '/root/Documents/Bug-Bounties/HackerOne/' + x['name'] + '/targets/'     
		if not os.path.exists(directory):
			os.mkdir(directory)
			os.mkdir(tfolder)
		bounty_targets = x['targets']
		in_scope = bounty_targets['in_scope']
		out_of_scope = bounty_targets['out_of_scope']	
		print "[i] Finding IN SCOPE targets: "
		print "=================================="
	 	for scope in in_scope:
			print scope['asset_identifier']
			inscp=directory + "/targets/in-scope.txt"
			if os.path.exists(inscp):
				append_write = 'a'
			else:
				append_write = 'w'
			
			targetfile=open(inscp,append_write)
			targetfile.write(scope['asset_identifier'].encode("utf-8")+"\n")
			targetfile.close()	
				
	
		print ''
		print ''
	
		print "[i] Finding OUT OF SCOPE targets: "
		print "=================================="	
		for scope in out_of_scope:
			print scope['asset_identifier']
			outscp=directory + "/targets/out-of-scope.txt"
			if os.path.exists(outscp):
				append_write = 'a'
			else:
				append_write = 'w'
			
			oosfile = open(outscp,append_write)
			oosfile.write(scope['asset_identifier'].encode("utf-8")+"\n")
			oosfile.close()	
	
			
		print '----------------------------------------------------------------------------'
	
def download_data():
	print "[+] DOWNLOADING NEW DATA...."
	# Awesome project by arkadiyt (where the data comes from)
	# src: https://github.com/arkadiyt/bounty-targets-data/
	# https://github.com/arkadiyt/bounty-targets
	h1_data="./data/hackerone_data.json"
	h1_url="https://github.com/arkadiyt/bounty-targets-data/raw/master/data/hackerone_data.json"
	bc_data="./data/bugcrowd_data.json"	
	bc_url="https://github.com/arkadiyt/bounty-targets-data/raw/master/data/bugcrowd_data.json"
	
	# delete files and download new	data every time.
	if os.path.exists(h1_data):
		os.remove(h1_data)
	if os.path.exists(bc_data):
		os.remove(bc_data)
	if os.path.exists("./data/wildcards.txt"):
		os.remove("./data/wildcards.txt")
	wcr= requests.get("https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/wildcards.txt")
	h1r= requests.get(h1_url)
	bcr= requests.get(bc_url)

	with open(h1_data, 'wb') as f:
		f.write(h1r.content)	
	with open(bc_data, 'wb') as f:
		f.write(bcr.content)
	with open("./data/wildcards.txt", 'wb') as f:
		f.write(wcr.content)
	
	print "[+] Done downloading new data."



def print_wildcards():
	with open("./data/wildcards.txt", 'rb') as f:
		print "[+] Printing WILDCARD DOMAINS."
		print "-----------------------------------+"
		print(f.read())
	



def main():
	# can change these as you please.
	# goal of using functions is for xternal use in other scripts ;) 
	# but also as a standalone script too.
	download_data()
	parse_bugcrowd()
	parse_hackerone()
	print_wildcards()

if __name__ == "__main__":
	main()
