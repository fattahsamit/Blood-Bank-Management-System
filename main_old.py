#Tkinter is the standard GUI library for Python
from tkinter import *
from tkinter import ttk
import pymysql

#class creation
class Donor:
    def __init__(self,root):
        self.root=root
        #Title of the application
        self.root.title("Blood Donor Management System")
        #Setting the Resolution
        self.root.geometry("1350x700+0+0")
        
        
        #Title of the Upper Label. Can change the values of border,relief, fonts, background and foreground colour. 
        #relief = RAISED/ GROOVE/ RIDGE/ FLAT/ SUNKEN
        title=Label(self.root,text="🩸 Blood Donor Management System",bd=10,relief=RAISED,font=("arial",35,"bold"),bg="crimson",fg="white")
        #packed, choosing location, fill=X to fillup the X axis area
        title.pack(side=TOP,fill=X)
        

#-------VARIABLES--------- 
        #using String variable because we don't want to use any calculations with these
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.gender_var=StringVar()
        self.bg_var=StringVar()
        self.num_var=StringVar()
        self.email_var=StringVar()
        self.dob_var=StringVar()
        self.ail_var=StringVar()
        self.lastdn_var=StringVar()
        self.address_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
#-------MANAGE FRAME---------        
        #create frame
        #border size, style
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        #placement and resolution of the frame
        Manage_Frame.place(x=10,y=82,height=610,width=472)
        #title for Manage_Frame
        m_title=Label(Manage_Frame,text="Manage Donors",font=("arial",25,"bold"),bg="crimson",fg="white")
        #grid method makes table-like structure, How many Rows and Column will be there. padx/pady gives space between the x/y axis 
        m_title.grid(row=0,columnspan=2,pady=20)
        
     #ID
        #label field
        lbl_id=Label(Manage_Frame,text="ID No.",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_id.grid(row=1,column=0,pady=5,padx=10,sticky="w")
        #text field, using entry method
        #textvariable is used to access the variables
        txt_id=Entry(Manage_Frame,textvariable=self.id_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=5,padx=10,sticky="w")
        
     #Name
        lbl_name=Label(Manage_Frame,text="Name",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=5,padx=10,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=5,padx=10,sticky="w")
    
    #Gender (combobox) - kinda like a option system
        lbl_gender=Label(Manage_Frame,text="Gender",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=3,column=0,pady=5,padx=10,sticky="w")
        #using combobox
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("arial",14,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=3,column=1,pady=5,padx=10)
        
     #Blood Group (combobox)
        lbl_bg=Label(Manage_Frame,text="Blood Group",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_bg.grid(row=4,column=0,pady=5,padx=10,sticky="w")
        
        combo_bg=ttk.Combobox(Manage_Frame,textvariable=self.bg_var,font=("arial",14,"bold"),state="readonly")
        combo_bg['values']=("A+","A-","B+","B-","AB+","AB-","O+","O-")
        combo_bg.grid(row=4,column=1,pady=5,padx=10)
     
     #Phone Number
        lbl_num=Label(Manage_Frame,text="Phone Number",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_num.grid(row=5,column=0,pady=5,padx=10,sticky="w")
        
        txt_num=Entry(Manage_Frame,textvariable=self.num_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_num.grid(row=5,column=1,pady=5,padx=10,sticky="w")
        
     #Email
        lbl_email=Label(Manage_Frame,text="E-mail",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=6,column=0,pady=5,padx=10,sticky="w")
        
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=6,column=1,pady=5,padx=10,sticky="w")        
        
     #Date of Birth
        lbl_dob=Label(Manage_Frame,text="Date of Birth",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_dob.grid(row=7,column=0,pady=5,padx=10,sticky="w")
        
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=7,column=1,pady=5,padx=10,sticky="w")        
        
     #Known Ailments
        lbl_ail=Label(Manage_Frame,text="Known Ailments",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_ail.grid(row=8,column=0,pady=5,padx=10,sticky="w")
        
        txt_ail=Entry(Manage_Frame,textvariable=self.ail_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_ail.grid(row=8,column=1,pady=5,padx=10,sticky="w")
        
     #Last Donation
        lbl_lastdn=Label(Manage_Frame,text="Last Donation Date",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_lastdn.grid(row=9,column=0,pady=5,padx=10,sticky="w")
        
        txt_lastdn=Entry(Manage_Frame,textvariable=self.lastdn_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_lastdn.grid(row=9,column=1,pady=5,padx=10,sticky="w")
        
     #Address
        lbl_address=Label(Manage_Frame,text="Address",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_address.grid(row=10,column=0,pady=5,padx=10,sticky="w")

        txt_address=Entry(Manage_Frame,textvariable=self.address_var,font=("arial",15,"bold"),bd=5,relief=GROOVE)
        txt_address.grid(row=10,column=1,pady=5,padx=10,sticky="w")
        
        #using text method (we are not using it)
        #use the help of self to access Text data
        #self.txt_address=Text(Manage_Frame,height=3, width=29)
        #self.txt_address.grid(row=10,column=1,pady=5,padx=10,sticky="w") 
        
#-------BUTTON FRAME--------- 
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=12,y=555,width=433)
        
        #command is used to call function
        Addbtn=Button(btn_Frame,text="Add",width=11,command=self.add_donors).grid(row=0,column=0,padx=10,pady=5)
        upbtn=Button(btn_Frame,text="Update",width=11,command=self.update_data).grid(row=0,column=1,padx=10,pady=5)
        delbtn=Button(btn_Frame,text="Delete",width=11,command=self.delete_data).grid(row=0,column=2,padx=10,pady=5)
        clrbtn=Button(btn_Frame,text="Clear",width=11,command=self.clear).grid(row=0,column=3,padx=10,pady=5)
        
        
#-------DETAIL FRAME--------- 
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=487,y=82,height=610,width=857)
        
        lbl_search=Label(Detail_Frame,text="Search By",font=("arial",15,"bold"),bg="crimson",fg="white")
        lbl_search.grid(row=0,column=0,pady=5,padx=10,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=13,font=("arial",14,"bold"),state="readonly")
    #name must be same as the database
        combo_search['values']=("Blood_Group","Last_Donation","Address","Number")
        combo_search.grid(row=0,column=1,pady=5,padx=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=25,font=("arial",13,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=5,padx=10,sticky="w")
        
        searchbtn=Button(Detail_Frame,text="Search",width=13,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=5)
        showallbtn=Button(Detail_Frame,text="Show All",width=13,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=5)
        
#-------TABLE FRAME--------- 
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=50,height=545,width=830)
        #scrolling method to add scrollbars for x and y axis
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        #TreeView allows us to do is to build a tree-like structure and insert items accordingly
        self.Donor_table=ttk.Treeview(Table_Frame,columns=("id","name","gender","bg","num","email","dob","ail","lastdn","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Donor_table.xview)
        scroll_y.config(command=self.Donor_table.yview)
        self.Donor_table.heading("id",text="ID No.")
        self.Donor_table.heading("name",text="Name")
        self.Donor_table.heading("gender",text="Gender")
        self.Donor_table.heading("bg",text="Blood Group")
        self.Donor_table.heading("num",text="Phone No.")
        self.Donor_table.heading("email",text="E-mail")
        self.Donor_table.heading("dob",text="Date of Birth")
        self.Donor_table.heading("ail",text="Ailments")
        self.Donor_table.heading("lastdn",text="Last Donation")
        self.Donor_table.heading("address",text="Address")
        #only show the ones with headings
        self.Donor_table["show"]="headings"
        #setting the column
        self.Donor_table.column("id",width=45)
        self.Donor_table.column("name",width=100)
        self.Donor_table.column("gender",width=60)
        self.Donor_table.column("bg",width=75)
        self.Donor_table.column("num",width=75)
        self.Donor_table.column("email",width=130)
        self.Donor_table.column("dob",width=73)
        self.Donor_table.column("ail",width=85)
        self.Donor_table.column("lastdn",width=80)
        self.Donor_table.column("address",width=130)
        #filled the table and expanded it for it cover the whole table
        self.Donor_table.pack(fill=BOTH,expand=1)
        #button event
        self.Donor_table.bind("<ButtonRelease-1>",self.get_cursor)
        #to show the table from the database
        self.fetch_data()
        
    def add_donors(self):
        #connection with database #database name=bdms
        con=pymysql.connect(host="localhost",user="root",password="",database="bdms")
        #cursor function is used to execute queries
        cur=con.cursor()
        #sql queries, Table name=donors, Used a tuple to store into variables, get() for accessing
        cur.execute("insert into donors values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
                                                                                self.name_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.bg_var.get(),
                                                                                self.num_var.get(),
                                                                                self.email_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.ail_var.get(),
                                                                                self.lastdn_var.get(),
                                                                                self.address_var.get(),
                                                                                ))
        #get('1.0',END) will show the first and the last line.....in the middle. (we are not using it btw)
        con.commit()
        #to show the table after inserting into the database 
        self.fetch_data()
        #clears the manage donors tab
        self.clear()
        con.close()
        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="bdms")
        cur=con.cursor()
        cur.execute("select * from donors")
        #save all data into a variabble that will be fetched
        rows=cur.fetchall()
        #delete empty rows and their children
        if len(rows)!=0:
            self.Donor_table.delete(*self.Donor_table.get_children())
            for row in rows:
                self.Donor_table.insert('',END,values=row) #passing the values
            con.commit()
        con.close()
        
    def clear(self):             
        #will show empty values
        self.id_var.set(""),
        self.name_var.set(""),
        self.gender_var.set(""),
        self.bg_var.set(""),
        self.num_var.set(""),
        self.email_var.set(""),
        self.dob_var.set(""),
        self.ail_var.set(""),
        self.lastdn_var.set(""),
        self.address_var.set("")
     
    def get_cursor(self,ev):
        cursor_row=self.Donor_table.focus() #focus brings up the row selected by the cursor
        contents=self.Donor_table.item(cursor_row) #brings selected the data into the function
        row=contents['values'] #fetches the values
        
        #saved into a list and will show in the management tab
        self.id_var.set(row[0])
        self.name_var.set(row[1]),
        self.gender_var.set(row[2]),
        self.bg_var.set(row[3]),
        #concatenation
        self.num_var.set("0"+str(row[4])),
        self.email_var.set(row[5]),
        self.dob_var.set(row[6]),
        self.ail_var.set(row[7]),
        self.lastdn_var.set(row[8]),
        self.address_var.set(row[9])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="bdms")
        cur=con.cursor()
    #name must be same as the database
        cur.execute("update donors set name=%s,gender=%s,blood_group=%s,number=%s,email=%s,dob=%s,ailment=%s,last_donation=%s,address=%s where id=%s",(
                                                                                                            self.name_var.get(),
                                                                                                            self.gender_var.get(),
                                                                                                            self.bg_var.get(),
                                                                                                            self.num_var.get(),
                                                                                                            self.email_var.get(),
                                                                                                            self.dob_var.get(),
                                                                                                            self.ail_var.get(),
                                                                                                            self.lastdn_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.id_var.get()
                                                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="bdms")
        cur=con.cursor()
        cur.execute("delete from donors where id=%s",self.id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="bdms")
        cur=con.cursor()
       #cur.execute("select * from donors where " +str(self.search_by.get())+" LIKE '"+str(self.search_txt.get())+"%'")
       #cur.execute("select * from donors where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")        
        if str(self.search_by.get())=="Blood_Group":
            cur.execute("select * from donors where " +str(self.search_by.get())+" LIKE '"+str(self.search_txt.get())+"%'")
        else:
            cur.execute("select * from donors where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.Donor_table.delete(*self.Donor_table.get_children())
            for row in rows:
                self.Donor_table.insert('',END,values=row)
            con.commit()
        con.close()      
    
root=Tk()
ob=Donor(root)
#just remove the comment and change the filepath of the image file on your pc
#root.iconbitmap('D:/Blood-Bank-Management-System/blood_drop_no_shadow_icon-icons.com_76229.ico')
root.mainloop()