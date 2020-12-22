from tkinter import Label,Button,Tk,Entry
import sqlite3

root=Tk()
root.title('Database app')

conn= sqlite3.connect('adress_book.db')
c= conn.cursor()

'''
c.execute(""" CREATE TABLE adresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
""")'''
#create edit fuction to Update
def update():
    conn= sqlite3.connect('adress_book.db')
    c= conn.cursor()

    record_id=del_box.get()
    c.execute("""UPDATE adresses SET
    first_name= :first,
    last_name= :last,
    address= :address,
    city= :city,
    state= :state,
    zipcode= :zipcode

    WHERE oid= :oid""",
    {
    'first':f_name_editor.get(),
    'last':l_name_editor.get(),
    'address':address_editor.get(),
    'city':city_editor.get(),
    'state':state_editor.get(),
    'zipcode':zipcode_editor.get(),

    'oid':record_id

    })

    conn.commit()
    conn.close()
    editor.destroy()


#define edit fuction to update record
def edit():
    global editor
    editor=Tk()
    editor.title('Update the Record')
    editor.geometry("320x300")

    conn= sqlite3.connect('adress_book.db')
    c= conn.cursor()

    record_id=del_box.get()

    #query the database
    c.execute('SELECT * FROM adresses WHERE oid='+record_id)
    records=c.fetchall()   #fetchone, fetchmany

    #create global variable for text names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes
    f_name_editor= Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor= Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    address_editor= Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    city_editor= Entry(editor,width=30)
    city_editor.grid(row=3,column=1)
    state_editor= Entry(editor,width=30)
    state_editor.grid(row=4,column=1)
    zipcode_editor= Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)

    #crete textbox labels
    f_name_label=Label(editor,text="First Name:")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label= Label(editor,text="Last Name:")
    l_name_label.grid(row=1,column=0)
    address_label= Label(editor,text="Adress:")
    address_label.grid(row=2,column=0)
    city_label= Label(editor,text="City:")
    city_label.grid(row=3,column=0)
    state_label= Label(editor,text="State:")
    state_label.grid(row=4,column=0)
    zipcode_label= Label(editor,text="Zip Code:")
    zipcode_label.grid(row=5,column=0)

    #loop through results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    #save Button
    edit_button=Button(editor,text="Save records",command=update)
    edit_button.grid(row=6,column=0,columnspan=2,pady=10,ipadx=111,padx=10)

    #editor.destroy()


#delete function to delete records
def delete():
    conn=sqlite3.connect('adress_book.db')
    c=conn.cursor()

    c.execute("DELETE from adresses WHERE oid="+del_box.get())  #where f_name='Saphal'

    conn.commit()
    conn.close()




#create submit funtion for db
def submit():

    conn= sqlite3.connect('adress_book.db')
    c= conn.cursor()

    #insert into TABLE
    c.execute("INSERT INTO adresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode )",
           {
               'f_name':f_name.get(),
               'l_name':l_name.get(),
               'address':address.get(),
               'city':city.get(),
               'state':state.get(),
               'zipcode':zipcode.get()
           })

    conn.commit()
    conn.close()
    #claer Text Boxes
    f_name.delete(0,"end")
    l_name.delete(0,'end')
    address.delete(0,'end')
    state.delete(0,'end')
    city.delete(0,'end')
    zipcode.delete(0,'end')

#create database show button
def query():
    conn= sqlite3.connect('adress_book.db')
    c= conn.cursor()

    #query the database
    c.execute('SELECT *,oid FROM adresses')
    records=c.fetchall()   #fetchone, fetchmany
    print(records)

    print_records=''
    for record in records:
        print_records+=str(record[0])+' '+str(record[1])+' '+'\t'+str(record[6])+'\n'

    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)

    conn.commit()
    conn.close()


#create text boxes
f_name= Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name= Entry(root,width=30)
l_name.grid(row=1,column=1)
address= Entry(root,width=30)
address.grid(row=2,column=1)
city= Entry(root,width=30)
city.grid(row=3,column=1)
state= Entry(root,width=30)
state.grid(row=4,column=1)
zipcode= Entry(root,width=30)
zipcode.grid(row=5,column=1)
del_box=Entry(root,width=30)
del_box.grid(row=9,column=1,pady=5)



#crete textbox labels
f_name_label=Label(root,text="First Name:")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label= Label(root,text="Last Name:")
l_name_label.grid(row=1,column=0)
address_label= Label(root,text="Adress:")
address_label.grid(row=2,column=0)
city_label= Label(root,text="City:")
city_label.grid(row=3,column=0)
state_label= Label(root,text="State:")
state_label.grid(row=4,column=0)
zipcode_label= Label(root,text="Zip Code:")
zipcode_label.grid(row=5,column=0)
del_box_label=Label(root,text=" Select Id: ")
del_box_label.grid(row=9,column=0,pady=5)

#Create _SUBMIT button
submit_button=Button(root,text='Add record to db',command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create query Button
query_button=Button(root,text='Show records',command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,ipadx=111,padx=10)

#create del Button
delete_button=Button(root,text='Delete records',command=delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=10,ipadx=11,padx=10)

#update Button
edit_button=Button(root,text="Edit records",command=edit)
edit_button.grid(row=11,column=0,columnspan=2,pady=10,ipadx=11,padx=10)

conn.commit()
conn.close()

root.mainloop()
