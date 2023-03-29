import time
import random
#New library management system(For newly opened library)

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
    print("Welcome to library")
    print("If you are a member already Enter 1")
    print("If you are new Enter 2")
    print("If you want to apply for job Enter 3")
    print("If you are an employee and mark attendance Enter 4")
    print("To see library rules Enter 5")
    mem=int(input("Enter 1/2/3/4/5: "))
    time.sleep(3)
    #for new member
    if mem==2:
        print("Please enter following details to become a member")
        name=input("Name: ")
        dob=input("Date of Birth(DDMMYYYY): ")
        phn_num=input("Phone Number: ")
        nameli.append(name)
        dobli.append(dob)
        phn_numli.append(phn_num)
        unique_id=randomnn(5)
        unique_id_li.append(unique_id)
        print("The membership process is complete, Your unique membership id is",str(unique_id))
        time.sleep(3)
        #for existing member
    elif mem==1:
        print("Welcome")
        uni_check=int(input("Please enter your unique membership id: "))
        if uni_check not in unique_id_li:
            exit("Invalid Unique membership ID entered")
        index1=unique_id_li.index(uni_check)
        print("Name=",nameli[index1])
        print("Date of birth=",dobli[index1])
        print("Enter 1 to issue a book/s")
        print("Enter 2 to return book/s")
        print("Enter 3 to update information")
        print("Enter 4 to cancel membership")
        deed=int(input("Enter action to be performed: "))
        time.sleep(3)
        if deed==1:
            issuen=int(input("enter unique book number: "))
            idn=input("Enter Identity Proof Document Number: ")
            idnli.append(idn)
            issuebook(issuen)#list changed
            curr=time.strftime("Book issued on: %d/%b/%Y")
            print(curr)
            print("Return this book after 1 Month")
            time.sleep(3)
        elif deed==2:
            returnn=int(input("Enter unique book number: "))
            returnbook(returnn)#list changed
            curr2=time.strftime("Book returned on: %d/%b/%Y")
            print(curr2)
            time.sleep(3)
        elif deed==3:
            uni=int(input("Please enter unique membership id: "))
            indexxx=unique_id_li.index(uni) 
            nameli[indexxx]=input("Please enter your name: ")
            dobli[indexxx]=input("Please enter your date of birth: ")       
            phn_numli[indexxx]=input("Please enter your phone number: ")
            print("Information updated successfully")
            time.sleep(3)
        elif deed==4:
            unic=int(input("enter unique membership id: "))
            xx=unique_id_li.index(unic)
            unique_id_li.remove(unic)
            nameli.remove(nameli[xx])
            dobli.remove(dobli[xx])
            phn_numli.remove(phn_numli[xx])
            print("your membership has been cancelled")
            time.sleep(3)
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
        time.sleep(3)
    elif mem==4:
            #mark attendance
        emplogin=int(input("please enter employee id to mark attendance: "))
        index2=employee_id_li.index(emplogin)
        print("name=",name_staff_li[index2])
        print("date of birth=",dob_staff_li[index2])
        print("your attendace has been marked")
        attendance.append(emplogin)
        time.sleep(3)
    elif mem==5:
        print("1. Keep silence")
        print("2. Don't damahge any property belonging to library")
        print("3. Keep your Mobile Phone on silent")
        print("4. Reference books(Encyclopedias, Handbook, Dictionary) cannot be issued")
        time.sleep(3)