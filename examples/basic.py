# !/usr/bin/env python

''' YapDi Example - Demonstrate basic YapDi functionality.
    Author - Kasun Herath <kasunh01@gmail.com>
    USAGE - python basic.py start|stop|restart

    python basic.py start would execute count() in daemon mode 
    if there is no instance already running. 

    count() prints a counting number to syslog. To view output of
    count() execute a follow tail to syslog file. Most probably 
    tail -f /var/log/syslog under linux and tail -f /var/log/messages
    under BSD.

    python basic.py stop would kill any running instance.

    python basic.py restart would kill any running instance; and
    start an instance. '''

import sys
import syslog
import time

import yapdi

COMMAND_START = 'start'
COMMAND_STOP = 'stop'
COMMAND_RESTART = 'restart'

def usage():
    print("USAGE: python %s %s|%s|%s" % (sys.argv[0], COMMAND_START, COMMAND_STOP, COMMAND_RESTART))

# Invalid executions
if len(sys.argv) < 2 or sys.argv[1] not in [COMMAND_START, COMMAND_STOP, COMMAND_RESTART]:
    usage()
    exit()

def count():
    ''' Outputs a counting value to syslog. Sleeps for 1 second between counts '''
    i = 0
    while 1:
        syslog.openlog("yapdi-example.info", 0, syslog.LOG_USER)
        syslog.syslog(syslog.LOG_NOTICE, 'Counting %s' % (i))    
        i += 1
        time.sleep(1)

if sys.argv[1] == COMMAND_START:
    daemon = yapdi.Daemon()

    # Check whether an instance is already running
    if daemon.status():
        print("An instance is already running.")
        exit()
    retcode = daemon.daemonize()

    # Execute if daemonization was successful else exit
    if retcode == yapdi.OPERATION_SUCCESSFUL:
        count()
    else:
        print('Daemonization failed')

elif sys.argv[1] == COMMAND_STOP:
    daemon = yapdi.Daemon()

    # Check whether no instance is running
    if not daemon.status():
        print("No instance running.")
        exit()
    retcode = daemon.kill()
    if retcode == yapdi.OPERATION_FAILED:
        print('Trying to stop running instance failed')

elif sys.argv[1] == COMMAND_RESTART:
    daemon = yapdi.Daemon()
    retcode = daemon.restart()

    # Execute if daemonization was successful else exit
    if retcode == yapdi.OPERATION_SUCCESSFUL:
        count()
    else:
        print('Daemonization failed')
