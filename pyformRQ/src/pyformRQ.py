#!/usr/bin/python

#runs on the server, reads form input, prints  HTML

import cgi, sys
form = cgi.FieldStorage()
print "Content-type: text/html"

html= """

<Title> pyformRQ.py </Title>
<h1> Hello - Greetings - Salam! - Peace <h2>
<hr>
<h4> so lets seee here, your form data gave me some information <h4>
<h4> first input field returns %(name)s</h4>
<h4> second input field returns %(input2)s - please verify</h4>
<h4> third input field returns %(option)s - please verify</h4>
<h4> fourth input field returns %(language)s - please verify</h4>
<h4> You also said: </h4>
<p>%(comment)s </p>

<hr> """

data ={}

for field in ('name', 'input2', 'option','language','comment'):
    if not form.has_key(field):
        data[field] = '(unknown)'
    
    else:
        if type(form[field]) !=list:
            data[field] = form[field].value

        else:
            values = [x.value for x in form[field]]
            data[field] = 'and'.join(values)

print html % data