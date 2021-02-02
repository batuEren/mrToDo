from tkinter import *
import json

toDoList = []
finishedToDoList = []


def LoadData():
    with open('data.json') as json_file:
        data = json.load(json_file)
        print(data['toDoList'])
        for index in data['toDoList']:
            toDoList.append(index["todo"])
        for index in data['finishedToDoList']:
            finishedToDoList.append(index["todo"])
    updateListbox()
    updateFinishedbox()



pencere = Tk()
pencere.geometry("410x210+15+30")
pencere.overrideredirect(1)
pencere.resizable(width=FALSE, height=FALSE)
pencere.title("mr.todo")
pencere.configure(background='#16266b')
pencere.lift()

#pencere.wm_attributes("-topmost", True)
#pencere.wm_attributes("-disabled", True)
pencere.wm_attributes("-transparentcolor", "#16266b")

#pencere.wm_attributes("-alpha",0.5)

def OnUnmap(event):
    # withdraw the tool window,
    print("lol")


pencere.bind("<Unmap>", OnUnmap)

def updateListbox():
    toDoListbox.delete(0,'end')
    for todo in toDoList:
        toDoListbox.insert("end", todo)
    saveData()

def saveData():
    data = {}
    data["toDoList"] = []
    for number in range(0, len(toDoList)):
        data["toDoList"].append({"todo" : toDoList[number]})

    data["finishedToDoList"] = []
    for number in range(0, len(finishedToDoList)):
        data["finishedToDoList"].append({"todo"  : finishedToDoList[number]})

    with open("data.json", "w") as file:
        json.dump(data, file)

def updateFinishedbox():
    finishedListbox.delete(0,'end')
    for todo in finishedToDoList:
        finishedListbox.insert("end", todo)
    saveData()

def addToDo():
    global toDoList
    todo = entry.get()
    if(todo != ''):
        entry.delete(0, 'end')
        toDoList.append(todo)
        print(todo)
        updateListbox()
    else:
        pass

def removeToDo():
    try:
        del toDoList[toDoListbox.curselection()[0]]
        updateListbox()
    except IndexError:
        print("nothin is selcted at first listbox")
    try:
        del finishedToDoList[finishedListbox.curselection()[0]]
        updateFinishedbox()
    except IndexError:
        print("nothin is selcted at second listbox")

def finishToDo():
    value = (toDoList[toDoListbox.curselection()[0]])
    finishedToDoList.append(value)
    updateFinishedbox()
    del toDoList[toDoListbox.curselection()[0]]
    updateListbox()

    print(value)

entry = Entry(pencere, bg="#12205b", fg="white")
entry.grid(row=4, column=0)

addToDoButton = Button(pencere, text="Add ToDo", command=addToDo, height = 1, width = 12, bg = "#12205b", fg="white")
addToDoButton.grid(row=3, column=0)

removeToDoButton = Button(pencere, text="Remove ToDo", command=removeToDo, height = 1, width = 12, bg = "#12205b", fg="white")
removeToDoButton.grid(row=2, column=0)

finishToDoButton = Button(pencere, text="Finish ToDo", command=finishToDo, height = 1, width = 12, bg = "#12205b", fg="white")
finishToDoButton.grid(row=1, column=0)

toDoListbox = Listbox(pencere, bg="#12205b", fg="white")
toDoListbox.grid(row=1, column=1, rowspan=7)

finishedListbox = Listbox(pencere, bg="#12205b", fg="white")
finishedListbox.grid(row=1, column=2, rowspan=7)

title = Label(pencere, text= "Mr.ToDo", bg='#16266b', fg="white", padx=50, pady=5)
title.grid(row=0, column=1)

quitButton = Button(pencere, text="Quit", command=quit, height = 1, width = 12, bg = "#12205b", fg="white")
quitButton.grid(row=5, column=0)

LoadData()

pencere.mainloop()
