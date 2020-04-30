from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Payment System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( '' ,30, 'bold' ),text="Payment System",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Name.get())
    colfries= float(Address.get())
    colri = float(Phoneno.get())


    costofname = cof*25
    costofaddress = colfries*40
    costofPhoneno = colri * 40

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Name.set("")
    Address.set("")
    Phoneno.set("")

rand = StringVar()
Name = StringVar()
Address = StringVar()
Phoneno=StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Name.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lbladdress = Label(f1, font=( 'aria' ,16, 'bold' ),text="Address",fg="steel blue",bd=10,anchor='w')
lbladdress.grid(row=1,column=0)
txtaddress = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Name , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtaddress.grid(row=1,column=1)



lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Phone no",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Phoneno, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=2,column=1)






#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)


btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)

root.mainloop()



