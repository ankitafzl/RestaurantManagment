from tkinter import *
from tkinter import messagebox,filedialog,ttk
from tkinter.ttk import Combobox
from datetime import datetime
import pymysql

root=Tk()

def checknum(P):
    if P.isdigit() or P == "":
        return True
    return False

def checkalpha(P):
    if P.isalpha() or P == "":
        return True
    return False

callback = root.register(checknum)
callback1 = root.register(checkalpha)

def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.grid_remove()

def connectdb():
    global conn
    global cursor
    conn = pymysql.connect(host="localhost", user="root", db="example")
    cursor = conn.cursor()

def insert():
    nm=iname.get()
    tp=itype.get()
    rt=irate.get()
    if(nm=="" or tp=="" or rt==""):
        messagebox.showwarning("Insertion...", "Please enter item name,rate and type...")
        return
    que="insert into item values(%s,%s,%s)"
    val = (nm,rt,tp)
    connectdb()
    cursor.execute(que, val)
    conn.commit()
    messagebox.showwarning("Insertion...", "Data inserted successfully...")
    setnull()
    showmenuitem()

def setnull():
    iname.set("")
    itype.set("")
    irate.set("")

def delete():
    nm = iname.get()
    tp = itype.get()
    rt = irate.get()
    if (nm == "" or tp == "" or rt == ""):
        messagebox.showwarning("Deletion...", "Please select item name,rate and type...")
        return
    que = "delete from item where name=%s"
    val = (nm)
    connectdb()
    cursor.execute(que, val)
    conn.commit()
    messagebox.showwarning("Deletion...", "Data deleted successfully...")
    setnull()
    showmenuitem()


def update():
    nm = iname.get()
    tp = itype.get()
    rt = irate.get()
    if (nm == "" or tp == "" or rt == ""):
        messagebox.showwarning("Updation...", "Please select item name,rate and type...")
        return
    que = "update item set name=%s,rate=%s,type=%s where name=%s;"
    val = (nm, rt, tp, itext)
    connectdb()
    cursor.execute(que, val)
    conn.commit()
    messagebox.showwarning("Updation...", "Data updated successfully...")
    setnull()
    showmenuitem()

def check():
    n = nm.get()
    p = pw.get()
    if n=="" or p=="":
        messagebox.showwarning("Login...","Please Enter UserId and Password...")
        return
    que="select userid,password from login where userid=%s and password=%s;"
    val = (n,p)
    connectdb()
    cursor.execute(que, val)
    data=cursor.fetchall()
    for row in data:
        if row[0]==n and row[1]==p:
            newwindow()
            break
    else:
        messagebox.showwarning("Login...","UserId and Password does not exist...")
        nm.set("")
        pw.set("")

def showmenuitem():
    records=menu.get_children()

    for element in records:
        menu.delete(element)

    conn=pymysql.connect(host="localhost",user="root",db="example")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    que="select * from item"
    mycursor.execute(que)
    data=mycursor.fetchall()
    for row in data:
        menu.insert('','end',text=row['name'],values=(row["rate"],row["type"]))
    menu.bind("<Button-1>",showmenu)

def showbillitem():
    records=menu2.get_children()
    for element in records:
        menu2.delete(element)
    conn=pymysql.connect(host="localhost",user="root",db="example")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    que="select * from bill"
    mycursor.execute(que)
    data=mycursor.fetchall()
    for row in data:
        menu2.insert('','end',text=row['dated'],values=(row["customer"],row["phone"],row["item"],row["cost"]))



def showmenu(event):
    item=menu.selection()
    global itext,ivalues
    itext=menu.item(item,"text")
    ivalues=menu.item(item,"values")
    iname.set(itext)
    irate.set(ivalues[0])
    itype.set(ivalues[1])

def getitem():
    connectdb()
    que = "select * from item"
    cursor.execute(que)
    data = cursor.fetchall()
    for row in data:
        l.append(row[0])

