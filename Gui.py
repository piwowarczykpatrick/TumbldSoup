from tkinter import *
import tkinter.filedialog
import Main

root = Tk()
root.title('TumbldSoup')

notes = 0
loop = BooleanVar()
hours = None
run = False
stop = False
tagsList = []
useGui = False

if useGui:
    def runEvent(event):
        Main.CycleMode = False
        Main.tagsToSearch = tagsText.get().split(',')
        Main.run = True
        Main.avgNotes = int(notesText.get())
        Main.CycleMode = loop.get()
        if hoursText.get() is not "" and loop.get() is False:
            print('ERROR: Loop interval was given, but Loop Mode was disabled.')
            return
        if hoursText.get() is '':
            Main.hourInterval = 0
        else:
            Main.hourInterval = int(hoursText.get())
        Main.runScript()



def stopEvent(event):
    Main.CycleMode = False
    Main.run = False
    print('Ending execution after current loop')


#title = Label(root,text="TmbldSoup", width="16", height="3")
tagsLabel = Label (root, text="Tags To Search: ")
tagsText = Entry(root,text = 'Ex: 240sx,326power,drift')
notesLabel = Label (root, text="Minimum Number of Notes: ",)
notesText = Entry(root)
loopBox = Checkbutton(root, text="Loop Mode?", variable = loop,offvalue = False, onvalue = True)
hourLabel = Label(root, text="Loop Interval (In Hours): ")
hoursText = Entry(root)
dirLabel = Label (root, text="Media Directory: ")
#dirSelect = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
run = Button (root, text="Run")
stop = Button (root, text="Stop")

run.bind("<Button-1>",runEvent)
stop.bind("<Button-1>", stopEvent)

#title.grid(row=0,columnspan=2,sticky=N)
tagsLabel.grid(row=0)
tagsText.grid(row=1)
notesLabel.grid (row=2, column = 0)
notesText.grid (row=3, column=0)
loopBox.grid(row=4,columnspan=2)
hourLabel.grid (row=5,column=0)
hoursText.grid (row=6, column = 0)
dirLabel.grid (row=7, column = 0)
run.grid(row=8)
stop.grid(row = 9)


root.mainloop()