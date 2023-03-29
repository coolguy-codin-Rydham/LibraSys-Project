import time
import random

#New library management system(For newly opened library)
booksinlib=open("booksinlib.txt","r")
booksinlibli=booksinlib.readlines()

idnli=open("idnli.txt","r")
idnlili=idnli.readlines()
idnli=open("idnli.txt","a")

attendance=open("attendance.txt","r")
attendanceli=attendance.readlines()
attendance=open("attendance.txt","a")

dob_staff_li=open("dob_staff_li.txt","r")
dob_staff_li_li=dob_staff_li.readlines()
dob_staff_li=open("dob_staff_li.txt","a")

dobli=open("dobli","r")
doblili=dobli.readlines()
dobli=open("dobli","a")

employee_id_li=open("employee_id_li.txt","r")
employee_id_li_li=employee_id_li.readlines()
employee_id_li=open("employee_id_li.txt","a")

issuedbooks=open("issuesbooks.txt","r")
issuedbooksli=issuedbooks.readlines()
issuedbooks=open("issuesbooks.txt","a")

max_qualif_staff_li=open("max_qualif_staff_li.txt","r")
max_qualif_staff_li_li=max_qualif_staff_li.readlines()
max_qualif_staff_li=open("max_qualif_staff_li.txt","a")

name_staff_li=open("name_staff_li.txt","r")
name_staff_li_li=name_staff_li.readlines()
name_staff_li=open("name_staff_li.txt","a")

nameli=open("nameli.txt","r")
namelili=nameli.readlines()
nameli=open("nameli.txt","a")

phn_num_staff_li=open("phn_num_staff_li.txt","r")
phn_num_staff_li_li=phn_num_staff_li.readlines()
phn_num_staff_li=open("phn_num_staff_li.txt","a")

phn_numli=open("phn_numli","r")
phn_numlili=phn_numli.readlines()
phn_numli=open("phn_numli","a")

unique_id_li=open("unique_if_li.txt","r")
unique_id_li_li=unique_id_li.readlines()
unique_id_li=open("unique_if_li.txt","a")
def randomnn(N):
    minimum=pow(10,N-1)
    maximum=pow(10,N)
    return random.randint(minimum,maximum)

def unicheck():
    uni_check=input("Enter Your Unique Membership ID: ")
    return uni_check

#books to be returned
#allinone={"booksinlib":[],"idnli":[],"attendance":[],"issuedbooks":[],"nameli":[],"employee_id_li":[],"phn_numli":[],"dobli":[],"unique_id_li":[],

#"dob_staff_li":[],"name_staff_li":[],"phn_num_staff_li":[],"max_qualif_staff_li":[]}
def returnbook(rb):
    booksinlib.write(rb)
#books to be issued
def issuebook(ib):
    issuedbooks.write(ib)

while True:
#new/existing member
    print("Welcome to library")
    print("If you are a member already Enter 1")
    print("If you are new Enter 2")
    print("If you want to apply for job Enter 3")
    print("If you are an employee and mark attendance Enter 4")
    print("To see library rules Enter 5")
    print("To Know Books in library Enter 6")
    print("To Exit Enter any number other than 1,2,3,4,5,6")
    mem=int(input("Enter 1/2/3/4/5/6/exit: "))
    time.sleep(1)
    #for new member
    if mem==2:
        print("Please enter following details to become a member")
        name=input("Name: ")
        dob=input("Date of Birth(DD MM YYYY): ")
        phn_num=input("Phone Number: ")
        nameli.write(name)
        namelili.append(name)
        dobli.write(dob)
        doblili.append(dob)
        phn_numli.write(phn_num)
        phn_numlili.append(phn_num)
        unique_id=randomnn(5)
        unique_id_str=str(unique_id)
        unique_id_li.write(unique_id_str)
        unique_id_li_li.append(unique_id)
        print("The membership process is complete, Your unique membership id is",str(unique_id))
        time.sleep(1)
        #for existing member
    elif mem==1:
        print("Welcome")
        
        a=unicheck()
        while a not in unique_id_li_li:
            print("Unique Membership ID you entered was wrong Please Enter Again")
            a=unicheck()
        #else:
        #    continue    
        index1=unique_id_li_li.index(a)
        print("Name=",namelili[index1])
        print("Date of birth=",doblili[index1])
        print("Enter 1 to issue a book/s")
        print("Enter 2 to return book/s")
        print("Enter 3 to update information")
        deed=int(input("Enter action to be performed: "))
        time.sleep(1)
        if deed==1:
            issuen=int(input("enter unique book number: "))
            idn=input("Enter Identity Proof Document Number: ")
            idnli.write(idn)
            issuebook(issuen)#list changed
            curr=time.strftime("Book issued on: %d/%b/%Y")
            print(curr)
            print("Return this book after 1 Month")
            time.sleep(1)
        elif deed==2:
            returnn=int(input("Enter unique book number: "))
            returnbook(returnn)#list changed
            curr2=time.strftime("Book returned on: %d/%b/%Y")
            print(curr2)
            time.sleep(1)
        elif deed==3:
            uni=int(input("Please enter unique membership id: "))
            indexxx=unique_id_li_li.index(uni) 
            namelili[indexxx]=input("Please enter your name: ")
            doblili[indexxx]=input("Please enter your date of birth(DD MM YY): ")       
            phn_numlili[indexxx]=input("Please enter your phone number: ")
            print("Information updated successfully")
            time.sleep(1)
    elif mem==3:
            #to add employee
        print("Hello, Please Enter the details below")
        name_staff=input("Name: ")
        dob_staff=input("Date of Birth(DD MM YY): ")
        phn_num_staff=input("Phone Number: ")
        max_qualif_staff=input("Highest Qualification: ")
        employee_id=randomnn(6)
        employee_id_li.write(employee_id)
        employee_id_li_li.append(employee_id)
        name_staff_li.write(name_staff)
        name_staff_li_li.append(name_staff)
        dob_staff_li.write(dob_staff)
        dob_staff_li_li.append(dob_staff)
        phn_num_staff_li.write(phn_num_staff)
        phn_num_staff_li_li.append(phn_num_staff)
        max_qualif_staff_li.write(max_qualif_staff)
        max_qualif_staff_li_li.append(max_qualif_staff)
        print("Welcome",name_staff,". You are part of the library staff now! Your Employee id is", employee_id)
        time.sleep(1)
    elif mem==4:
            #mark attendance
        emplogin=int(input("please enter employee id to mark attendance: "))
        index2=employee_id_li_li.index(emplogin)
        print("name=",name_staff_li_li[index2])
        print("date of birth=",dob_staff_li_li[index2])
        print("your attendace has been marked")
        attendanceli.append(emplogin)
        time.sleep(1)
    elif mem==5:
        print("1. Keep silence")
        print("2. Don't damahge any property belonging to library")
        print("3. Keep your Mobile Phone on silent")
        print("4. Reference books(Encyclopedias, Handbook, Dictionary) cannot be issued")
        time.sleep(3)
    elif mem==6:
        print(booksinlibli)    
    elif mem>6 or mem<=0:
        print("Exitting")
        time.sleep(1)
        exit()
