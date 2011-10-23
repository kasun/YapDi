# !/usr/bin/env python
''' Python unix daemon module '''

from signal import SIGTERM
import sys, atexit, os
import inspect

class Daemon:
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def daemonize(self):
        ''' Do the UNIX double-fork magic '''
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit first parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.setsid() 
        os.umask(0)

        # do second fork
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit from second parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1) 

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.get_pidfile(),'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.get_pidfile())

    def get_pidfile(self):
        ''' Return file name equal to the called module '''
        try:
            called_modulepath = inspect.stack()[1][1]
        except IndexError:
            # if run stand alone
            called_modulepath = inspect.stack()[0][1]
        called_module = os.path.split(called_modulepath)[1].split('.')[0]
        return called_module
