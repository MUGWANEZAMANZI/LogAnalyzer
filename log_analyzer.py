#Student names: MUGWANEZA MANZI Audace
#Student code: s39
#Class code: RW-University-II
#Lecturer's name : Dominique HARELIMANA
#1. Log Parse auth.log: Extract command usage, Displaying timestamp, executing users and executed commands
def command_usage():
	try:
		with open('/var/log/auth.log') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User","\t"*3, "+ Command used")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'guest' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t guest || \t \t {l[2]}')
				elif 'unknown' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t unknown || \t \t {l[2]}')
				elif 'anonymous' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t anonymous || \t \t {l[2]}')
				else :
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t kali || \t \t {l[2]}')
			print("="*140)
		file1.close()
	except:
		print("Failed loading a file!")
command_usage()
#2. Log Parse auth.log: Monitor user authenthication changes
#2.1 Added users
def added_user():
	try:
		with open('/var/log/auth.log') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User","\t"*3, "+ Added user")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'group added' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t guest || \t \t Hello')
				elif 'COMMAND=/usr/sbin/adduser' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t kali || \t \t {l[-1]}')
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
added_user()
#2.2 Displaying deleted users
def deleted_user():
	try:
		with open('/var/log/auth.log') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User","\t"*3, "+ Deleted user")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'COMMAND=/usr/sbin/userdel' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t kali || \t \t {l[-1]}')
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
deleted_user()
#2.3 Display changing passwords for users
def password_ch():
	try:
		with open('/var/log/auth.log') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User","\t"*3, "+ Password changed")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'pam_unix(passwd:chauthtok):' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t kali || \t \t {l[-1]}')
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
password_ch()
#2.4 When user have used su command
def su_cmd():
	try:
		with open('/var/log/auth.log') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User","\t"*3, "+ Used command")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'su:' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t {l[10]} || \t \t {l[2]}')
					#print(l)
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
su_cmd()
#2.5 Display when user have used sudo command
def sudo_cmd():
	try:
		with open('/var/log/auth.log', 'r') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ User Privelidges","\t"*3, "+ Used command")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if 'sudo:' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t {l[8]} || \t \t {l[2]}')
					#print(l)
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
sudo_cmd()
#2.6 Alert if sudo fails 
def alert_sudo_cmd_fail():
	try:
		with open('/var/log/auth.log', 'r') as file1:
			lines = file1.readlines()
			print("="*140)
			print("+ Timestamp", "\t"*5,"+ Host","\t"*3,"+ Message","\t"*3, "+ Used command")
			print("="*140)
			for line in lines:
				l = line.split(' ')
				if l[2] == 'sudo:' and l[5] == 'failure;' in l:
					print(f'|| {l[0]} \t ||\t {l[1]} \t \t \t|| \t ALERT || \t \t {l[2]}')
			print("="*140)
			file1.close()
	except:
		print("Failed to load file!")
alert_sudo_cmd_fail()
#End of pthr progran.


				

