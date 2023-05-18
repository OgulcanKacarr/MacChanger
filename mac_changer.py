from colorama import Fore, Back, Style
import subprocess as sub
import colorama
import argparse
import random
import re


def create_random_mac():	
	charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	new_mac = ""
	for i in range(12):
		new_mac = new_mac+random.choice(charList)
	return new_mac

def change_mac(interface,new_mac):	
	ifconfig_result = sub.check_output("ifconfig "+interface,shell=True).decode()
	old_mac = re.search("ether(.*?)txqueuelen",ifconfig_result).group(1).strip()

	sub.check_output("ifconfig"+interface+"down",shell=True)
	sub.check_output("ifconfig"+interface+"hw ether"+new_mac,shell=True)
	sub.check_output("ifconfig"+interface+"up",shell=True)

	print("Old Mac -> "+old_mac)
	print("New Mac -> " + new_mac)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--interface", required=True, help="interface")
ap.add_argument("-r", "--random", required=False, help="random mac")
ap.add_argument("-m" "--mac", required=False, help="manuel mac")
args = vars(ap.parse_args())

interface = args["interface"]
make_random_mac = args["random"]
make_manuel_mac = args["mac"]

if(make_manuel_mac != ""):
	new_mac = create_random_mac()
	change_mac(interface,new_mac)
else:
	change_mac(interface,make_manuel_mac)
