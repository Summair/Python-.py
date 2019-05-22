'''
Created on April 11, 2017

@author: M.Brohi
'''

# A GUI for viewing/updating class instances stored in a shelve; dependencies on Tkinter, tkmessageBox libraries

#Database application that can be utilized for import and export of values  #



from tkinter import *
from tkMessageBox import *
import shelve
from turtledemo.__main__ import getExampleEntries
from tkinter.constants import LEFT
from idlelib.idle_test.test_replace import showerror

shelvename = 'class-shelve'

fieldnames = ('name', 'age', 'job', 'pay')


def makeWidget():
    global entries
    window = Tk()
    window.title('A Little Text box for input')
    form = Frame(window)
    labels = Frame(form)
    values = Frame(form)
    labels.pack(side=LEFT)
    values.pack(side=RIGHT)
    form.pack()
    entries = {}
    for label in ('key',) + fieldnames:
        Label(labels, text=label).pack()
        ent = Entry(values)
        ent.pack()
        entries[label] = ent
    Button(window, text= "Pull", command=pullRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window

def pullRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title = 'Error', message=' No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))
            
def updateRecord():
    
    key = entries['key'].get()
    if key in db.keys():
        record= db[key]
    else:
        from person import Person
        record= Person(name='?', age='?')
    
    for field in fieldnames:  
        setattr(record, field, eval(entries(entries[field].get()))
    db[key] = record
    
db = shelve.open(shelvename)
window = makeWidget()
window.mainloop()
db.close()                          
        
        
        
        
        
        