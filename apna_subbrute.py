import dns.resolver
import requests

print("""	
			     _                        ____        _           _                _       
			    / \   _ __  _ __   __ _  / ___| _   _| |__       | |__  _ __ _   _| |_ ___ 
			   / _ \ | '_ \| '_ \ / _` | \___ \| | | | '_ \ _____| '_ \| '__| | | | __/ _ /
			  / ___ \| |_) | | | | (_| |  ___) | |_| | |_) |_____| |_) | |  | |_| | ||  __/
			 /_/   \_\ .__/|_| |_|\__,_| |____/ \__,_|_.__/      |_.__/|_|   \__,_|\__\___|
			         |_|                                                                   

""")

try:
	read_file = open(input("Enter path of the file containing subdomains: "),'r')    

	for host in read_file:
		try:
			domain = host.rstrip("\n")
			answers = dns.resolver.query(domain, 'CNAME')
			try:
				for rdata in answers:
					page = requests.get('http://'+ domain)
					print ('Looks like the domain: ', answers.qname ,'has a CNAME: ', rdata.target, 'Status Code: ', page.status_code)
			except:
				for rdata in answers:
					print ('Looks like the domain: ', answers.qname ,'has a CNAME: ', rdata.target, 'Status Code: Not found')
		except:
			print("No CNAME found for the domain: "+ domain)

except:
	print('File not found')





