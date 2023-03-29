import time
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
#New library management system(For newly opened library)

#total books in library

window=tk.Tk()
window.title("Library Management System")

def randomnn(N):
    minimum=pow(10,N-1)
    maximum=pow(10,N)
    return random.randint(minimum,maximum)


#books to be returned
booksinlib=[]
idnli=[]
attendance=[]
issuedbooks=[]
def returnbook(rb):
    booksinlib.append(rb)
#books to be issued
def issuebook(ib):
    issuedbooks.append(ib)
nameli=[]
employee_id_li=[]
phn_numli=[]
dobli=[]
unique_id_li=[]
name_staff_li=[]
dob_staff_li=[]
phn_num_staff_li=[]
max_qualif_staff_li=[]
while True:
#new/existing member
    li=ttk.Label (window,text="Welcome to library!",font=("Arial Bold",10))
    li.grid(column=0,row=0,sticky=tk.W)
    choi=ttk.Label(window,text="Click the option which suits best",width=20)
    choi.grid(column=0,row=1,sticky=tk.W)
    bt=ttk.Button(window,text="New Member",width=20)
    bt.grid(column=0,row=2,sticky=tk.W)
    bt2=ttk.Button(window,text="Existing Member",width=20)
    bt2.grid(column=1,row=2,sticky=tk.W)
    bt3=ttk.Button(window,text="Apply for Job",width=20)
    bt3.grid(column=2,row=2,sticky=tk.W,)
    bt4=ttk.Button(window,text="Staff Member",width=20)
    bt4.grid(column=3,row=2,sticky=tk.W)
    bt5=ttk.Button(window,text="Library rules",width=20)
    bt5.grid(column=4,row=2,sticky=tk.W)
    #print("If you are a member already Enter 1")
    #print("if you are new Enter 2")
    #print("if you want to apply for job Enter 3")
    #print("if you are an employee and mark attendance Enter 4")
    #print("To see library rules Enter 5")
    #for new member
    if bt:
        deta=ttk.Label(window,text="please enter following details to become a member")
        namek=ttk.Label(window,text="Name:")
        namek.grid(column=0,row=4)
        name_var=tk.StringVar
        name=ttk.Entry(window,width=20,textvariable=name_var)
        name.grid(column=1,row=4)
        #name=input("Name: ")
        #dob=input("Date of Birth(DDMMYYYY): ")
        dobk=ttk.Label(window,text="Date of Birth: ")
        dobk.grid(column=0,row=5)
        dob_var=tk.StringVar
        dob=ttk.Entry(window,width=20,textvariable=dob_var)
        dob.grid(column=1,row=5)
        phn_num=input("Phone Number: ")
        nameli.append(name)
        dobli.append(dob)
        phn_numli.append(phn_num)
        unique_id=randomnn(5)
        unique_id_li.append(unique_id)
        print("The membership process is complete, Your unique id is",str(unique_id))
        time.sleep(5)
        #for existing member
    elif bt2:
        print("welcome")
        uni_check=int(input("please enter your unique id: "))
        index1=unique_id_li.index(uni_check)
        print("name=",nameli[index1])
        print("date of birth=",dobli[index1])
        print("enter 1 to issue a book/s")
        print("enter 2 to return book/s")
        print("enter 3 to update information")
        print("enter 4 to cancel membership")
        deed=int(input("Enter action to be performed: "))
        time.sleep(5)
        if deed==1:
            issuen=int(input("enter unique book number: "))
            idn=input("Enter Identity Proof Document Number: ")
            idnli.append(idn)
            issuebook(issuen)#list changed
            curr=time.strftime("Book issued on: %d/%b/%Y")
            print(curr)
            print("Return this book after 1 Month")
            time.sleep(5)
        elif deed==2:
            returnn=int(input("enter unique book number: "))
            returnbook(returnn)#list changed
            curr2=time.strftime("Book issued on: %d/%b/%Y")
            print(curr2)
            time.sleep(5)
        elif deed==3:
            uni=int(input("Please engter unique id: "))
            indexxx=unique_id_li.index(uni) 
            nameli[indexxx]=input("Please enter your name: ")
            dobli[indexxx]=input("please enter your date of birth: ")       
            phn_numli[indexxx]=input("please enter your phone number: ")
            print("information updated successfully")
            time.sleep(5)
        elif deed==4:
            unic=int(input("enter unique id: "))
            xx=unique_id_li.index(unic)
            unique_id_li.remove(unic)
            nameli.remove(nameli[xx])
            dobli.remove(dobli[xx])
            phn_numli.remove(phn_numli[xx])
            print("your membership has been cancelled")
            time.sleep(5)
    elif bt3:
            #to add employee
        print("Hello, Please Enter the details below")
        name_staff=input("Name: ")
        dob_staff=input("Date of Birth(DDMMYYYY): ")
        phn_num_staff=input("Phone Number: ")
        max_qualif_staff=input("Highest Qualification: ")
        employee_id=randomnn(6)
        employee_id_li.append(employee_id)
        name_staff_li.append(name_staff)
        dob_staff_li.append(dob_staff)
        phn_num_staff_li.append(phn_num_staff)
        max_qualif_staff_li.append(max_qualif_staff)
        print("Welcome",name_staff,". You are part of the library staff now! Your Employee id is", employee_id)
        time.sleep(5)
    elif bt4:
            #mark attendance
        emplogin=int(input("please enter employee id to mark attendance: "))
        index2=employee_id_li.index(emplogin)
        print("name=",name_staff_li[index2])
        print("date of birth=",dob_staff_li[index2])
        print("your attendace has been marked")
        attendance.append(emplogin)
        time.sleep(5)
    elif bt5:
        print("1. Keep silence")
        print("2. Don't damahge any property belonging to library")
        print("3. Keep your Mobile Phone on silent")
        print("4. Reference books(Encyclopedias, Handbook, Dictionary) cannot be issued")
        time.sleep(5)