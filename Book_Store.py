from cgitb import reset
from datetime import date
from email.mime import application
from logging.config import valid_ident
from math import fabs
from msilib.schema import PublishComponent
from sqlite3 import connect
import sqlite3
from textwrap import fill
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import end_fill, heading, left, width
from unittest import result
from pip import main
import mysql.connector
from mysql.connector import Error



# Main Class
class ConnectorDB:

    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.title(102* titlespace + "My Sql Connector")
        self.root.geometry("795x700+300+0")
        self.root.resizable(width = False, height = False)
    

#  Front styling
# ============================================================================================================================

        mainFrame = Frame(self.root, bd = 10, width = 775, height = 100, relief = RIDGE, bg = "gray")
        mainFrame.grid()

        titleFrame = Frame(mainFrame, bd = 5, width = 755, height = 100, relief = RIDGE)
        titleFrame.grid(row = 0, column = 0)

        topFrame3 = Frame(mainFrame, bd = 5, width = 755, height = 500, relief = RIDGE)
        topFrame3.grid(row = 1, column = 0)

        leftFrame = Frame(topFrame3, bd = 5, width = 775, height = 400, padx = 2, bg = "gray", relief = RIDGE)
        leftFrame.pack(side = LEFT)
        leftFrame1 = Frame(leftFrame, bd = 5, width = 600, height = 380, padx = 2, pady = 4, relief = RIDGE)
        leftFrame1.pack(side = TOP, padx = 0, pady = 0)

        rightFrame1 = Frame(topFrame3, bd = 5, width = 130, height = 400, padx = 2, bg = "gray", relief = RIDGE)
        rightFrame1.pack(side = RIGHT)
        rightFrame1a = Frame(rightFrame1, bd = 5, width = 120, height = 380, padx = 2, pady = 2, relief = RIDGE)
        rightFrame1a.pack(side = TOP)

# ============================================================================================================================

# Valiables 
        B_ID = StringVar()
        B_TITLE = StringVar()
        B_A_FNAME = StringVar()
        B_A_LNAME = StringVar()
        B_PUBLISHER = StringVar()
        B_PUB_DATE = StringVar()
        B_SUBJECT = StringVar()
        B_UNIT_PRIZE = StringVar()
        B_STOCK = StringVar()


        # Exit Function 
# ============================================================================================================================


        def iExit():
            iExit = tkinter.messagebox.askyesno("Book Store", "Confirm If You Want to Exit")
            if iExit > 0:
                root.destroy()
                return

#  Adding data to database
# ============================================================================================================================

        def addData():
            try:
                # Connecting to Database
                connection = mysql.connector.connect(host='localhost',
                                         database='book_store',
                                         user='root',
                                         password='1212')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()

                    #  Input data
                    bookTitle = B_TITLE.get()
                    autherFname = B_A_FNAME.get()
                    autherLname = B_A_LNAME.get()
                    publisherName = B_PUBLISHER.get()
                    PublicationDate = B_PUB_DATE.get()
                    bookSubject = B_SUBJECT.get()
                    bookPrice = B_UNIT_PRIZE.get()
                    bookStock = B_STOCK.get()

                    sql = "SELECT * FROM auther where A_FNAME='"+autherFname+"'"
                    cursor.execute(sql)
                    auther = cursor.fetchall()
                    if(len(auther)>0):
                        print("Auther already Existed !")
                    
                    else:
                        sql = "INSERT INTO auther (A_FNAME, A_LNAME) VALUES (%s, %s)"
                        val = (autherFname, autherLname)
                        cursor.execute(sql, val)
                        connection.commit()

                        
                #  last inserted Auther
                cursor.execute("select * from auther ORDER BY A_ID DESC LIMIT 1")
                autherID = cursor.fetchall()
                lastInsertedAutherID = autherID[0][0]
                lastInsertedAutherName = autherID [0][1]


                # # same auther same book
                sql = "SELECT B_A_ID, B_TITLE FROM books where B_TITLE='"+bookTitle+"'"
                cursor.execute(sql)
                autherID_inBook = cursor.fetchall()
                print("add: ",autherID_inBook)

                if(len(autherID_inBook) > 0):
                    tkinter.messagebox.showerror("Book Store", "Record already Existed !")
                else:
                    sql = "SELECT * FROM auther WHERE A_FNAME='"+autherFname+"'"
                    cursor.execute(sql)
                    autherID = cursor.fetchall()
                    autherID = autherID[0][0]
                    sql = "INSERT INTO books (B_TITLE, B_A_ID, B_PUBLISHER, B_PUB_DATE, B_SUBJECT, B_UNIT_PRIZE, B_STOCK) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (bookTitle, autherID, publisherName, PublicationDate, bookSubject, bookPrice)
                    cursor.execute(sql, val)
                    connection.commit()
                    connection.close() 
                    tkinter.messagebox.showinfo("Book Store", "Record enter Successfully !")
  
            except Error as e:
                print("Error while connecting to MySQL", e)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")


