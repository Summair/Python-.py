'''
web-based interface for viewing/updating class instances stored in a shelve;
Shelve lives on the server

@author: M.Brohi
'''

import cgi, shelve
from pip._vendor.distlib.locators import Page
from dataclasses import fields
from test.support import record_original_stdout

form = cgi.FieldStorage()

print ("Content-type text/html")

shelvename = 'class-shelve'

fieldnames = ('name', 'age', 'job', 'pay')

#main HTML template of webShelvepy.html

replyhtml = """

<html>
<title> Web input Form </title>
<body>
Forms reply Page
<form method= Post action= "pythonDBcgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch", name=action>
    <input type=submit value='Update', name=action>
</form>
</body>
</html>
"""
    #taking data given from the HMTL form
 
rowhtml='<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,)* 3))
replyhtml= replyhtml.replace('$ROWS$', rowshtml)    

    
def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr, (value))
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields
 
def updateRecord(db, form):
    if not form.has_key('key'):
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db.keys():
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

    db = shelve.open(shelvename)
    action = form.has_key('action') and form['action'].value
    if action == 'Fetch':
        fields = fetchRecord(db, form)
    elif action == 'Update':
        fields == updateRecord(db, form)
    else:
        field = dict.fromkeys(fieldnames, '?')
        fields['keys'] ='Missing or invalid action!'
    db.close()
   
    
    print (replyhtml) % htmlize(fields)
    
          


    
               
 
 
 
     
