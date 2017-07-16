import httplib

number = 9857
#This is just the number for the link. E.g bob.com/4/XXXX.mp4 Where XXXX is a number
host = "www.google.com"
#I would give out the link but it would get tooken down.

while number > 1:
	conn = httplib.HTTPConnection(host)
	conn.request("GET", '/' + str(number) + '.mp4')
	#"GET" Was used because it is a download "HEAD" is faster in some cases.
	
	print ("Trying:" + str(number))	
	response = conn.getresponse()
	print response.status
	conn.close()
	if response.status == 200:
		trueurl = "www.google.com + str(number) + ".mp4" + "\n"
		#Puts the link in var trueurl if status == 200 returns True
		file_object = open("links.txt", "a")
		#a appends it so it keeps the previous one w over rights.
		file_object.write(str(trueurl))
		file_object.close()
		#writes to the file the links.

	number = number -1
	#Changes it to a new link.

	
	
	