#  Update data to database
# ============================================================================================================================

        def update():
            try:
                # Connecting to Database
                connection = mysql.connector.connect(host='localhost',
                                         database='book_store',
                                         user='root',
                                         password='1212')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()

                    #  Input data
                    bookID = B_ID.get()
                    bookTitle = B_TITLE.get()
                    autherFname = B_A_FNAME.get()
                    autherLname = B_A_LNAME.get()
                    publisherName = B_PUBLISHER.get()
                    PublicationDate = B_PUB_DATE.get()
                    bookSubject = B_SUBJECT.get()
                    bookPrice = B_UNIT_PRIZE.get()
                    bookStock = B_STOCK.get()

                    sql = "SELECT * FROM auther where A_FNAME='"+autherFname+"'"
                    cursor.execute(sql)
                    auther = cursor.fetchall()
                    if(len(auther)):
                        print("Auther already Existed !")
                    
                    else:
                        sql = "INSERT INTO auther (A_FNAME, A_LNAME) VALUES (%s, %s)"
                        val = (autherFname, autherLname)
                        cursor.execute(sql, val)
                        connection.commit()

                # current auther if inserted id 
                cursor.execute("select A_ID FROM auther WHERE A_FNAME='"+autherFname+"'")
                autherID = cursor.fetchall()
                currentInsertedAutheID = autherID [0][0]
                print("current", currentInsertedAutheID)

                sql = "Update books set B_TITLE = %s, B_A_ID = %s, B_PUBLISHER = %s, B_PUB_DATE = %s, B_SUBJECT = %s, B_UNIT_PRIZE = %s, B_STOCK = %s WHERE B_ID=%s"
                val = (bookTitle, currentInsertedAutheID, publisherName, PublicationDate, bookSubject, bookPrice, bookStock, bookID)
                cursor.execute(sql, val)
                connection.commit()
                connection.close() 
  
            except Error as e:
                print("Error while connecting to MySQL", e)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")


#  Displaying Data
# ============================================================================================================================

        def displayData():
            try:
                # Connecting to Database
                connection = mysql.connector.connect(host='localhost', database='book_store',user='root', password='1212')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()
                    cursor.execute("select b.B_ID, b.B_TITLE, a.A_FNAME,a.A_LNAME, b.B_PUBLISHER , b.B_PUB_DATE, b.B_SUBJECT, b.B_UNIT_PRIZE, b.B_STOCK from books b JOIN auther a on b.B_A_ID = a.A_ID")
                    result = cursor.fetchall()
 

                    if len(result) != 0:
                        self.bookStore.delete(*self.bookStore.get_children())
                        for row in result:
                            self.bookStore.insert('', END, values = row)

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

# Touch to Input 

# ============================================================================================================================

        def treeInfo(arg):
            viewInfo = self.bookStore.focus()
            learnerData = self.bookStore.item(viewInfo)
            row = learnerData['values']

            B_ID.set(row[0])
            B_TITLE.set(row[1])
            B_A_FNAME.set(row[2])
            B_A_LNAME.set(row[3]) 
            B_PUBLISHER.set(row[4])
            B_PUB_DATE.set(row[5])
            B_SUBJECT.set(row[6])
            B_UNIT_PRIZE.set(row[7])
            B_STOCK.set(row[8])

# deleting Database values
# ============================================================================================================================

        def delete():
            try:
                # Connecting to Database
                connection = mysql.connector.connect(host='localhost',
                                         database='book_store',
                                         user='root',
                                         password='1212')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()

                    sql = "DELETE FROM books WHERE B_ID='"+B_ID.get()+"'"
                    cursor.execute(sql)
                    connection.commit()
                    connection.close()

                    tkinter.messagebox.showinfo("Book Store","Record Deleted SussessFully")

            except Error as e:
                print("Error while connecting to MySQL", e)
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

