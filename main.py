import tkinter
from tkinter import *
import time
import random
import tkinter.messagebox as box

operator = ''
class Swig(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        cont = tkinter.Frame(self)
        tkinter.Tk.wm_title(self, "Swig")

        cont.pack(side="top", fill="both", expand=True)
        cont.grid_rowconfigure(0, weight=1)
        cont.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage, FifthPage):
            frame = F(cont, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, cont1):
        frame = self.frames[cont1]
        frame.tkraise()






class FirstPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        def dialog1():
            username = Entry_Username.get()
            password = Entry_Password.get()
            if (username == 'admin' and password == 'secret'):
                box.showinfo('info', 'Correct Login')
                controller.show_frame(SecondPage)
            else:
                box.showinfo('info', 'Invalid Login')

        Label_Username=Label(self, text= "Username: ")
        Label_Username.pack()

        Entry_Username=Entry(self, bd= 5)
        Entry_Username.pack()

        Label_Password  = Label(self, text='Password: ')
        Label_Password.pack(padx=15, pady=6)

        Entry_Password = Entry(self, bd=5)
        Entry_Password.pack(padx=15, pady=7)

        Button_Login = Button(self, text='Check Login', command= dialog1 )
        Button_Login.pack(side=RIGHT, padx=5)



class SecondPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        v=tkinter.IntVar()
        v.set(1)

        options = [
            ("Burger king"),
            ("Subway"),
            ("Dominos"),
            ("Pizza hut"),
        ]

        def ShowChoice():
            print(v.get())

        tkinter.Label(self, text = "Restaurants", justify = tkinter.CENTER).pack()
        for val, opt in enumerate(options):
            tkinter.Radiobutton(
                self,
                text = opt,
                padx = 20,
                variable = v,
                command = ShowChoice,
                value= val).pack(anchor=tkinter.W)
        btnGoToNext = tkinter.Button(self, text = "Select", command = lambda: controller.show_frame(ThirdPage))
        btnGoToNext.pack()

class ThirdPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self, width=900, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self, width=400, height=700, relief=SUNKEN)
        f2.pack(side=RIGHT)
        # ------------------TIME--------------
        localtime = time.asctime(time.localtime(time.time()))
        # -----------------INFO TOP------------
        lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Menu", fg="black", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(Tops, font=('aria', 20,), text=localtime, fg="black", anchor=W)
        lblinfo.grid(row=1, column=0)

        # ---------------Calculator------------------
        text_Input = StringVar()
        operator = ""

        txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white",
                           justify='right')
        txtdisplay.grid(columnspan=4)

        def btnclick(numbers):
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)

        def clrdisplay():
            global operator
            operator = ""
            text_Input.set("")

        def eqals():
            global operator
            sumup = str(eval(operator))

            text_Input.set(sumup)
            operator = ""

        def Ref():
            x = random.randint(12980, 50876)
            randomRef = str(x)
            rand.set(randomRef)

            cof = float(Fries.get())
            colfries = float(Largefries.get())
            cob = float(Burger.get())
            cofi = float(Filet.get())
            cochee = float(Cheese_burger.get())
            codr = float(Drinks.get())

            costoffries = cof * 25
            costoflargefries = colfries * 40
            costofburger = cob * 35
            costoffilet = cofi * 50
            costofcheeseburger = cochee * 50
            costofdrinks = codr * 35

            costofmeal = "Rs.", str('%.2f' % (
            costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
            PayTax = (
            (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) * 0.33)
            Totalcost = (
            costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)
            Ser_Charge = (
            (costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks) / 99)
            Service = "Rs.", str('%.2f' % Ser_Charge)
            OverAllCost = "Rs.", str(PayTax + Totalcost + Ser_Charge)
            PaidTax = "Rs.", str('%.2f' % PayTax)

            Service_Charge.set(Service)
            cost.set(costofmeal)
            Tax.set(PaidTax)
            Subtotal.set(costofmeal)
            Total.set(OverAllCost)

        # def qexit():
            # root.destroy()

        def reset():
            rand.set("")
            Fries.set("")
            Largefries.set("")
            Burger.set("")
            Filet.set("")
            Subtotal.set("")
            Total.set("")
            Service_Charge.set("")
            Drinks.set("")
            Tax.set("")
            cost.set("")
            Cheese_burger.set("")

        btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="powder blue",
                      command=lambda: btnclick(7))
        btn7.grid(row=2, column=0)

        btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
                      command=lambda: btnclick(8))
        btn8.grid(row=2, column=1)

        btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
                      command=lambda: btnclick(9))
        btn9.grid(row=2, column=2)

        Addition = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+",
                          bg="powder blue", command=lambda: btnclick("+"))
        Addition.grid(row=2, column=3)
        # ---------------------------------------------------------------------------------------------
        btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
                      command=lambda: btnclick(4))
        btn4.grid(row=3, column=0)

        btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
                      command=lambda: btnclick(5))
        btn5.grid(row=3, column=1)

        btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
                      command=lambda: btnclick(6))
        btn6.grid(row=3, column=2)

        Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-",
                              bg="powder blue", command=lambda: btnclick("-"))
        Substraction.grid(row=3, column=3)
        # -----------------------------------------------------------------------------------------------
        btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
                      command=lambda: btnclick(1))
        btn1.grid(row=4, column=0)

        btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
                      command=lambda: btnclick(2))
        btn2.grid(row=4, column=1)

        btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
                      command=lambda: btnclick(3))
        btn3.grid(row=4, column=2)

        multiply = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*",
                          bg="powder blue", command=lambda: btnclick("*"))
        multiply.grid(row=4, column=3)
        # ------------------------------------------------------------------------------------------------
        btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
                      command=lambda: btnclick(0))
        btn0.grid(row=5, column=0)

        btnc = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="powder blue",
                      command=clrdisplay)
        btnc.grid(row=5, column=1)

        btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=",
                          bg="powder blue", command=eqals)
        btnequal.grid(columnspan=4)

        Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="powder blue",
                         command=lambda: btnclick("."))
        Decimal.grid(row=5, column=2)

        Division = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/",
                          bg="powder blue", command=lambda: btnclick("/"))
        Division.grid(row=5, column=3)

        # ---------------------------------------------------------------------------------------
        rand = StringVar()
        Fries = StringVar()
        Largefries = StringVar()
        Burger = StringVar()
        Filet = StringVar()
        Subtotal = StringVar()
        Total = StringVar()
        Service_Charge = StringVar()
        Drinks = StringVar()
        Tax = StringVar()
        cost = StringVar()
        Cheese_burger = StringVar()

        lblreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
        lblreference.grid(row=0, column=0)
        txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                             justify='right')
        txtreference.grid(row=0, column=1)

        lblfries = Label(f1, font=('aria', 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
        lblfries.grid(row=1, column=0)
        txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtfries.grid(row=1, column=1)

        lblLargefries = Label(f1, font=('aria', 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
        lblLargefries.grid(row=2, column=0)
        txtLargefries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4,
                              bg="powder blue", justify='right')
        txtLargefries.grid(row=2, column=1)

        lblburger = Label(f1, font=('aria', 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
        lblburger.grid(row=3, column=0)
        txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtburger.grid(row=3, column=1)

        lblFilet = Label(f1, font=('aria', 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
        lblFilet.grid(row=4, column=0)
        txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtFilet.grid(row=4, column=1)

        lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10,
                                 anchor='w')
        lblCheese_burger.grid(row=5, column=0)
        txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4,
                                 bg="powder blue", justify='right')
        txtCheese_burger.grid(row=5, column=1)

        # --------------------------------------------------------------------------------------
        lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
        lblDrinks.grid(row=0, column=2)
        txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue",
                          justify='right')
        txtDrinks.grid(row=0, column=3)

        lblcost = Label(f1, font=('aria', 16, 'bold'), text="cost", fg="steel blue", bd=10, anchor='w')
        lblcost.grid(row=1, column=2)
        txtcost = Entry(f1, font=('ariel', 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue",
                        justify='right')
        txtcost.grid(row=1, column=3)

        lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="steel blue", bd=10,
                                  anchor='w')
        lblService_Charge.grid(row=2, column=2)
        txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4,
                                  bg="powder blue", justify='right')
        txtService_Charge.grid(row=2, column=3)

        lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
        lblTax.grid(row=3, column=2)
        txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue",
                       justify='right')
        txtTax.grid(row=3, column=3)

        lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
        lblSubtotal.grid(row=4, column=2)
        txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4,
                            bg="powder blue", justify='right')
        txtSubtotal.grid(row=4, column=3)

        lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
        lblTotal.grid(row=5, column=2)
        txtTotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtTotal.grid(row=5, column=3)

        # -----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1, text="---------------------", fg="white")
        lblTotal.grid(row=6, columnspan=3)

        btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="TOTAL",
                          bg="powder blue", command=Ref)
        btnTotal.grid(row=7, column=1)

        btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                          bg="powder blue", command=reset)
        btnreset.grid(row=7, column=2)

        # btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
        #                  bg="powder blue", command=qexit)
        # btnexit.grid(row=7, column=3)

        btnFourthPage = Button(self, text="Next Page", command= lambda: controller.show_frame(FourthPage) )
        btnFourthPage.pack()
        def price():
            roo = Tk()
            roo.geometry("600x220+0+0")
            roo.title("Price List")
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)

            roo.mainloop()

        btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE",
                          bg="powder blue", command=price)
        btnprice.grid(row=7, column=0)

class FourthPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        Tops = Frame(self, bg="white", width=1600, height=50, relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self, width=900, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self, width=400, height=700, relief=SUNKEN)
        f2.pack(side=RIGHT)

        # -----------------INFO TOP------------
        lblinfo = Label(Tops, font=('', 30, 'bold'), text="Customer Details", fg="steel blue", bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)

        def Ref():
            x = random.randint(12980, 50876)
            randomRef = str(x)
            rand.set(randomRef)

            cof = float(Name.get())
            colfries = float(Address.get())
            colri = float(Phoneno.get())

            costofname = cof * 25
            costofaddress = colfries * 40
            costofPhoneno = colri * 40

        def qexit():
            self.destroy()

        def reset():
            rand.set("")
            Name.set("")
            Address.set("")
            Phoneno.set("")

        rand = StringVar()
        Name = StringVar()
        Address = StringVar()
        Phoneno = StringVar()

        lblreference = Label(f1, font=('aria', 16, 'bold'), text="Name.", fg="steel blue", bd=10, anchor='w')
        lblreference.grid(row=0, column=0)
        txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue",
                             justify='right')
        txtreference.grid(row=0, column=1)

        lbladdress = Label(f1, font=('aria', 16, 'bold'), text="Address", fg="steel blue", bd=10, anchor='w')
        lbladdress.grid(row=1, column=0)
        txtaddress = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Name, bd=6, insertwidth=4, bg="powder blue",
                           justify='right')
        txtaddress.grid(row=1, column=1)

        lblfries = Label(f1, font=('aria', 16, 'bold'), text="Phone no", fg="steel blue", bd=10, anchor='w')
        lblfries.grid(row=2, column=0)
        txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Phoneno, bd=6, insertwidth=4, bg="powder blue",
                         justify='right')
        txtfries.grid(row=2, column=1)

        # -----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1, text="---------------------", fg="white")
        lblTotal.grid(row=6, columnspan=3)

        btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET",
                          bg="powder blue", command=reset)
        btnreset.grid(row=7, column=2)

        btnFifthPage =Button(self, text = "Next page", command = lambda : controller.show_frame(FifthPage))
        btnFifthPage.pack()

        btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                         bg="powder blue", command=qexit)
        btnexit.grid(row=7, column=3)

class FifthPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        v = tkinter.IntVar()
        v.set(1)  # initializing the choice, i.e. Python

        languages = [
            ("COD"),
            ("Debit card"),
            ("Credit card"),
            ("Net banking"),

        ]

        def ShowChoice():
            print(v.get())

        tkinter.Label(self,
                 text="""Choose your mode of payment""",
                 justify=tkinter.LEFT,
                 padx=20).pack()

        for val, language in enumerate(languages):
            tkinter.Radiobutton(self,
                           text=language,
                           padx=20,
                           variable=v,
                           command=ShowChoice,
                           value=val).pack(anchor=tkinter.W)

app = Swig()
app.mainloop()