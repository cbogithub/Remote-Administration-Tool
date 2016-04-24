#1/usr/bin/python 

def incomingFile(data, socketHolder):
	print data
	nextData = socketHolder.recv(1024)
	while nextData:
		if nextData == "FILEDONE": 
			break
		else:
			with open("client_dictionary.txt", 'w') as file:
				file.write(nextData)
			nextData = socketHolder.recv(1024)