# search 
#======================================================================================================

        def searchDB():
            try:
                # Connecting to Database
                connection = mysql.connector.connect(host='localhost',
                                         database='book_store',
                                         user='root',
                                         password='1212')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()

                    cursor.execute("SELECT books.B_ID, books.B_TITLE, auther.A_FNAME, auther.A_LNAME, books.B_PUBLISHER, books.B_PUB_DATE, books.B_SUBJECT, books.B_UNIT_PRIZE, books.B_STOCK FROM books JOIN auther ON books.B_A_ID = auther.A_ID WHERE books.B_ID='"+B_ID.get()+"'")
                    result = cursor.fetchall()

                    print(result)
                    if len(result) != 0:
                        self.bookStore.delete(*self.bookStore.get_children())
                        for row in result:
                            self.bookStore.insert('', END, values = row)
                    else:
                        tkinter.messagebox.showinfo("Book Store", "No search fOUND")
                    connection.commit()
            except:
                reset()
            connection.close()


#======================================================================================================

        def open_win():
            new= Toplevel(root)
            new.geometry("450x250")
            new.title("New Window")

            mainFrame = Frame(self.root, bd = 10, width = 775, height = 100, relief = RIDGE, bg = "gray")
            mainFrame.grid()

            titleFrame = Frame(mainFrame, bd = 5, width = 755, height = 100, relief = RIDGE)
            titleFrame.grid(row = 0, column = 0)

            topFrame3 = Frame(mainFrame, bd = 5, width = 755, height = 500, relief = RIDGE)
            topFrame3.grid(row = 1, column = 0)

            connection = mysql.connector.connect(host='localhost',
                                         database='book_store',
                                         user='root',
                                         password='1212')
            if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()
                    

                    # tottal books availabe
                    sql = "SELECT SUM(B_STOCK)FROM books"
                    cursor.execute(sql)
                    totalBooks = cursor.fetchall()
                    totalBooks[0][0]

                    # Books reserved
                    sql = "SELECT SUM(R_B_QUANTITY)FROM reservation"
                    cursor.execute(sql)
                    reservedBooks = cursor.fetchall()
                    reservedBooks[0][0]

                    sql = "SELECT B_TITLE,  B_PUB_DATE FROM books ORDER BY B_PUB_DATE DESC"
                    cursor.execute(sql)
                    bookPub = cursor.fetchall()

                    sql = "SELECT B_ID, B_SUBJECT, SUM(B_STOCK) AS Stock, COUNT(B_SUBJECT) AS COUNT FROM books GROUP BY B_SUBJECT"
                    cursor.execute(sql)
                    booksPerSub = cursor.fetchall()

                    sql = "SELECT AVG(B_UNIT_PRIZE) FROM books"
                    cursor.execute(sql)
                    avgPrice = cursor.fetchall()


                    connection.commit()
                    connection.close()




