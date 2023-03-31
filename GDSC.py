from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import sqlite3
class student_details():
    def __init__(self, root):
        self.root=root
        self.root.title('Get safe water system')
        self.root.geometry('1400x700+0+0')
        title=Label(self.root, text='SAFE WATER SUPPLY SYSTEM',bd=9, relief=GROOVE, font=('times new roman',36, 'bold'), bg='yellow', fg='red4')
        title.pack(side=TOP, fill=X)
        #''''''''''''''''Variables
        self.id_No_var=IntVar()
        self.City_var=StringVar()
        self.name_var=StringVar()
        self.search_txt_var=StringVar()
        self.search_by_var=StringVar()
        self.email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=IntVar()


         

        ###the mainframe
        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg='blue')
        Manage_Frame.place(x=20, y=100, width=450, height= 585)

        m_title=Label(Manage_Frame, text='WATER USERS', bg='orange', fg='black', font=('times new roman', 30, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=28)

        lbl_Student_No=Label(Manage_Frame, text='id No', bg='blue', fg='white', font=('times new roman', 25, 'bold'))
        lbl_Student_No.grid(row=1, column=0, pady=0, padx=20,sticky='w')
        txt_Student_No=Entry(Manage_Frame,textvariable=self.id_No_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_Student_No.grid(row=1, column=1, pady=10, padx=20, sticky='w')



        lbl_name=Label(Manage_Frame, text='Name', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_name.grid(row=2, column=0, pady=0, padx=20,sticky='w')
        txt_name=Entry(Manage_Frame,textvariable=self.name_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')


        lbl_Email=Label(Manage_Frame, text='Email', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_Email.grid(row=3, column=0, padx=20,sticky='w')
        txt_Email=Entry(Manage_Frame, textvariable=self.email_var,font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        
        lbl_Gender=Label(Manage_Frame, text='Gender', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_Gender.grid(row=4, column=0, pady=0, padx=20,sticky='w')
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var, font=('times nemw roman', 13, 'bold'),state='readonly')
        combo_gender['values']=('male', 'Female', 'Other')
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact=Label(Manage_Frame, text='Contact', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_Contact.grid(row=5, column=0, pady=0, padx=20,sticky='w')
        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_Faculty=Label(Manage_Frame, text='City', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_Faculty.grid(row=6, column=0, pady=0, padx=20,sticky='w')
        txt_Faculty=Entry(Manage_Frame,textvariable=self.City_var, font=('times new roman', 15, 'bold'), bd=5, relief=GROOVE)
        txt_Faculty.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_Address=Label(Manage_Frame, text='Address', bg='blue', fg='white', font=('times new roman', 26, 'bold'))
        lbl_Address.grid(row=7, column=0, pady=0, padx=20,sticky='w')
        self.txt_Address=Text(Manage_Frame,width=30, height=3, font=('times new roman', 10, 'bold'))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        

     

    ######buton frame
        btn_Frame=Frame(Manage_Frame, bd=3, relief=RIDGE, bg='black')
        btn_Frame.place(x=15, y=525, width=420)

        Addbtn=Button(btn_Frame, text='Add', width=10, command=self.add_students)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)

        Updatebtn=Button(btn_Frame, text='Update', width=10, command=self.update_data)
        Updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn=Button(btn_Frame, text='Delete', width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)

        clearbtn=Button(btn_Frame, text='Clear', width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)





        ####details


        Details_Frame=Frame(self.root, bd=4, relief=RIDGE, bg='blue')
        Details_Frame.place(x=500, y=100, width=880, height= 585)

        lbl_search=Label(Details_Frame, text='Search By', bg='blue', fg='white', font=('times new roman', 20, 'bold'))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        combo_search=ttk.Combobox(Details_Frame,textvariable=self.search_by_var, font=('times nemw roman', 13, 'bold'),width=10,state='readonly')
        combo_search['values']=('id No', 'Name', 'Contact')
        combo_search.grid(row=0 , column=1, padx=20, pady=10)

        txt_search=Entry(Details_Frame, textvariable=self.search_txt_var,width=20,font=('times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

           

        searchbtn=Button(Details_Frame, text='Search', width=10, pady=5)
        searchbtn.grid(row=0, column=3, padx=10, pady=10)
        showallbtn=Button(Details_Frame, text='Show All', width=10,pady=5)
        showallbtn.grid(row=0, column=4, padx=10, pady=10)

        ####tableframe
        Table_Frame=Frame(Details_Frame, bd=4, relief=RIDGE, bg='red4')
        Table_Frame.place(x=10, y=70, width=760, height= 500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.student_details_table=ttk.Treeview(Table_Frame, column=('id_No','Gender', 'name', 'email', 'contact', 'City', 'Address'), xscrollcommand=scroll_y , yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.student_details_table.heading('id_No', text='id No.')
        self.student_details_table.heading('name', text='Name')
        self.student_details_table.heading('email', text='Email')
        self.student_details_table.heading('Gender', text='Gender')
        self.student_details_table.heading('contact', text='Contact')
        self.student_details_table.heading('City', text='City')
        self.student_details_table.heading('Address', text='Address')

        self.student_details_table['show']='headings'
        self.student_details_table.column('id_No', width=100)
        self.student_details_table.column('name', width=100)
        self.student_details_table.column('Gender', width=100)
        self.student_details_table.column('email', width=100)
        self.student_details_table.column('contact', width=100)
        self.student_details_table.column('City', width=100)
        self.student_details_table.column('Address', width=150)

        self.student_details_table.pack(fill=BOTH, expand=1)
        self.student_details_table.bind('<ButtonRelease-1>', self.get_cursor)

    def add_students(self):
         if self.id_No_var.get()=='' or self.name_var.get()=='':
             messagebox.showerror('Error', 'all fields are required boss')
         if self.id_No_var.get() == 'StringVar()' or self.Contact_var.get() == 'StringVar()':
            
            messagebox.showerror('Error', 'Enter an integer')
            
        
         else:
           

            
            

            con=sqlite3.connect('Student_details.db')
            cur=con.cursor()
            cur.execute('INSERT INTO student_detailss VALUES (:id_No, :name, :City, :email, :Contact,:Gender, :Address)', (self.id_No_var.get(),
                                                                             self.name_var.get(),
                                                                             self.City_var.get(),
                                                                             self.email_var.get(),
                                                                             self.Contact_var.get(),
                                                                             
                                                                             self.Gender_var.get(),                                                     
                                                                                                                                  
                                                                             self.txt_Address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            
            messagebox.showinfo('success', 'Record added succesfilly')



    def update_data(self):
        
        
        con=sqlite3.connect('Student_details.db')
        cur=con.cursor()
        cur.execute('UPDATE student_detailss SET (name= :name,Gender= :Gender,email= :email, Contact=:Contact,dob=:dob,Address= :Address WHERE id No=:id_No)', (self.id_No_var.get(),
                                                                              self.name_var.get(),
                                                                             
                                                                             self.City_var.get(),                                                                                           
                                                                             self.email_var.get(),
                                                                             self.Contact_var.get(),
                                                                             
                                                                             self.Gender_var.get(),                                                                                           
                                                                             self.txt_Address.get('1.0', END)))
        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        self.fetch_data()


    def delete_data(self):
        
         
        
        
        con=sqlite3.connect('Student_details.db')
        cur=con.cursor()
        cur.execute('delete from student_detail where Student_No=:Student_No', self.Student_No_var.get())
        
        con.commit()
        
        con.close()
        self.fetch_data
        self.clear_data

   


    def fetch_data(self):
        con=sqlite3.connect('Student_details.db')
        cur=con.cursor()
        con.execute('select * from student_detail')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_details_table.delete(*self.student_detail_table.get_children())
            for row in rows:
                self.student_detail_table.insert('', END, values=row)
            con.commit()
            
        con.close()



    def clear(self):
        self.id_No_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.Gender_var.set('')
        self.Contact_var.set('')
        self.City_var.set('')
        self.txt_Address.delete('1.0', END)
            
        
    def get_cursor(self,ev):
        cursor_row=self.student_detail_table.focus()
        contents=self.student_detail_table.item(cursor_row)
        row=contents['values']
        self.id_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.Contact_var.set(row[3])
        self.Gender_var.set(row[4])
        self.City_var.set(row[5])
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END, row[6])
        #if len(rows)!=0:
         #   self.student_details_table.delete(self.student_details_table.get_children())
        #  for row in rows:
         #       self.student_details_table.insert('', END, values=row)
          #  con.commit()
        #con.close()




        
class student_details():
    
    root=Tk()
    ob=student_details(root)
    root.mainloop()
