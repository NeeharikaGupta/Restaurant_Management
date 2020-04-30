from Tkinter import*
import random
import time;

root=Tk()
root.geometry("1600x800+0+0")
root.title("Menu")
text_Input=StringVar()
operator=""
Tops= Frame(root,width=1600, height=50,bg="black",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800, height=700,bg="pink",relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300, height=700,bg="pink",relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Comic Sans MS',50,'bold','underline'),text="Menu",fg="black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)


def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""





txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable= input ,bd=30,insertwidth=4,bg="black",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="7",bg="black",command=lambda:btnClick(7)).grid(row=2,column=0)


btn8=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="8",bg="black",command=lambda:btnClick(8)).grid(row=2,column=1)


btn9=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="9",bg="black",command=lambda:btnClick(9)).grid(row=2,column=2)


Addition=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="+",bg="black",command=lambda:btnClick('+')).grid(row=2,column=3)
#------------------------------------------------------#
btn4=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="4",bg="black",command=lambda:btnClick(4)).grid(row=3,column=0)


btn5=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="5",bg="black",command=lambda:btnClick(5)).grid(row=3,column=1)


btn6=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="6",bg="black",command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="-",bg="black",command=lambda:btnClick('-')).grid(row=3,column=3)

#-----------------------------------------------------#
btn1=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="1",bg="black",command=lambda:btnClick(1)).grid(row=4,column=0)


btn2=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="2",bg="black",command=lambda:btnClick(2)).grid(row=4,column=1)


btn3=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="3",bg="black",command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="*",bg="black",command=lambda:btnClick('*')).grid(row=4,column=3)

#-----------------------------------------------------#
btn0=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="0",bg="black",command=lambda:btnClick(0)).grid(row=5,column=0)


btnClear=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="C",bg="black",command=btnClearDisplay).grid(row=5,column=1)


btnEquals=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="=",bg="black").grid(row=5,column=2)

Division=Button(f2, padx=16,pady=16,bd=8, fg='white',font=('arial',20,'bold'),text="/",bg="black",command=lambda:btnClick('/')).grid(row=5,column=3)

#----------------------------------------------------#

A=StringVar()
lblA=Label(f1,font=("arial",16,"bold"),text="A:",bd=16,anchor="w")
lblA.grid(row=0,column=1)
lblA=Label(f1,font=("arial",16,"bold"),text="Rs 50",bd=16,anchor="w")
lblA.grid(row=0,column=2)

B=StringVar()
lblB=Label(f1,font=("arial",16,"bold"),text="B:",bd=16,anchor="w")
lblB.grid(row=1,column=1)
lblB=Label(f1,font=("arial",16,"bold"),text="Rs 150",bd=16,anchor="w")
lblB.grid(row=1,column=2)

C=StringVar()
lblC=Label(f1,font=("arial",16,"bold"),text="C:",bd=16,anchor="w")
lblC.grid(row=2,column=1)
lblC=Label(f1,font=("arial",16,"bold"),text="Rs 100",bd=16,anchor="w")
lblC.grid(row=2,column=2)

D=StringVar()
lblD=Label(f1,font=("arial",16,"bold"),text="D:",bd=16,anchor="w")
lblD.grid(row=3,column=1)
lblD=Label(f1,font=("arial",16,"bold"),text="Rs 50",bd=16,anchor="w")
lblD.grid(row=3,column=2)

E=StringVar()
lblE=Label(f1,font=("arial",16,"bold"),text="E:",bd=16,anchor="w")
lblE.grid(row=4,column=1)
lblE=Label(f1,font=("arial",16,"bold"),text="Rs 50",bd=16,anchor="w")
lblE.grid(row=4,column=2)

F=StringVar()
lblF=Label(f1,font=("arial",16,"bold"),text="F:",bd=16,anchor="w")
lblF.grid(row=5,column=1)
lblF=Label(f1,font=("arial",16,"bold"),text="Rs 200",bd=16,anchor="w")
lblF.grid(row=5,column=2)



root.mainloop()
