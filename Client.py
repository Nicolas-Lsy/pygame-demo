#coding: UTF-8 

from socket import * 


def client():
	#creat a socket 
	c = socket(AF_INET, SOCK_STREAM)
	#connect the server    
	c.connect(('127.0.0.1',5555))
	print("++++++++++++++++++++++++++++")
	print("Connect Succeed")
	print("++++++++++++++++++++++++++++")
	while(1):
		#get infomation 
		text = c.recv(1024)
		print "***********************\n"
		print "Server: ",text 
		print "***********************\n"
		put_text = raw_input("Client: ")
		if put_text == "Bye":
			break 
		c.send(put_text)

	#close 
	c.close() 

if __name__ == "__main__":

	client() 
