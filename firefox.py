from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random
RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

username = 'ecstatic_stories' #input('{0}->{1} Enter your Username : '.format(YELLOW,END))
password = 'gameover' #input('{0}->{1} Enter your Password : '.format(YELLOW,END))
url = 'https://instagram.com'
target = input('{0}->{1} Target account : '.format(RED,END))
q = input('{0}->{1} Are you following target account? y/n - '.format(YELLOW,END))
print ('{2} >>{1} Type of message\n{2}  [{1}1{2}]{1} Random\n  {2}[{1}2{2}]{1} Custom'.format(RED, END ,YELLOW))
opt = int(input('   {0}>>{1}'.format(YELLOW,END)))
if opt != 1 :
    message = input('{0}   Type your message : {1}'.format(GREEN,END))
a = int(input('{0}->{1} Number of messages : '.format(YELLOW,END)))

def path():
        global firefox
     
        # starts a new chrome session
        firefox = webdriver.Firefox()

def url_name(url):
  firefox.get(url)
  time.sleep(3)
        
def login(usr, pwd):
    # finds the username box
    username = firefox.find_element_by_name("username")
     
    # sends the entered username
    username.send_keys(usr)
 
    # finds the password box
    password = firefox.find_element_by_name("password")
 
    # sends the entered password
    password.send_keys(pwd)
     
    # press enter after sending password
    password.send_keys(Keys.RETURN)
    time.sleep(4)
     
    # goto target page
    firefox.get('https://instagram.com/'+ target )
    time.sleep(4)
    
    if q == 'y':
        return
    else:
        firefox.find_element_by_class_name('_6VtSN').click()
        time.sleep(3)

def send_message():
    firefox.find_element_by_class_name('sqdOP').click()
    time.sleep(4)
    firefox.find_element_by_class_name("HoLwm").click()
    time.sleep(1)
    if opt==1 :
    	rand()
    else:
    	cust()
    
def rand():
    l = ['you are in danger', 'be careful', 'we\'re anonymous', 'you\'ve messed with the wrong peaple', 'there is no escape']
    for x in range(a):
        mbox = firefox.find_element_by_tag_name('textarea')
        mbox.send_keys(random.choice(l))
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)    
def cust():
    for x in range(a):
        mbox = firefox.find_element_by_tag_name('textarea')
        mbox.send_keys(message)
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)    

print ('{0}>> {1}Initializing firefox driver...'.format(RED,GREEN,END))
path()
time.sleep(1)
url_name(url)
print ('{0}>> {1}Attempting to login...'.format(RED,GREEN,END))
login(username, password)
print ('{0}>> {1}Logged in...'.format(RED,GREEN,END))
print ('{0}>> {1}Opening message box...'.format(RED,GREEN,END))
send_message()
print ('{0}>> {1}Message sent successfully...'.format(RED,GREEN,END))
if q == 'n':
    firefox.get('https://instagram.com/'+ target )
    firefox.find_element_by_class_name('-fzfL').click()
    time.sleep(2)
    firefox.find_element_by_class_name('-Cab_').click()
    time.sleep(2)
    print ('{0}>> {1}Unfollowed...'.format(RED,GREEN,END))
print ('{0}>> {1}Exiting the program...'.format(RED,GREEN,END))
firefox.close()

