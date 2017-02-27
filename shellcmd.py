#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# file: shellcmd.py
#
# execute shell command
#
# An example in `python 2` on how you can run a shell command 
# from within your python program. 
#
#==============================================================

import subprocess

#1===shell command execution 
def shellcmd(xcommand):
    # run command (can be an array (for parameters))
    p = subprocess.Popen(xcommand, shell=True, \
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # capture output and error
    (output, err) = p.communicate()
    # wait for command to end
    # TODO: really long running?
    status = p.wait()

    # decode output from byte string
    if output is not None:
        output = output.decode('utf-8')
    if err is not None:
        err = err.decode('utf-8')
    # return stdout, stderr, status code
    return (output, err, status)


#==============================================================
def test():
    #--input your command
    xcmd = raw_input('>> type your command [Ctrl+C to exit]: ')

    #--$ xcmd
    xrtn = shellcmd(xcmd)

    #show results
    print '==>xcmd: %s' % xcmd
    print '==>output: xrtn[0] >\n%s' % xrtn[0] 
    print '==>error string: xrtn[1] >\n%s' % xrtn[1] 
    print '==>error code: xrtn[2] = %i' % xrtn[2] 


#===Entry-Point
if __name__ == '__main__':
    while True:
		test()
    

