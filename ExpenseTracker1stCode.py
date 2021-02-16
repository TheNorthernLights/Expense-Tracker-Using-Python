from tkinter import *
from tkinter import ttk
import pymysql


class Expense:
	def _init_(self,root):
		self.root=root
		self.root.title("Expense Management System")
		self.root.geometry("1370x700+0+0")
		self.root.config(bg="cadet blue") 

		title = Label(self.root,text="Expense Management System",bd=10,relief=RIDGE, font=("arial",50,"bold"),bg="Ghost White",)
		title.pack(side=TOP,fill=X)

		#======All variables=====
		self.expID_var=StringVar()
		self.dates_var=StringVar()
		self.spenton_var=StringVar()
		self.amount_var=StringVar()
		self.notes_var=StringVar()
		self.search_by=StringVar()
		self.search_txt=StringVar()

		#========manage frames===============

		Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Ghost White")
		Detail_Frame.place(x=500,y=100,width=800,height=580)


		Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Ghost White")
		Manage_Frame.place(x=20,y=100,width=450,height=580)

		m_title=Label(Manage_Frame,text="MANAGE EXPENSES",bg="cadet blue",font=("arial",30,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_exp=Label(Manage_Frame,text="Number",bg="cadet blue",font=("arial",20,"bold"))
		lbl_exp.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		txt_exp=Entry(Manage_Frame,textvariable=self.expID_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
		txt_exp.grid(row=1,column=1,pady=10,padx=20,sticky="w")

		lbl_DoE=Label(Manage_Frame,text="Date",bg="cadet blue",font=("arial",20,"bold"))
		lbl_DoE.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		txt_DoE=Entry(Manage_Frame,textvariable=self.dates_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
		txt_DoE.grid(row=2,column=1,pady=10,padx=20,sticky="w")

		lbl_SpE=Label(Manage_Frame,text="Spent On",bg="cadet blue",font=("arial",20,"bold"))
		lbl_SpE.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		txt_SpE=Entry(Manage_Frame,textvariable=self.spenton_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
		txt_SpE.grid(row=3,column=1,pady=10,padx=20,sticky="w")

		lbl_AmT=Label(Manage_Frame,text="Amount",bg="cadet blue",font=("arial",20,"bold"))
		lbl_AmT.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		txt_AmT=Entry(Manage_Frame,textvariable=self.amount_var,font=("arial",15,"bold"),bd=5,relief=RIDGE,bg="cadet blue",fg="Ghost white")
		txt_AmT.grid(row=4,column=1,pady=10,padx=20,sticky="w")

		lbl_notes=Label(Manage_Frame,text="Notes",bg="cadet blue",font=("arial",20,"bold"))
		lbl_notes.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		self.txt_notes=Text(Manage_Frame,width=31,height=4,font=("",10),fg="Ghost White",bg="cadet blue",bd=5,relief=RIDGE)
		self.txt_notes.grid(row=5,column=1,pady=10,padx=20,sticky="w")

		#===========Button frames=======

		btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='cadet blue')
		btn_Frame.place(x=10,y=500,width=420)

		Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_expenses).grid(row=0,column=0,padx=10,pady=10)
		updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
		deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
		clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

		lbl_search=Label(Detail_Frame,text="Search",bg="cadet blue",font=("arial",20,"bold"))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("arial",13,"bold"),state='readonly')
		combo_search['values']=("date","spenton")
		combo_search.grid(row=0,column=1,padx=20,pady=10)

		txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("arial",13,"bold"),bd=5,relief=RIDGE)
		txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

		searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
		showall=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

		#======table frame========
		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Ghost white")
		Table_Frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
		self.Expense_table=ttk.Treeview(Table_Frame,columns=("Number","Date","Spent On","Amount","Notes"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.Expense_table.xview)
		scroll_y.config(command=self.Expense_table.yview)
		self.Expense_table.heading("Number",text="Number")
		self.Expense_table.heading("Date",text="Date")
		self.Expense_table.heading("Spent On",text="Spent On")
		self.Expense_table.heading("Amount",text="Amount")
		self.Expense_table.heading("Notes",text="Notes")
		self.Expense_table['show']='headings'
		self.Expense_table.column("Number",width=60)

		self.Expense_table.pack()
		self.Expense_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()
	def add_expenses(self):
		con=pymysql.connect(host="localhost",user="root",password="snow@mysql",database="ems")
		cur=con.cursor()
		cur.execute("INSERT into expenses values(%s,%s,%s,%s,%s)",(self.expID_var.get(),
																self.dates_var.get(),
																self.spenton_var.get(),
																self.amount_var.get(),
																self.txt_notes.get('1.0',END)
																))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def fetch_data(self):
		con=pymysql.connect(host="localhost",user="root",password="snow@mysql",database="ems")
		cur=con.cursor()
		cur.execute("SELECT *from expenses")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Expense_table.delete(*self.Expense_table.get_children())
			for row in rows:
				self.Expense_table.insert('',END,values=row)
			con.commit()
		con.close()	

	def clear(self):
		self.expID_var.set("")
		self.dates_var.set("")
		self.spenton_var.set("")
		self.amount_var.set("")
		self.txt_notes.delete('1.0',END)

	def get_cursor(self,ev):
		cursor_row=self.Expense_table.focus()
		contents=self.Expense_table.item(cursor_row)
		row=contents['values']
		self.expID_var.set(row[0])
		self.dates_var.set(row[1])
		self.spenton_var.set(row[2])
		self.amount_var.set(row[3])
		self.txt_notes.delete('1.0',END)
		self.txt_notes.insert(END,row[4])

	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",password="snow@mysql",database="ems")
		cur=con.cursor()
		cur.execute("UPDATE expenses SET date=%s,spenton=%s,amount=%s,notes=%s WHERE expID=%s",(
																self.dates_var.get(),
																self.spenton_var.get(),
																self.amount_var.get(),
																self.txt_notes.get('1.0',END),
																self.expID_var.get()
																))
		con.commit()

		self.fetch_data()
		self.clear()
		con.close()

	def delete_data(self):
		con=pymysql.connect(host="localhost",user="root",password="snow@mysql",database="ems")
		cur=con.cursor()
		cur.execute("DELETE from expenses where expID=%s",self.expID_var.get())
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def search_data(self):
		con=pymysql.connect(host="localhost",user="root",password="snow@mysql",database="ems")
		cur=con.cursor()

		cur.execute("SELECT *from expenses where "+str(self.search_by.get())+" LIKE '%s"+str(self.search_txt.get())+"%s'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Expense_table.delete(*self.Expense_table.get_children())
			for row in rows:
				self.Expense_table.insert('',END,values=row)
			con.commit()
		con.close()



root=Tk()
ob=Expense()
root.mainloop()