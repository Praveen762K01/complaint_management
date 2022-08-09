from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
class complaint:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS complaint(
           pid INTEGER Primary Key,
           name TEXT ,
           mail TEXT ,
           date INTEGER ,
           gender TEXT ,
           complaint_ TEXT                     
           )
           """)
        self.con.commit()
    def insert(self,name,mail,date,gender,complaint_):
        self.cur.execute("INSERT INTO complaint VALUES(NULL,?,?,?,?,?)",(name,mail,date,gender,complaint_))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * from complaint")
        rows = self.cur.fetchall()
        return rows
        #self.con.commit()
    def update(self,name,mail,date,gender,complaint_):
        self.cur.execute("UPDATE VALUES IN complaint Name=?,Mail=?,Date=?,Gender=?,Complaint=? where id=?",
                         (name,mail,date,gender,complaint_,id))
        self.con.commit()

    def remove(self,id):
        self.cur.execute("delete from complaint where id=?",(id,))
        self.con.commit()
variable = complaint("sqldatabase.db")  
names = StringVar
mails = StringVar
dates = StringVar
genders = StringVar
complaints = StringVar


def addData():
    if txtname.get()=="" or txtmail.get()=="" or txtdate.get()=="" or txtgender.get()=="" or txtcomplaint.get()=="":
        messagebox.showinfo("Message","Please fill all required fields")
    else:
        variable.insert(txtname.get(),txtmail.get(), txtdate.get(),txtgender.get(), txtcomplaint.get())
        messagebox.showinfo("Message",("Your complaint is registered successfully\nReference number:",id(complaint)))
def getData():
    tv = ttk.Treeview()
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    txtname.set(row[1])
    txtmail.set(row[2])
    txtdate.set(row[3])
    txtgender.set(row[4])
    txtcomplaint.delete(1.0, END)
    txtcomplaint.insert(END, row[5])

def admin():
    adminpage=Tk()
    adminpage.title("Admin Login")
    adminpage.geometry("450x200")
    ets1=StringVar
    ets2=IntVar
    def login():
        if et1.get() =="" or et2.get()=="":
            messagebox.showinfo("Message","Please enter all fields")
        elif et1.get() == "praveen" or et2.get() == 1234567890:
            messagebox.showinfo("Messagebox","Logged in successfully")
            finalwindow=Tk()
            finalwindow.title("Complaints")
            finalwindow.geometry("1500x800")
            finalwindow.config(bg="#b2bec3")
            def showinfo():
                frame = Frame(finalwindow,bg="#ecf0f1")
                frame.place(x=0,y=0,height=800,width=1500)
                style = ttk.Style()
                style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
                style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
                tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5,6), style="mystyle.Treeview")
                tv.heading ("1",text="id")
                tv.column ("1",width = 2)
                tv.heading("2",text="name")
                tv.column("2",width=7)
                tv.heading("3",text="mail")
                tv.column("3",width=13)
                tv.heading("4",text="date")
                tv.column("4",width=5)
                tv.heading("5",text="gender")
                tv.column("5",width=5)
                tv.heading("6",text="complaint")
                tv.column("6",width=20)

                tv['show']='headings'
                tv.bind("<ButtonRelease-1>",getData)
                tv.pack(fill=X)
                #tv['columns']=('pid', 'name', 'mail' , 'date' , 'gender' , 'complaint_')
                tv.delete(*tv.get_children())
                #cur = variable.cursor()
                #cur.execute("SELECT * FROM complaint")
                #result=variable.fetchall()
                for row in variable.fetch():
                    tv.insert("", END, values=row)
                    #tv.insert( 'end', '#{}'.format(row['pid']), text=row['pid'])
            #r = login(self,db)
            showinfo()
            finalwindow.mainloop()
        else:
            messagebox.showinfo("Message","Wrong username or password")
    lbl = Label(adminpage,text = "Login to see complaints",font=("times",20,"bold"),pady = 5)
    lbl.pack()
    lbl1 = Label(adminpage,text = "User id",font = ("times",20,"bold"))
    lbl1.place(relx=0.05,rely = 0.25)
    lbl2 = Label(adminpage,text = "Password",font=("times",20,"bold"))
    lbl2.place(relx=0.05,rely= 0.50)
    et1 = Entry(adminpage,font=("times",20,"bold"),bg="#b2bec3",textvariable=ets1,show = '@')
    et1.place(relx=0.35,rely=0.25)
    et2 = Entry(adminpage,font = ("times",20,"bold"),bg="#b2bec3",textvariable=ets2,show = '*')
    et2.place(relx=0.35,rely=0.50)
    btnlogin = Button(adminpage,text = "Login",font=("times",20,"bold"),bg = "#2d3436",fg="#f5f6fa",
               activebackground="#596275",activeforeground="#d1d8e0",command = login)
    btnlogin.place(relx=0.40,rely=0.75)
    adminpage.mainloop()
    
def delete_data():
    root = Tk()
    root.geometry("350x150")
    root.title("Delete your complaint")
    refs=StringVar()
    def delref():
        #for ref in range(complaint):
        if ref.get()=="":
            messagebox.showinfo("Message","Please enter referrence number !")
        elif ref.get() != id(complaint):
            messagebox.showinfo("Message","Complaint deleted successfully")   
        else:
            variable.remove(row[id(complaint)])
            messagebox.showinfo("Message","Complaint deleted successfully")
        
    label = Label(root,text="Enter reference number",font=("times",20,"bold"))
    label.pack(pady=5)
    ref = Entry(root,font=("times",20,"bold"),textvariable=refs)
    ref.place(relx=0.12,rely=0.30)
    btndel = Button(root,text="Delete",font=("times",20,"bold"),bg="red2",activebackground="red3",fg="#ffffff",
            command=delref)
    btndel.place(relx=0.36,rely=0.65)
    root.mainloop()
def clear_data():
    txtname.delete(0,END)
    txtmail.delete(0,END)
    txtdate.delete(0,END)
    txtgender.set('')
    txtcomplaint.delete(0,END)
window = Tk()
window.geometry("700x400")
window.config(bg="#273c75")
window.title("COMPLAINT MANAGEMENT SYSTEM")

lbl = Label(window,text = "COMPLAINT MANAGEMENT SYSTEM",font = ("times",20,"bold"),bg = "#f5f6fa",fg = "#1e3799")
lbl.pack(fill = X, pady = 10)

#name
name_lbl = Label(window, text = "Name",font = ("times",20,"bold"),bg = "#dcdde1",width = 9,fg = "#1e3799")
name_lbl.place(relx=0,rely=0.15)
txtname = Entry(window,width = 27,font = ("times",18,"bold"),bg = "#dcdde1",textvariable=names)
txtname.place(relx=0.19,rely=0.15)

#mail
mail_lbl = Label(window,text ="Mail",font =("times",20,"bold"),bg ="#dcdde1",fg = "#1e3799",width = 9)
mail_lbl.place(relx=0,rely=0.25)
txtmail = Entry(window,font = ("times",18,"bold"),bg = "#dcdde1",width =27,textvariable=mails)
txtmail.place(relx=0.19,rely=0.25)

#date
date_lbl = Label(window,text ="Date",font =("times",20,"bold"),bg ="#dcdde1",fg = "#1e3799",width = 9)
date_lbl.place(relx=0,rely=0.35)
txtdate = Entry(window,font = ("times",18,"bold"),bg = "#dcdde1",width =27,textvariable=dates)
txtdate.place(relx=0.19,rely=0.35)

#gender
gender_lbl = Label(window,text ="Gender",font =("times",20,"bold"),bg ="#dcdde1",fg = "#1e3799",width = 9)
gender_lbl.place(relx=0,rely=0.45)
txtgender = ttk.Combobox(window,font=("times",18,"bold"),width = 26,state = "readonly",textvariable= genders)
txtgender['values']=("Male","Female","Others")
txtgender.place(relx=0.19,rely=0.45)

#complaint
complaint_lbl = Label(window,text ="Register\n your\n complaint\n here\n",font =("times",20,"bold"),bg ="#dcdde1",fg = "#1e3799",width = 9)
complaint_lbl.place(relx=0,rely=0.55,height = 170)
txtcomplaint = Entry(window,font = ("times",18,"bold"),bg = "#dcdde1",width =27,textvariable = complaints)
txtcomplaint.place(relx=0.19,rely=0.55,height = 170)

#button submit
btn_submit = Button(window,text="Submit",font= ("times",30,"bold"),bg = "#1abc9c",activebackground = "#16a085",
             fg="#ffffff",width = 8,command = addData)
btn_submit.place(relx=0.69,rely=0.38)

#button admin
btn_update = Button(window,text="Admin",font= ("times",30,"bold"),bg = "#1B9CFC",activebackground = "#4b7bec",
                   fg="#ffffff",width = 8,command= admin)
btn_update.place(relx=0.69,rely=0.18)

#button delete
btn_delete = Button(window,text="Delete",font= ("times",30,"bold"),bg = "#f53b57",activebackground = "#ff3838",
                   fg="#ffffff",width = 8,command= delete_data)
btn_delete.place(relx=0.69,rely=0.58)

#butto clear
btn_clear = Button(window,text="Clear",font= ("times",30,"bold"),bg = "#ffc048",activebackground = "#EAB543",
                   fg="#ffffff",width = 8,command=clear_data)
btn_clear.place(relx=0.69,rely=0.78)



window.mainloop()