def setrate(*a):

    connectdb()
    que = "select rate from item where name=%s"
    val=(item.get())
    global r
    r=0
    cursor.execute(que,val)
    data = cursor.fetchall()
    for row in data:
        for value in row:
            r=value
    rate.set(r)


def setcost(*a):
    q=int(quantity.get())
    global r
    cost.set(int(r)*q)


####################################################################bill#######################

def billdetails():
    remove_all_widgets()
    mainheading()

    global dt,Cname,Cno,item,rate,quantity,cost
    dt = StringVar()
    Cname= StringVar()
    Cno= StringVar()
    item= StringVar()
    rate= StringVar()
    quantity=StringVar()
    cost=StringVar()
    lg = Button(root, text="logout", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=logout).grid(row=2, column=0)
    bk = Button(root, text="back", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=back).grid(row=2, column=3)
    q = Label(root, text=" Bill Details ", pady=10, font=("Comic Sans Ms", 25, "bold", "underline", "italic")).grid(
    row=3, columnspan=5)
    l1 = Label(root, text="Date/Time:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=5,
        column=1)
    e1 = Entry(root, fg="black", width=20,state='disable', font=("Comic Sans Ms", 15, "italic"), textvariable=dt).grid(row=5,column=2)

    dt.set(datetime.now())
    l2 = Label(root, text="Customer Name:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=6,
        column=1)
    e2 = Entry(root, fg="black", width=20, font=("Comic Sans Ms", 15, "italic"), textvariable=Cname)
    e2.configure(validate="key", validatecommand=(callback1, "%P"))
    e2.grid(row=6,column=2)
    l3 = Label(root, text="Contact No:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=7,
        column=1)
    e3 = Entry(root, fg="black", width=20, font=("Comic Sans Ms", 15, "italic"), textvariable=Cno)
    e3.configure(validate="key", validatecommand=(callback, "%P"))
    e3.grid(row=7,column=2)
    l4 = Label(root, text="Select Item:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=8,
        column=1)
    global l
    l = []
    getitem()
    c = Combobox(root, values=l,width=18, font=("Comic Sans Ms", 15, "italic"), height=1,textvariable=item)
    c.set("Select Item")
    c.grid(row=8, column=2)
    item.trace('w',setrate)
    quantity.trace('w',setcost)


    l5 = Label(root, text="Rate:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=9,
        column=1)
    e5 = Entry(root, fg="black", width=20, font=("Comic Sans Ms", 15, "italic"), textvariable=rate)
    e5.configure(validate="key", validatecommand=(callback, "%P"))
    e5.grid(row=9,column=2)
    l6 = Label(root, text="Quanitity:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=10,
        column=1)
    l2 = ["1", "2", "3","4","5"]
    c2 = Combobox(root, values=l2,width=18, font=("Comic Sans Ms", 15, "italic"), height=1,textvariable=quantity)
    c2.set("0")
    c2.grid(row=10, column=2)

    l7 = Label(root, text="Cost:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=11,
        column=1)
    e7 = Entry(root, fg="black", width=20, font=("Comic Sans Ms", 15, "italic"), textvariable=cost)
    e7.configure(validate="key", validatecommand=(callback, "%P"))
    e7.grid(row=11,column=2)

    q = Label(root, text="").grid(row=12, columnspan=5)

    sb = Button(root, text="Show Bills", width=10, fg="white", bg="black", border=4, font=("Comic Sans Ms", 15, "bold"),
            command=showbills).grid(row=13, column=0)
    gb = Button(root, text="Genrate Bill", width=10, fg="white", bg="black", border=4, font=("Comic Sans Ms", 15, "bold"),
            command=genratebill).grid(row=13, column=3)


