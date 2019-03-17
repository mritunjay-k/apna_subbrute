# apna_subbrute
A very handy tool for finding subdomain takeover vulnerability.

I was just using a subdomain enumeration tool to gather information regarding which of them are vulnerable to takeover. What i found was that the tool was too slow to process. Even on the high speed internet connection it took me about 3-4 hours just to enumerate all and even the result after that were not satisfying. The fast mode on that tool was still experimental, so I didn't wanna use that. 

###### I thought why not develop my own??

I came up with an idea to develop this tool. Steps to use it are as follows:

1. There must a bash file named 'requirements.sh'. Run it as:  ~$ sudo bash requirements.sh 
   (Don't forget to give the 'sudo', otherwise it'll create a mess)
2. Now you're good to go. Run the python file as:  ~$ python3 apna_subbrute.py

## One thing to notice here is that you will need to provide a list of subdomains to it. It will then show you if there is an external host (CNAME) to it, and whether there is an error 404 or not. (I don't know why but this 'error 404' kinda triggers me.)

#### This tool works fine with the output generated by other subdomain enumeration tools like Sublist3r (my favourite).

If you got any problem, email me: mritunjayk.1229@outlook.com     
I'll be happy to help.

Didn't like it? Better not use it. 
Suggest me the better option too (**if you have**)

