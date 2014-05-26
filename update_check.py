# -*- coding: utf8 -*-

import subprocess
import time
import inspect

DEBUG_MODE = 0

def checkForUpdate():
	if DEBUG_MODE == 1:
		print "entering {0}".format(inspect.stack()[0][3])

	#create a subprocess that launches apt-check and gathers results
	p = subprocess.Popen('apt-get -s upgrade | grep -Po "^\\d+ (?=mis à jour)"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	#read stderr to a string
	str = p.stdout.read();
	print "tjeriotjeroi {0}".format(str)

	#split it
	updates = int(str)

	#if result is non zero, tweet it
	if updates != 0 or sec_updates != 0:
		#print "Twitting..."
		cur_date = time.strftime("%x")
		cur_time = time.strftime("%X")
		tweet = "{0} - {1} - Your server has {2} updates pending!".format(cur_date, cur_time, updates)
		twitter = subprocess.Popen("/usr/local/bin/twitter -edeadbird.fr@gmail.com set {0}".format(tweet), stderr=subprocess.PIPE, shell=True)
	
	#debug mode
	if DEBUG_MODE == 1:
		print "apt-check returned this: {0}".format(str)
		print "Then I got this: updates={0}".format(updates)
		#check for variable existence
		if 'tweet' in locals():
			print "Tweet = {0}".format(tweet)
			print "Twitter subprocess returned this: {0}".format(twitter.stderr.read())

if __name__ == '__main__':
	checkForUpdate()