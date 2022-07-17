import random
import datetime
from tkinter import *
root=Tk()
root.geometry('1600x700')
root.title('Balaji Hotels')
TOPF=Frame(root,bg="#a21b1b",width=1600,height=50)
TOPF.pack(side=TOP)
BottomF=Frame(root,bg="#ff0854",width=1600,height=50)
BottomF.pack(side=BOTTOM)
F1=Frame(root,bg="red",width=900,height=700)
F1.pack(side=LEFT)
F2=Frame(F1,width=850,height=400)
F2.pack(side=TOP)
F2.pack(padx=15,pady=12)
d=datetime.datetime.now()
F3=Frame(F1,width=850,height=175)
F3.pack(side=BOTTOM)
F3.pack(padx=15,pady=12)
F4=Frame(root,bg="#f9b750",width=600,height=700)
F4.pack(side=RIGHT)
F5=Frame(F4,bg="green",width=600,height=350)
F5.pack(side=TOP)
F5.pack(padx=50,pady=100)

#------------Frame items----------------------------------------------------------------
lblinfo=Label(TOPF,font=('Sans serif',25,'bold'),text="Restaurant Management System",fg="Steelblue",bd=8)
lblinfo.grid(row=0,column=1)
lbltime=Label(TOPF,font=('Sans serif',18,'bold'),text=d,fg="Steelblue",bd=8)
lbltime.grid(row=1,column=1)
#frame variables------------------------------------------------------------------------------

rand=StringVar()
fishmeal=StringVar()
chickendish=StringVar()
chowmein=StringVar()
Pasta=StringVar()
Beefsteak=StringVar()
Porkrib=StringVar()
porkgrill=StringVar()
taco=StringVar()
kim=StringVar()
lob=StringVar()
cr=StringVar()
sh=StringVar()
la=StringVar()
sub_tot=StringVar()
Total=StringVar()
Serv_ch=StringVar()
Cost=StringVar()
Tax=StringVar()
#----------------------defintions for frame contents---------------------------------------------------------------------

def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cofh = float(fishmeal.get())
    coch = float(chickendish.get())
    cocm = float(chowmein.get())
    copa = float(Pasta.get())
    cobee = float(Beefsteak.get())
    copr = float(Porkrib.get())
    copg = float(porkgrill.get())
    cota = float(taco.get())
    coki = float(kim.get())
    colb = float(lob.get())
    cocr = float(cr.get())
    cosh = float(sh.get())
    cola = float(la.get())

    costoffh = cofh * 75
    costofch = coch * 65
    costofcm = cocm * 45
    costofpa = copa * 55
    costofbee = cobee * 50
    costofpr = copr * 60
    costofpg = copg * 70
    costofta = cota * 65
    costofki = coki * 67.50
    costoflb = colb * 100
    costofcr = cocr * 92.50
    costofsh = cosh * 80
    costofla = cola * 150

    costofmeal = (costoffh+costofch+costofcm+costofpa+costofbee+costofpr+costofpg+costofta+costofki+costoflb+costofcr+costofsh+costofla)
    PayTax=((costoffh+costofch+costofcm+costofpa+costofbee+costofpr+costofpg+costofta+costofki+costoflb+costofcr+costofsh+costofla)*0.33)
    Totalcost=(costoffh+costofch+costofcm+costofpa+costofbee+costofpr+costofpg+costofta+costofki+costoflb+costofcr+costofsh+costofla)
    Ser_Charge=((costoffh+costofch+costofcm+costofpa+costofbee+costofpr+costofpg+costofta+costofki+costoflb+costofcr+costofsh+costofla)/99)
    Service=Ser_Charge
    OverAllCost=PayTax + Totalcost + Ser_Charge
    PaidTax=PayTax

    Serv_ch.set(Service)
    Cost.set(costofmeal)
    Tax.set(PaidTax)
    sub_tot.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    fishmeal.set("")
    chickendish.set("")
    chowmein.set("")
    Pasta.set("")
    Beefsteak.set("")
    Porkrib.set("")
    porkgrill.set("")
    taco.set("")
    kim.set("")
    lob.set("")
    cr.set("")
    sh.set("")
    la.set("")
    sub_tot.set("")
    Serv_ch.set("")
    Total.set("")
    Tax.set("")
    Cost.set("")

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Steamed Curried Fish", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Seekh kebab", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="65", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chow Mein Noodles", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="45", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sweet Pasta", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="55", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Beef Steak", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pork rib", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Yucatan-Style Grilled Pork", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mexican beef taco", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="65", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Kimchi Chigae", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="67.50", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lobster Risotto", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Singaporean Chile Crab", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="92.50", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Creamy Presto Shrimp", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Grilled Lamb", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=3)

    roo.mainloop()

#  F2 frame display-------------------------------------------------------------

Label(F2,font=('aria',12,'bold'),text="Order no:",fg="steel blue",bd=8,anchor='w').grid(row=0,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=rand,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=0,column=1)

