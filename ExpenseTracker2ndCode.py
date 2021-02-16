from tkinter import *
from tkinter import ttk
import sqlite3


class Expense:
    def __init__(self, root):
        self.root=root
        self.root.title("Expense Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="cadet blue")

        title = Label(self.root,text="Expense Management System",bd=10,relief=RIDGE, font=("arial",50,"bold"),bg="Ghost White",)
        title.pack(side=TOP,fill=X)

        #======All variables=====
        self.expID_var=StringVar()
        self.date_var=StringVar()
        self.spenton_var=StringVar()
        self.amount_var=StringVar()
        self.notes_var=StringVar()

        # Database

        # Connect Database
        conn = sqlite3.connect('expenses.db')

        # create cursor
        c = conn.cursor()

        # Create Table
        # c.execute('''
        #         CREATE TABLE expenses(
        #         number INTEGER PRIMARY KEY,
        #         date text,
        #         spent_on text,
        #         amount int
        #         )
        #         ''')

        # Create Submit Function For Databases

        def submit():
            # Connect Database
            conn = sqlite3.connect('expenses.db')

            # create cursor
            c = conn.cursor()

            #Insert into Table
            c.execute("INSERT INTO expenses VALUES(:number, :date, :spenton, :amount, :notes)",
                      {
                          'number': txt_expID.get(),
                          'date': txt_DoE.get(),
                          'spenton': txt_SpE.get(),
                          'amount': txt_AmT.get(),
                          'notes': txt_notes.get('1.0', 'end')
                      })
            # Comit Changes
            conn.commit()
            # Close Connection
            conn.close()

            txt_expID.delete(0, END)
            txt_DoE.delete(0, END)
            txt_SpE.delete(0, END)
            txt_AmT.delete(0, END)
            txt_notes.delete('1.0', 'end')

        #Create Query function
        def query():
            # Connect Database
            conn = sqlite3.connect('expenses.db')

            # create cursor
            c = conn.cursor()
            c.execute('SELECT * FROM expenses')
            rows = c.fetchall()
            for row in rows:
                print(row)



            # Comit Changes
            conn.commit()
            # Close Connections
            conn.close()


        # Comit Changes
        conn.commit()
        # Close Connections
        conn.close()
        #========manage frames===============

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Ghost White")
        Detail_Frame.place(x=500,y=100,width=800,height=580)


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Ghost White")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="MANAGE EXPENSES",bg="cadet blue",font=("arial",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_expID = Label(Manage_Frame,text="Number",bg="cadet blue",font=("arial",20,"bold"))
        lbl_expID.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_expID = Entry(Manage_Frame,textvariable=self.expID_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
        txt_expID.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_DoE=Label(Manage_Frame,text="Date",bg="cadet blue",font=("arial",20,"bold"))
        lbl_DoE.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_DoE=Entry(Manage_Frame,textvariable=self.date_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
        txt_DoE.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_SpE=Label(Manage_Frame,text="Spent On",bg="cadet blue",font=("arial",20,"bold"))
        lbl_SpE.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_SpE = Entry(Manage_Frame,textvariable=self.spenton_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
        txt_SpE.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_AmT=Label(Manage_Frame,text="Amount",bg="cadet blue",font=("arial",20,"bold"))
        lbl_AmT.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_AmT=Entry(Manage_Frame,textvariable=self.amount_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
        txt_AmT.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_notes=Label(Manage_Frame,text="Notes",bg="cadet blue",font=("arial",20,"bold"))
        lbl_notes.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_notes=Text(Manage_Frame,width=31,height=4,font=("",10),fg="Ghost White",bg="cadet blue",bd=5,relief=RIDGE)
        txt_notes.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        #===========Button frames=======

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='cadet blue')
        btn_Frame.place(x=10,y=500,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10, command=submit)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)

        lbl_search=Label(Detail_Frame,text="Search",bg="cadet blue",font=("arial",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("arial",13,"bold"),state='readonly')
        combo_search['values']=("Date","Spent On")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,width=20,font=("arial",13,"bold"),bd=5,relief=RIDGE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5, command=query).grid(row=0,column=3,padx=10,pady=10)
        showall=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #======table frame========
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Ghost white")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Expense_table=ttk.Treeview(Table_Frame,columns=("Number","Date","Spent On","Amount", "Notes"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Expense_table.xview)
        scroll_y.config(command=Expense_table.yview)
        Expense_table.heading("Number",text="Number")
        Expense_table.heading("Date",text="Date")
        Expense_table.heading("Spent On",text="Spent On")
        Expense_table.heading("Amount",text="Amount")
        Expense_table.heading("Notes",text="Notes")
        Expense_table['show']='headings'
        Expense_table.column("Number", width=60)

        Expense_table.pack()


root = Tk()
ob = Expense(root)
root.mainloop()