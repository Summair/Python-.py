'''
Server script that will bring your HTTP implementation in Python
serves files/scripts from current working dir;
Pyton scripts must be stored in  
webdir\cgi-bin or webdir\htbin



@ M.Brohi 5.20.2018
'''
webdir = ''  #insert your web directory here
port = 80

import os, sys

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler


if sys.platform[:3] == 'win':
    
    #if it is a windows server
    
    CGIHTTPRequestHandler.have_popen2 = False
    CGIHTTPRequestHandler.have_popen3 = False
    
os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer( srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()

  
    