def genratebill():
    dated=dt.get()
    cst=Cname.get()
    ph=Cno.get()
    i=item.get()
    r=rate.get()
    q=quantity.get()
    c=cost.get()
    if(dated=="" or cst=="" or ph=="" or i=="" or r=="" or q=="" or c==""):
        messagebox.showwarning("Insertion...", "Missing some data...")
        return
    que="insert into bill values(%s,%s,%s,%s,%s,%s,%s)"
    val = (dated,cst,ph,i,r,q,c)
    connectdb()
    cursor.execute(que, val)
    conn.commit()
    messagebox.showwarning("Insertion...", "Data inserted successfully...")

########################################################################3
def showbills():
    remove_all_widgets()
    root.geometry("1050x600+300+50")
    showbillitem()
    l = Label(root, text="STARLIGHT RESTAURANT", bg="black", width=50, fg="black", font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=0,column=0,columnspan=6)
    q = Label(root, text=" Item Details ",pady=10, font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=3, columnspan=5)

    lg = Button(root, text="logout", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=logout).grid(row=2, column=0)
    bk = Button(root, text="back", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=back).grid(row=2, column=4)
    lbl= Label(root, text="").grid(row=4, columnspan=5)
    menu2.grid(row=5, column=0, columnspan=5)
    menu2.heading('#0', text="DATE")
    menu2.heading('#1', text="CUSTOMER")
    menu2.heading('#2', text="PHONE")
    menu2.heading('#3', text="ITEM")
    menu2.heading('#4', text="COST")
    scroll2.grid(row=5,column=5,rowspan=10,sticky=N+S+W)
    q = Label(root, text="").grid(row=6, columnspan=5)

    pb = Button(root, text="Print Bill", width=8, fg="white", bg="black", border=4, font=("Comic Sans Ms", 15, "bold"),
            command=printbill).grid(row=7, column=0)



def printbill():
    item = menu2.selection()
    itext = menu2.item(item, "text")
    f = filedialog.asksaveasfile(mode='w', defaultextension="*.txt")
    conn = pymysql.connect(host="localhost", user="root", db="example")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    que = "select * from bill"
    mycursor.execute(que)
    data = mycursor.fetchall()
    for row in data:
        if row["dated"]==itext:
          s="\n******************************************************************************************\n"+"\nDate         = "+row["dated"]+"\nCustomerName = "+row["customer"]+"\nPhone no     = "+row["phone"]+"\nItemName     = "+row["item"]+"\nRate         = "+row["rate"]+"\nQuantity     = "+row["quantity"]+"\nTotalCost    = "+row["cost"]+"\n******************************************************************************************"+"\nThank You...."
          f.write(s)
    f.close()


############################################################item#################
def itemdetails():
    remove_all_widgets()
    mainheading()
    global iname, itype, irate
    iname = StringVar()
    itype = StringVar()
    irate = StringVar()
    q = Label(root, text=" Item Details ",pady=10, font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=3, columnspan=5)

    lg = Button(root, text="logout", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=logout).grid(row=2, column=0)
    bk = Button(root, text="back", width=5, fg="white", bg="black", border=2, font=("Comic Sans Ms", 10, "bold"),
                command=back).grid(row=2, column=4)
    lbl= Label(root, text="").grid(row=4, columnspan=5)

    l1 = Label(root, text="Item name:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(row=5,
                                                                                                         column=1)
    e1 = Entry(root, fg="black", width=15, font=("Comic Sans Ms", 15, "italic"), textvariable=iname)
    e1.configure(validate="key", validatecommand=(callback1, "%P"))
    e1.grid(row=5, column=2)
    b1 = Button(root, text="insert", width=10, fg="white", bg="black", border=5, font=("Comic Sans Ms", 10, "bold"),
                command=insert).grid(row=5, column=3)

    q = Label(root, text="").grid(row=6, columnspan=5)

    l2 = Label(root, text="Item type:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(row=7,
                                                                                                                  column=1)
    e2 = Entry(root, fg="black", width=15, font=("Comic Sans Ms", 15, "italic"), textvariable=itype)
    e2.configure(validate="key", validatecommand=(callback1, "%P"))
    e2.grid(row=7, column=2)
    b2 = Button(root, text="delete", width=10, fg="white", bg="black", border=5, font=("Comic Sans Ms", 10, "bold"),
                command=delete).grid(row=7, column=3)

    q = Label(root, text="").grid(row=8, columnspan=5)

    l3 = Label(root, text="Item rate:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(
        row=9,
        column=1)
    e3 = Entry(root, fg="black", width=15, font=("Comic Sans Ms", 15, "italic"), textvariable=irate)
    e3.configure(validate="key", validatecommand=(callback, "%P"))
    e3.grid(row=9, column=2)
    b3 = Button(root, text="update", width=10, fg="white", bg="black", border=5, font=("Comic Sans Ms", 10, "bold"),
                command=update).grid(row=9, column=3)

    q = Label(root, text="").grid(row=10, columnspan=5)
    menu.grid(row=11,column=1,columnspan=3)
    menu.heading('#0',text="Item Name")
    menu.heading('#1',text="Rate")
    menu.heading('#2',text="Type")

    scroll.grid(row=11,column=4,rowspan=5,sticky=N+S+W)
    showmenuitem()


