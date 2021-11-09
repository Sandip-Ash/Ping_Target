#Program to PING a target system using normal python commands
#It can run in any python IDLE
import os

ping = input("Number of pings= ") #Stores the number of ping values

IP = input("IP address= ") #Stores the IP address


#os.system('ping -c number_of_pings Target_IP')
os.system('ping -c '+ping+' '+IP)
