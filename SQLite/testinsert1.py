#!/usr/bin/python
import sys
import time
import random
import sqlite3

#0--init
print "\nSQLite3-Python: Test insert into TMEASURE."
print "------------------------------------------------"

#1--mydb1,sqlcmd
mydb1 = '/home/pi/myiot/myiot01.db'
print ">> database file:", mydb1


#2a--xcount 
xcount = input(">> no. of records to insert [1-100000]: ")

#2b--xsqlfmt 
# "insert into TMEASURE (STAG,SVALUE) values ('T1', 25.0)";
xsqlfmt = '''insert into TMEASURE (STAG,SVALUE) values ('%s', %.1f);'''
print ">>"
print ">>" , xsqlfmt

#2c--staglist = get list of STAG
sql1 = '''select distinct STAG from TSETTING'''
cn1 = sqlite3.connect(mydb1)
cur1 = cn1.execute(sql1)
staglist = cur1.fetchall()


#3--loop xsqlcmd
print ">> ... ",
tstart = time.asctime( time.localtime(time.time()) )
try:
	#3a--loop xsqlcmd
	for xi in range(1,xcount):
		#3a1--xsqlcmd
		xtag = '%s' % (random.choice(staglist))
		xval = random.random()*100
		xsqlcmd = xsqlfmt % (xtag,xval)
		#3a2--execute
		cn1.execute(xsqlcmd)
		#3c
		if (xi % 100) == 0 :
			print ".",
			sys.stdout.flush
	#3b--commit
	cn1.commit()
	xmsg = '>> insert OK.'
except:
	#3z--rollback if error
	cn1.rollback()
	xcount = 0
	xmsg = '>> insert ERROR.'

#4--insert done
tdone = time.asctime( time.localtime(time.time()) )
print ">>"
print xmsg
print ">> %i records inserted." % (xcount)
print ">> timestart:", tstart
print ">> timedone: ", tdone

#9a---
print ">> "
xsqlcmd = '''select * from TMEASURE '''
cursor1 = cn1.execute(xsqlcmd)	
tb01 = cursor1.fetchall()
print ">>", xsqlcmd
print ">> total records: %i\n" % (len(tb01))


#99---done
cn1.close()
