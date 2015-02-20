# -*- coding: utf8 -*-

import subprocess
import time
import inspect

def checkIfApacheIsRunning():
	twitter = subprocess.Popen("service apache2 status", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	#woops, lost connection to mothership!
	if "is running" not in twitter.stdout.read():
		cur_date = time.strftime("%x")
		cur_time = time.strftime("%X")
		tweet = "{0} - {1} - Apache is not running!".format(cur_date, cur_time)
		twitter = subprocess.Popen("/usr/local/bin/twitter -eyouremail@domain.com set {0}".format(tweet), stderr=subprocess.PIPE, shell=True)


if __name__ == '__main__':
	checkIfApacheIsRunning()