def back():
    root.geometry("700x600+500+50")
    newwindow()



def newwindow():
    remove_all_widgets()
    mainheading()

    q = Label(root, text=" Operations ",pady=30, font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=2, columnspan=5)

    b1=Button(text="Item Details", width=15, fg="white",bg="black",border=5, font=("Comic Sans Ms", 15, "bold"), command=itemdetails).grid(row=3,column=2)
    q = Label(root, text="").grid(row=4, columnspan=5)
    b2=Button(text="Bill Details", width=15, fg="white",bg="black",border=5, font=("Comic Sans Ms", 15, "bold"), command=billdetails).grid(row=5,column=2)
    q = Label(root, text="").grid(row=6, columnspan=5)
    b3=Button(text="Logout", width=15, fg="white",bg="black",border=5, font=("Comic Sans Ms", 15, "bold"), command=logout).grid(row=7,column=2)



def mainheading():
    l = Label(root, text="STARLIGHT RESTAURANT", bg="black", width=35, fg="white", font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=0,column=0,columnspan=6)

def loginwindow():

    mainheading()
    q = Label(root, text=" Login ",pady=30, font=("Comic Sans Ms", 25,"bold","underline","italic")).grid(row=1,columnspan=5)

    l1 = Label(root, text="Userid:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(row=2,column=2)
    global nm,pw
    nm = StringVar()
    pw = StringVar()
    e1 = Entry(root, fg="black", width=25, font=("Comic Sans Ms", 15, "italic"), textvariable=nm).grid(row=2,column=3)

    q = Label(root, text="").grid(row=3, columnspan=5)
    l2 = Label(root, text="Password:", bg="black", width=15, fg="white", font=("Comic Sans Ms", 15, "bold")).grid(row=4,
                                                                                                                column=2)
    e2 = Entry(root, bg="white", show="*",fg="black", width=25, font=("Comic Sans Ms", 15, "italic"), textvariable=pw).grid(
        row=4, column=3)
    q = Label(root, text="").grid(row=5, columnspan=5)

    b1 = Button(root, text="Login", width=15, fg="white",bg="black",border=5, font=("Comic Sans Ms", 15, "bold"), command=check).grid(row=6,column=3)

def logout():
    remove_all_widgets()
    loginwindow()






root.geometry("700x600+500+50")
menu=ttk.Treeview(height=5,columns=('Item Name''Rate','Type'))
menu2=ttk.Treeview(height=10,columns=('date''Customer','Phone','item','cost'))

scroll = Scrollbar(root)
scroll.config(command=menu.yview)
scroll2 = Scrollbar(root)
scroll2.config(command=menu2.yview)
loginwindow()

mainloop()
