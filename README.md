# YapDi - Yet another python Daemon implementation #

## Overview ##

As the name implies YapDi is yet another python daemon implementation. Python 2.x standard library didn't have a daemonizing module. It is one of those rare few modules python standard library lacked that put the phrase "batteries included" to shame. There is [PEP 3143](http://www.python.org/dev/peps/pep-3143/) which introduces a daemonizing package to python 3.x standard library.

Python community is scattered with so many daemon implementations and this is one of them. This module is a modified version of a code originally posted [here](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/). So any compliments should go there first.

## Installation ##

python setup.py install

## Basic Usage ##
    import yapdi

    # Creating a yapdi daemon instance
    daemon = yapdi.Daemon()

    # You can also supply a pid file name at daemon instance creation time
    daemon = yapdi.Daemon(pidfile='/var/run/.myservice.pid')
    
    # Daemonizing an instance; Any code placed under this would get executed in daemon mode
    daemon.daemonize()

    # Stopping a running instance
    daemon.kill()

    # Restarting an instance; If an instance is already running it would be killed and started again, else would just start
    daemon.restart()

    # Checking whether an instance is running
    if daemon.status():
        print('An instance is already running')
    else:
        print('No instance is running')

    # Running a daemonized instance as a different user; any code below these two lines would get executed in daemon mode as user 'user123'
    daemon.set_user('user123')
    daemon.daemonize()

