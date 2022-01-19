from tkinter import *

def view_Times_Table():
    number = numberbox.get()
    number = int(number)
    for i in range(1,13):
        result = i*number
        #record = str(i)+"x"+str(number)+"="+str(result)
        #List_Table_box.insert(END,record)
        List_Table_box.insert(END,(i,"x",number,"=",result))
    numberbox.delete(0,END)
    numberbox.focus()

def Clear_info():
    numberbox.delete(0,END)
    List_Table_box.delete(0,END)
    numberbox.focus()

root = Tk()
root.title("Times Table")
root.geometry("400x350")

numberlabel = Label(text = "Enter a number:")
numberlabel.place(x=20,y=40,width=100,height=30)

numberbox = Entry(text = "")
numberbox.place(x=130,y=40,width=140,height=30)

ViewBtn = Button(text = "View Times Table",command=view_Times_Table)
ViewBtn.place(x=280,y=40,width=100,height=30)

List_Table_box = Listbox()
List_Table_box.place(x=130,y=80,width=140,height=200)

ClearBtn = Button(text = "Clear",command=Clear_info)
ClearBtn.place(x=280,y=80,width=100,height=30)

root.mainloop()