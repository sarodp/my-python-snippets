#!/usr/bin/python2
#testselect1.py
#
#writen by: sarodp@yahoo.com
#last update: 19-20-2017
#----------------------------------------------

import time
import sqlite3

#0--init
print "\nSQLite3-Python: Test read tables."
print "--------------------------------------------"

#1--mydb1,sqlcmd
mydb1 = '/home/pi/myiot/myiot01.db'
print ">> database file:", mydb1

xtable = raw_input('>> table name: ')   

xsqlcmd = 'select * from %s' % xtable
print ">> sqlcmd:",xsqlcmd

print ">> ..."

#2--xsqlcmd ==> tb01
timestart = time.asctime(time.localtime(time.time()))
cn1 = sqlite3.connect(mydb1)
cursor1 = cn1.execute(xsqlcmd)
tb01 = cursor1.fetchall()
timedone = time.asctime(time.localtime(time.time()))

print ">> timestart: %s" % (timestart	)
print ">> timedone : %s" % (timedone)
print ">> total records: %i" % (len(tb01)),

#3--print tb01
xret = raw_input('\n\n>> press any key to list data...')   

i=0
for xrowi in tb01: 
	i =i+1  
	#print " row(%i).list => %s" % (i,xrowi)
	print "\n>> #%i =>" % (i),
	for xdati in xrowi:
		print "%s," % (xdati),



#99---done
cursor1.close
cn1.close()
