from asyncio.windows_events import NULL
from cmath import rect
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.tix import Tree
import mysql.connector
from tkinter import *
   
mysqldb=mysql.connector.connect(host="localhost",user="root",password="hikam0611",database="perpustakaan")
mycursor=mysqldb.cursor()

def get_value(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['ISBN'])
    e2.insert(0,select['Judul Buku'])
    e3.insert(0,select['Nama Penulis'])
    e4.insert(0,select['Tahun Terbit'])

def by_isbn():
    key = [e1.get()]
    sql = "SELECT isbn,judul,penulis,tahun_terbit,rating_average FROM perpustakaan.daftar_buku WHERE isbn LIKE %s"
    val = key
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    print(results)
    
    for i in listBox.get_children() :
        listBox.delete(i)
            
    for i, (isbn, judul, penulis, tahun_terbit, rating) in enumerate(results, start=1):
        listBox.insert("", "end", values=(isbn, judul, penulis, tahun_terbit, rating))
        
def by_judul():
    key = [e2.get()]
    sql = "SELECT isbn,judul,penulis,tahun_terbit,rating_average FROM perpustakaan.daftar_buku WHERE judul LIKE %s"
    val = key
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    print(results)

    for i in listBox.get_children():
        listBox.delete(i)
    
    for i, (isbn, judul, penulis, tahun_terbit, rating) in enumerate(results, start=1):
        listBox.insert("", "end", values=(isbn, judul, penulis, tahun_terbit, rating))

def by_penulis():
    key = [e3.get()]
    sql = "SELECT isbn,judul,penulis,tahun_terbit,rating_average FROM perpustakaan.daftar_buku WHERE penulis LIKE %s"
    val = key
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    print(results)

    for i in listBox.get_children():
        listBox.delete(i)
        
    for i, (isbn, judul, penulis, tahun_terbit, rating) in enumerate(results, start=1):
        listBox.insert("", "end", values=(isbn, judul, penulis, tahun_terbit, rating))
        
def by_tahun():
    key = [e4.get()]
    sql = "SELECT isbn,judul,penulis,tahun_terbit,rating_average FROM perpustakaan.daftar_buku WHERE tahun_terbit LIKE %s"
    val = key
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    print(results)

    for i in listBox.get_children():
        listBox.delete(i)
        
    for i, (isbn, judul, penulis, tahun_terbit, rating) in enumerate(results, start=1):
        listBox.insert("", "end", values=(isbn, judul, penulis, tahun_terbit, rating))
         
def show():
    mycursor.execute("SELECT isbn,judul,penulis,tahun_terbit,rating_average FROM perpustakaan.daftar_buku")
    results = mycursor.fetchall()
    print(results)

    for i, (isbn, judul, penulis, tahun_terbit, rating) in enumerate(results, start=1):
        listBox.insert("", "end", values=(isbn, judul, penulis, tahun_terbit, rating))
               
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    for i in listBox.get_children():
        listBox.delete(i)
                   
def rating():
    rate_input = [var.get()]
    isbn = [e1.get()]
    
    sql = "SELECT rating_count FROM perpustakaan.daftar_buku WHERE isbn LIKE %s"
    val = isbn
    mycursor.execute(sql, val)
    rec1 = mycursor.fetchall()
    print(rec1)
    
    if rec1 is None:
        sql = "INSERT INTO perpustakaan.daftar_buku (rating_count) VALUES (%s) WHERE isbn LIKE %s"
        val = (rate_input, isbn)
        mycursor.execute(sql, val)
        mysqldb.commit()         

    sql = "INSERT INTO perpustakaan.daftar_buku (rating_average) VALUES (%s) WHERE isbn LIKE %s"
    val = (rate_input, isbn)
    mycursor.execute(sql, val)
    mysqldb.commit()
        
    messagebox.showinfo("information", "Kamu sudah memberikan Rating, Terimakasih...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()
        
#inisialisasi tkinter
root = Tk()

root.title("Welcome to Search Book Library App")

tk.Label(root, text="SEARCH BOOK LIBRARY", fg="black", font=("Times New Roman", 40)).place(x=200, y=5)

root.geometry("1020x535")

global e1
global e2
global e3
global e4

Label(root, text="ISBN").place(x=10, y=103)
Label(root, text="Judul Buku").place(x=10, y=138)
Label(root, text="Penulis").place(x=10, y=173)
Label(root, text="Tahun Terbit").place(x=10, y=208)

e1 = Entry(root)
e1.place(x=140, y=103)

e2 = Entry(root)
e2.place(x=140, y=138)

e3 = Entry(root)
e3.place(x=140, y=173)

e4 = Entry(root)
e4.place(x=140, y=208)

Button(root, text="Search",command = by_isbn,height=1, width= 10).place(x=300, y=100)
Button(root, text="Search",command = by_judul,height=1, width= 10).place(x=300, y=135)
Button(root, text="Search",command = by_penulis,height=1, width= 10).place(x=300, y=170)
Button(root, text="Search",command = by_tahun,height=1, width= 10).place(x=300, y=205)

Button(root, text="Show All Books",command = show,height=1, width= 15).place(x=10, y=250)
Button(root, text="Refresh",command = show,height=1, width= 14).place(x=150, y=250)
Button(root, text="Clear All",command = clear,height=1, width= 14).place(x=290, y=250)
Button(root, text="Rate this book",command = rating,height=1, width= 15).place(x=500, y=250)

def select():
   selection = "You selected for " + str(var.get()) + " Stars\ndo you want to rate this book?"
   stars_choice.config(text = selection)

Label(root, text="BERI RATING:", font=("Arial", 13)).place(x=500, y=110)

#stars rate choice
var = IntVar()
R1 = Radiobutton(root, text="1 Star", variable=var, value=1,command=select)
R1.pack( anchor = W )
R1.place(x=500,y=140)
R2 = Radiobutton(root, text="2 Star", variable=var, value=2,command=select)
R2.pack( anchor = W )
R2.place(x=500,y=160)
R3 = Radiobutton(root, text="3 Star", variable=var, value=3,command=select)
R3.pack( anchor = W)
R3.place(x=500,y=180)
R4 = Radiobutton(root, text="4 Star", variable=var, value=4,command=select)
R4.pack( anchor = W)
R4.place(x=500,y=200)
R5 = Radiobutton(root, text="5 Star", variable=var, value=5,command=select)
R5.pack( anchor = W)
R5.place(x=500,y=220)
       
stars_choice = Label(root)
stars_choice.pack()
stars_choice.place(x=600,y=170)

#table list book
cols = ('ISBN', 'Judul Buku', 'Nama Penulis','Tahun Terbit', 'Rating Buku')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)

    listBox.place(x=10, y=300)


show()

listBox.bind('<Double-Button-1>', get_value)

mainloop()