'''
CGI Script aka Common Gateway interface that will respond back to a form setup in HTML

Created on January 2, 2019

@author: M.Brohi

Below is a simple HTML5 input form but its action will send data to cgiResponseScript.py
<html> 
<title> Your Webpage </title>
<body>
<form method=POST action="HTML_CGIpy/cgiResponseScript.py">
    <P><B> Please Enter A String: </B>
    <P><input type= text name=user>
    <P><input type=submit>
    
</form>
</body>
</html>

'''
#! /user/bin/python            # sample directory you would place the script on the server
import cgi
form = cgi.FieldStorage()
print "Content-type: text/html\n"   
print "<title> Reply Page from Server </title>"

if not form.has.key('user'):
    print "<h1> How are you ? </h1>"
else:
    print "<h1> Hello <i> %s </i> ! </h1>" % cgi.escape(form['user'].value)   