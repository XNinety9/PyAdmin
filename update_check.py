import subprocess
import time



#create a subprocess that launches apt-check and gathers results
p = subprocess.Popen("/usr/lib/update-notifier/apt-check", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#read stderr to a string
str = p.stderr.read();

#split it
updates = int(str.split(";")[0])
sec_updates = int(str.split(";")[1]) 

print "Number of packets that can be updated: {0}".format(updates)
print "Number of security update: {0}".format(sec_updates)

#if result is non zero, tweet it
if updates != 0 or sec_updates != 0:
	print "Twitting..."
	cur_date = time.strftime("%x")
	cur_time = time.strftime("%X")
	tweet = "{0} - {1} - Your server has {2}+{3} updates pending!".format(cur_date, cur_time, updates, sec_updates)
	p = subprocess.Popen("/usr/local/bin/twitter -edeadbird.fr@gmail.com set {0}".format(tweet), stderr=subprocess.PIPE, shell=True)
	out, err = p.communicate()
	print "Twitt sent!"
