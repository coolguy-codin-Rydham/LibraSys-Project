import time
import random
# library management system

#total books in library
def randomnn(N):
    minimum=pow(10,N-1)
    maximum=pow(10,N)
    return random.randint(minimum,maximum)


#books to be returned
booksinlib=[]
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
    
    print("If you are a member Enter 1")
    print("if you are new Enter 2")
    print("if you want to apply for job Enter 3")
    print("if you are an employee Enter 4")
    mem=int(input("Enter 1/2/3/4: "))
    #for new member
    if mem==2:
        print("please enter following details to become a member")
        name=input("Name: ")
        dob=input("Date of Birth(DDMMYYYY): ")
        phn_num=input("Phone Number: ")
        nameli.append(name)
        dobli.append(dob)
        phn_numli.append(phn_num)
        unique_id=randomnn(5)
        unique_id_li.append(unique_id)
        print("The membership process is complete, Your unique id is",str(unique_id))
    #for existing member
    elif mem==1:
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
        if deed==1:
            issuen=int(input("enter unique book number: "))
            issuebook(issuen)#list changed
            curr=time.strftime("Book issued on: %d/%b/%Y")
            print(curr)
            print("Return this book after 1 Month")
        elif deed==2:
            returnn=int(input("enter unique book number: "))
            returnbook(returnn)#list changed
            curr2=time.strftime("Book issued on: %d/%b/%Y")
            print(curr2)
        elif deed==3:
            uni=int(input("Please engter unique id: "))
            indexxx=unique_id_li.index(uni) 
            nameli[indexxx]=input("Please enter your name: ")
            dobli[indexxx]=input("please enter your date of birth: ")       
            phn_numli[indexxx]=input("please enter your phone number: ")
            print("information updated successfully")
        elif deed==4:
            unic=int(input("enter unique id: "))
            xx=unique_id_li.index(unic)
            unique_id_li.remove(unic)
            nameli.remove(nameli[xx])
            dobli.remove(dobli[xx])
            phn_numli.remove(phn_numli[xx])
            print("your membership has been cancelled")
    elif mem==3:
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



                
