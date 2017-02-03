#coding: UTF-8 

from socket import * 

def server():
	#creat a socket 
	s = socket(AF_INET, SOCK_STREAM)

	#bind 
	s.bind(('',5555))

	#listen 
	s.listen(3) 

	#get info from guest  it is a socket named sock
	sock, addr = s.accept()
	print "+++++++++++++++++++++++++++++++++"
	print "There is a friend frmo IP:",addr 
	print "+++++++++++++++++++++++++++++++++"
	#new socket start work 
	#we can do something by it , and friend can get 
	while(1):
		send_text = raw_input("YOU: ")
		sock.send(send_text)
		
		# get some infomation from your friend 
		get_text = sock.recv(1024)
		print "--------------------------\n"
		print "Friend: ",get_text
		print "--------------------------\n"
		if get_text == "Bye":
			break
	#close both of two socket 's' and 'sock'
	s.close()
	sock.close()

if __name__ == '__main__':

	server() 






