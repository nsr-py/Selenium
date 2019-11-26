import time
from getpass import getpass
# getpass.getpass() helps take input without showing it on the terminal as it 
#is typed by the console
ls = []
d = {}
y = 'y'
print("Start entering the required data systematically as asked")
time.sleep(2)
print("REMEMBER! If you want to add more data just click 'y' at the end of each entry" )
time.sleep(2)
print("else click any other key")
time.sleep(2)
with open("file.txt",'w') as file :
	while(y == 'y'):
		username = input("Enter username : ")
		password = input("Enter password : ")
		file.write(username + "\n")
		file.write(password + "\n")
		y = getpass("")
		print()

	
	# To use this file transfer the contents into an array or linked list as below
	# for line in file:
	# 	ls.append(line.strip())
	# d[ls[0]] = ls[1]
