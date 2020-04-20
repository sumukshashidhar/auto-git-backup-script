## this program requires the use of an ssh method, else, a password will have to be passed



import schedule
from datetime import date
import os
import time
from time import ctime


duration = 10 ## enter the duration in minutes here
password = ''

def ssh_backup():
	os.system('git add . && git commit -m "Auto-Backup-Script'+str(ctime())+' " && git push')



##schedule.every(10).minutes.do(ssh_backup)

while True:
	#schedule.run_pending()
	ssh_backup()
	time.sleep(1000)







#def password_backup():
#	os.system('git add . && git commit -m "Auto-')
