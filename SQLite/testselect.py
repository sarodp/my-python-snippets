#!/usr/bin/python
import time
import sqlite3

#01-------------------------------
mydb1 = '/home/pi/myiot/myiot01.db'
cn1 = sqlite3.connect(mydb1)

print "\nSQLite == 1.Test read tables fron python."
print "Database file:", mydb1
print "-----------------------------------"

#1a---sql1
print "\n",time.asctime( time.localtime(time.time()) )
sql1 = 'select * from TSETTING'
cursor1 = cn1.execute(sql1)
tb01 = cursor1.fetchall()
print "\n",time.asctime( time.localtime(time.time()) )

print "\nQuery:",sql1
print  "  no.of rows = %i" % (len(tb01)),
i=0

for xrowi in tb01: 
	i =i+1  
	#print " row(%i).list => %s" % (i,xrowi)
	print "\n row(%i).data => " % (i),
	for xdati in xrowi:
		print " %s, " % (xdati),


#1b---sql2
print "\n",time.asctime( time.localtime(time.time()) )
sql2 = 'select * from TMEASURE'
cursor2 = cn1.execute(sql2)
tb02 = cursor2.fetchall()
print "\n",time.asctime( time.localtime(time.time()) )

print "\n\nQuery:",sql2
print  "  no.of rows = %i" % (len(tb02)),
i=0
for xrowi in tb02: 
	i =i+1  
	#print " row(%i).list => %s" % (i,xrowi)
	print "\n row(%i).data => " % (i),
	for xdati in xrowi:
		print " %s, " % (xdati),



#99---done
cursor1.close
cursor2.close
cn1.close()
