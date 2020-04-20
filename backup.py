## this program requires the use of an ssh method, else, a password will have to be passed
## this is helpful for syncing logs and the such from a remote server to github


import schedule
from datetime import date
import os
import time
from time import ctime

duration = 1000 ## enter the duration in seconds here -> backup duration
password = ''

def ssh_backup():
	os.system('git add . && git commit -m "Auto-Backup-Script'+str(ctime())+' " && git push')



##schedule.every(10).minutes.do(ssh_backup)

while True:
	#schedule.run_pending()
	ssh_backup()
	print("keep me running, I'm just sleeping for 1000 seconds now")
	time.sleep(duration)







#def password_backup():
#	os.system('git add . && git commit -m "Auto-')
