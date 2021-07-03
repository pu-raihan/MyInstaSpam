
from __future__ import print_function
from platform import python_version
from sys import exit
from time import sleep
from os import path
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror
from os import system

RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'
def gchrome():
	system('python3 chrome.py')
def firefox():
	system('python3 firefox.py')
def Runner():
	print ('\n{2}Choose your browser: \n\n{2}[{3}1{2}]{3} Google Chrome\n{2}[{3}2{2}]{3} Mozilla Firefox{1}'.format(RED, END ,YELLOW,GREEN))
	opt = input('\n{1}>{0}>{1}> '.format(END,YELLOW))
	if opt == '1':
		gchrome()
		Runner()
	elif opt == '2':
		firefox()
		Runner()
	else:
		print ('{0}[{1}!{0}]{1} Invalid Option.\nExiting in few seconds...'.format(RED, END))
		exit()

Runner()
        