Label(F2,font=('aria',12,'bold'),text="Steamed Curried Fish",fg="steel blue",bd=8,anchor='w').grid(row=1,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=fishmeal,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=1,column=1)

Label(F2,font=('aria',12,'bold'),text="Chicken Seekh kebab",fg="steel blue",bd=8,anchor='w').grid(row=2,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=chickendish,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=2,column=1)

Label(F2,font=('aria',12,'bold'),text="Chow Mein Noodles",fg="steel blue",bd=8,anchor='w').grid(row=3,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=chowmein,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=3,column=1)

Label(F2,font=('aria',12,'bold'),text=" Sweet Pasta",fg="steel blue",bd=8,anchor='w').grid(row=4,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=Pasta,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=4,column=1)

Label(F2,font=('aria',12,'bold'),text="Beef steak",fg="steel blue",bd=8,anchor='w').grid(row=5,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=Beefsteak,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=5,column=1)

Label(F2,font=('aria',12,'bold'),text="Pork rib",fg="steel blue",bd=8,anchor='w').grid(row=6,column=0)
Entry(F2,font=('aria',12,'bold'),textvariable=Porkrib,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=6,column=1)

#---------------------------------------------------------------------------------
Label(F2,font=('aria',12,'bold'),text="Yucatan-Style Grilled Pork",fg="steel blue",bd=8,anchor='w').grid(row=0,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=porkgrill,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=0,column=3)

Label(F2,font=('aria',12,'bold'),text="Mexican beef taco",fg="steel blue",bd=8,anchor='w').grid(row=1,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=taco,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=1,column=3)

Label(F2,font=('aria',12,'bold'),text="Kimchi Chigae",fg="steel blue",bd=8,anchor='w').grid(row=2,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=kim,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=2,column=3)

Label(F2,font=('aria',12,'bold'),text=" Lobster Risotto",fg="steel blue",bd=8,anchor='w').grid(row=3,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=lob,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=3,column=3)

Label(F2,font=('aria',12,'bold'),text="Singaporean Chile Crab",fg="steel blue",bd=8,anchor='w').grid(row=4,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=cr,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=4,column=3)

Label(F2,font=('aria',12,'bold'),text="Creamy Presto Shrimp",fg="steel blue",bd=8,anchor='w').grid(row=5,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=sh,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=5,column=3)

Label(F2,font=('aria',12,'bold'),text="Grilled Lamb",fg="steel blue",bd=8,anchor='w').grid(row=6,column=2)
Entry(F2,font=('aria',12,'bold'),textvariable=la,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=6,column=3)

# F2 Frame display ends--------------------------------------------------------------------------
# F3 Frame display-------------------------------------------------------------------------------

Label(F3,font=('aria',12,'bold'),text="Cost:",fg="steel blue",bd=8,anchor='w').grid(row=0,column=0)
Entry(F3,font=('aria',12,'bold'),textvariable=Cost,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=0,column=1)

Label(F3,font=('aria',12,'bold'),text="Service charge:",fg="steel blue",bd=8,anchor='w').grid(row=1,column=0)
Entry(F3,font=('aria',12,'bold'),textvariable=Serv_ch,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=1,column=1)

Label(F3,font=('aria',12,'bold'),text="Tax:",fg="steel blue",bd=8,anchor='w').grid(row=2,column=0)
Entry(F3,font=('aria',12,'bold'),textvariable=Tax,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=2,column=1)

Label(F3,font=('aria',12,'bold'),text="Sub Total:",fg="steel blue",bd=8,anchor='w').grid(row=3,column=0)
Entry(F3,font=('aria',12,'bold'),textvariable=sub_tot,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=3,column=1)

Label(F3,font=('aria',12,'bold'),text="Total:",fg="steel blue",bd=8,anchor='w').grid(row=4,column=0)
Entry(F3,font=('aria',12,'bold'),textvariable=Total,bd=6,insertwidth=4,bg="#9fc5e8" ,justify='right').grid(row=4,column=1)

Button(F3,padx=10,pady=5, bd=6 ,fg="black",font=('ariel',15,'bold'),width=8,text="Price",bg="#e6d7ab",command=price).grid(row=5,column=2)
Button(F3,padx=10,pady=5, bd=6 ,fg="black",font=('ariel',15,'bold'),width=8,text="Total",bg="#e6d7ab",command=Ref).grid(row=5,column=4)
Button(F3,padx=10,pady=5, bd=6 ,fg="black",font=('ariel',15,'bold'),width=8,text="Reset",bg="#e6d7ab",command=reset).grid(row=5,column=6)
Button(F3,padx=10,pady=5, bd=6 ,fg="black",font=('ariel',15,'bold'),width=8,text="Exit",bg="#e6d7ab",command=qexit).grid(row=5,column=8)

root.mainloop()