# Input fields styling
#======================================================================================================
    #  Title name 
        self.title = Label(titleFrame, font = ("arial", 40, "bold"), text = "Book Store")
        self.title.grid(row = 0, column = 0, padx = 172)


        self.bookID = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Book ID")
        self.bookID.grid(row = 1, column = 0, sticky = W, padx = 5)
        self.bookIDEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_ID)
        self.bookIDEn.grid(row = 1, column = 1, sticky = W, padx = 5)

        self.bookID = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Book Title")
        self.bookID.grid(row = 2, column = 0, sticky = W, padx = 5)
        self.bookIDEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_TITLE)
        self.bookIDEn.grid(row = 2, column = 1, sticky = W, padx = 5)
        
        self.bookTitle = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Auther First Name")
        self.bookTitle.grid(row = 3, column = 0, sticky = W, padx = 5)
        self.bookTitleEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_A_FNAME)
        self.bookTitleEn.grid(row = 3, column = 1, sticky = W, padx = 5)
        
        self.autherName = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Auther Last Name")
        self.autherName.grid(row = 4, column = 0, sticky = W, padx = 5)
        self.autherNameEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_A_LNAME)
        self.autherNameEn.grid(row = 4, column = 1, sticky = W, padx = 5)

        self.publisherName = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Publisher Name")
        self.publisherName.grid(row = 5, column = 0, sticky = W, padx = 5)
        self.publisherNameEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_PUBLISHER)
        self.publisherNameEn.grid(row = 5, column = 1, sticky = W, padx = 5)

        self.publicationDate = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Publication Date")
        self.publicationDate.grid(row = 6, column = 0, sticky = W, padx = 5)
        self.publicationDateEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_PUB_DATE)
        self.publicationDateEn.grid(row = 6, column = 1, sticky = W, padx = 5)

        self.bookSubject = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Subject Of Book")
        self.bookSubject.grid(row = 7, column = 0, sticky = W, padx = 5)
        self.bookSubjectEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_SUBJECT)
        self.bookSubjectEn.grid(row = 7, column = 1, sticky = W, padx = 5)

        self.bookPrice = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Price Of the Book")
        self.bookPrice.grid(row = 8, column = 0, sticky = W, padx = 5)
        self.bookPriceEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_UNIT_PRIZE)
        self.bookPriceEn.grid(row = 8, column = 1, sticky = W, padx = 5)

        self.bookPrice = Label(leftFrame1, font = ("arial", 12, "bold"), text = "Books In stock")
        self.bookPrice.grid(row = 9, column = 0, sticky = W, padx = 5)
        self.bookPriceEn = Entry(leftFrame1, font = ("arial", 12, "bold"), bd = 5, width = 44, justify = "left", textvariable = B_STOCK)
        self.bookPriceEn.grid(row = 9, column = 1, sticky = W, padx = 5)


# TreeView
# ============================================================================================================================

        scroll_Y = Scrollbar(leftFrame, orient = VERTICAL)

        self.bookStore = ttk.Treeview(leftFrame, height = 12, columns = ("BookID", "BookTitle","authFName","authLastName", "pubName", "PubDate", "Subject"
        "Price", "Stock", "jpo"),xscrollcommand = scroll_Y.set)

        scroll_Y.pack(side = RIGHT, fill = Y)

        self.bookStore.heading("#1", text = "ID")
        self.bookStore.heading("#2", text = "Title")
        self.bookStore.heading("#3", text = "Auth F-Name")
        self.bookStore.heading("#4", text = "Auth L-Name")
        self.bookStore.heading("#5", text = "Publisher")
        self.bookStore.heading("#6", text = "Pub-Date")
        self.bookStore.heading("#7", text = "Subject")
        self.bookStore.heading("#8", text = "Price")
        self.bookStore.heading("#9", text = "Stock")

        self.bookStore ['show'] = 'headings'

        self.bookStore.column("#1", width = 1)
        self.bookStore.column("#2", width = 50)
        self.bookStore.column("#3", width = 60)
        self.bookStore.column("#4", width = 70)
        self.bookStore.column("#5", width = 40)
        self.bookStore.column("#6", width = 50)
        self.bookStore.column("#7", width = 30)
        self.bookStore.column("#8", width = 20)
        self.bookStore.column("#9", width = 20)

        self.bookStore.pack(fill = BOTH)
        self.bookStore.bind("<ButtonRelease-1>", treeInfo)
        displayData()





# Button
# ======================================================================================================================

        self.addNew = Button(rightFrame1a, font = ("arial", 12, "bold"), text = " Add New", bd =4,
        padx =24, pady = 1, width = 6, height = 2, command = addData).grid(row = 0, column = 0, padx = 1)

        self.detete = Button(rightFrame1a, font = ("arial", 12, "bold"), text = " Delete", bd =4,
        padx =24, pady = 1, width = 6, height = 2, command = delete).grid(row = 1, column = 0, padx = 1)

        self.edit = Button(rightFrame1a, font = ("arial", 12, "bold"), text = " Edit", bd =4,
        padx =24, pady = 1, width = 6, height = 2, command = update).grid(row = 2, column = 0, padx = 1)

        self.edit = Button(rightFrame1a, font = ("arial", 12, "bold"), text = " Search", bd =4,
        padx =24, pady = 1, width = 6, height = 2, command = searchDB).grid(row = 3, column = 0, padx = 1)
        
        self.edit = Button(rightFrame1a, font = ("arial", 12, "bold"), text = "Detail", bd =4,
        padx =24, pady = 1, width = 7, height = 2, command = open_win).grid(row = 4, column = 0, padx = 1)



if __name__ == "__main__":
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()