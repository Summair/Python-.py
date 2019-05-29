'''
LAUNCH Python is a program that when run in python enviroment  will launch Python programs on the system you want implementations to start
this script application is set to windows eviroment, a little editing can make it RHEL AWS Debain friendly.


'''

import sys, posixpath, os
from cgitb import text
from test.test_multiprocessing_main_handling import launch_source


pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'

def findPythonExe():
    
    try:
        pypath = sys.executable
    except AttributeError:
        try:    
            pypath = os.environ['PP3E_Python_File']
        except KeyError:
            from Launcher import which, guessLocation 
            pypath = (which(pyfile, trace=False) or 
                      guessLocation(pyfile, trace=False))  
    return pypath

class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self):
        self.announce(self.what)
        self.run(self, text)
        print (text)
    def run(self, cmdline):
        assert 0, 'run must be defined'

class System(LaunchMode):
    def run(self, cmdline):
        pypath = findPythonExe()
        os.system('%s %s' % (pypath, cmdline))
                
        
class Popen(LaunchMode):
    def run(self, cmdline):
        pypath = findPythonExe()
        os.popen(pypath + '' + cmdline)
        
class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            pypath = findPythonExe()
            os.execvp(pypath, [pyfile] + cmdline)
 
class Start(LaunchMode):
    def run(self,cmdline):
        assert sys.platform[:3] == 'win'
        os.startfile(cmdline)
        
class StartArgs(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start ' + cmdline)
        
class Spawn(LaunchMode):
    def run(self, cmdline):
        pypath = findPythonExe()      
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))     
        
class Top_level(LaunchMode):
    def run(self, cmdline):
        assert 0, 'Sorry - mode not yet implemented'
 
 
if sys.platform[:3] == 'win'
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork                                    
                    
class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass
    
def selftest():
    myfile = 'launchmodes.py'
    program = 'Gui/TextEditor/textEditor.py ' + myfile
    input('default mode...') 
    launcher = PortableLauncher('PyEdit', program)
    launcher()
    
    input('system mode...')
    System('PyEdit', program)()
    
    input('popen mode...')
    Popen('PyEdit', program)()
    
    if sys.platform[:3] == 'win'
    
    input('PowerShell start mode...')
    StartArgs('PyEdit ', os.path.normpath(program))()
    
    
    if __name__ == '__main__' : selftest()                  
        
        
        
        
        
                      