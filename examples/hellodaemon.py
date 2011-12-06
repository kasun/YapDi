# !/usr/bin/env python

''' YapDi Most basic Example - Prints a 'Hello Daemon' in daemon mode. This is to just to demonstrate how to run a statement(s) in daemon mode. 
    The output will not be visible.

    Author - Kasun Herath <kasunh01@gmail.com>
    USAGE - python hellodaemon.py '''

import yapdi

daemon = yapdi.Daemon()
retcode = daemon.daemonize()

# This would run in daemon mode; output is not visible
if retcode == yapdi.OPERATION_SUCCESSFUL:
    print('Hello Daemon')

