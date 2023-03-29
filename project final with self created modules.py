import time
import random

#Library management system(For newly opened library)
fh=open("Dictionery.txt","r")
li=fh.readlines()
strallinone=li[0]
allinone=eval(strallinone)

def randomnn(N):
    minimum=pow(10,N-1)
    maximum=pow(10,N)
    return random.randint(minimum,maximum)

def unicheck():
    uni_check=int(input("Enter Your Unique Membership ID: "))
    return uni_check

#books to be returned
# allinone={"booksinlib":[],"idnli":[],"attendance":[],"issuedbooks":[],"nameli":[],"employee_id_li":[],"phn_numli":[],"dobli":[],"unique_id_li":[],
# "dob_staff_li":[],"name_staff_li":[],"phn_num_staff_li":[],"max_qualif_staff_li":[]}

def returnbook(rb):
    allinone["booksinlib"].append(rb)
#books to be issued

def issuebook(ib):
    allinone["issuedbooks"].append(ib)

while True:
#new/existing member

    print("Welcome to Library")
    print("If you are already a member Enter 1")
    print("If you are new Enter 2")
    print("If you want to apply for job Enter 3")
    print("If you are an employee and mark attendance Enter 4")
    print("To see Library rules Enter 5")
    print("To Exit Enter any number other than 1,2,3,4,5")
    member=int(input("Enter 1/2/3/4/5/Exit: "))
    time.sleep(1)
    #for new member

    if member==2:
        print("Please enter following details to become a member")
        name=input("Name: ")
        dob=input("Date of Birth(DD MM YYYY): ")
        phn_num=input("Phone Number: ")
        allinone["nameli"].append(name)
        allinone["dobli"].append(dob)
        allinone["phn_numli"].append(phn_num)
        unique_id=randomnn(5)
        while unique_id in allinone["unique_id_li"]:
            unique_id=randomnn(5)
        allinone["unique_id_li"].append(unique_id)
        print("The membership process is complete, Your Unique Membership id is",str(unique_id))
        time.sleep(1)
        #for existing member

    elif member==1:
        print("Welcome")
        
        a=unicheck()
        if a not in allinone["unique_id_li"]:
            print("Unique Membership ID you entered was wrong Please Enter Again")
            a=unicheck()    
        index1=allinone["unique_id_li"].index(a)
        print("Name=",allinone["nameli"][index1])                                      
        print("Date of birth=",allinone["dobli"][index1])
        print("Enter 1 to issue a book/s")
        print("Enter 2 to return book/s")
        print("Enter 3 to update information")
        print("Enter 4 to cancel membership")
        deed=int(input("Enter action to be performed: "))
        time.sleep(1)
        
        if deed==1:
            issuen=int(input("Enter unique book number: "))
            idn=input("Enter ID Proof Number: ")
            allinone["idnli"].append(idn)
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
            indexxx=allinone["unique_id_li"].index(uni) 
            allinone["nameli"][indexxx]=input("Please enter your name: ")
            allinone["dobli"][indexxx]=input("Please enter your date of birth(DD MM YY): ")       
            allinone["phn_numli"][indexxx]=input("Please enter your phone number: ")
            print("Information updated successfully")
            time.sleep(1)
        
        elif deed==4:
            unic=int(input("enter unique membership id: "))
            xx=allinone["unique_id_li"].index(unic)
            allinone["unique_id_li"].remove(unic)
            allinone["nameli"].remove(allinone["nameli"][xx])
            allinone["dobli"].remove(allinone["dobli"][xx])
            allinone["phn_numli"].remove(allinone["phn_numli"][xx])
            print("your membership has been cancelled")
            time.sleep(1)
    
    elif member==3:
            #to add employee
        print("Hello, Please Enter the details below")
        name_staff=input("Name: ")
        dob_staff=input("Date of Birth(DD MM YY): ")
        phn_num_staff=input("Phone Number: ")
        max_qualif_staff=input("Highest Qualification: ")
        employee_id=randomnn(6)
        allinone["employee_id_li"].append(employee_id)
        allinone["name_staff_li"].append(name_staff)
        allinone["dob_staff_li"].append(dob_staff)
        allinone["phn_num_staff_li"].append(phn_num_staff)
        allinone["max_qualif_staff_li"].append(max_qualif_staff)
        print("Welcome",name_staff,". You are part of the library staff now! Your Employee id is", employee_id)
        time.sleep(1)
    
    elif member==4:
            #mark attendance
        emplogin=int(input("please enter employee id to mark attendance: "))
        index2=allinone["employee_id_li"].index(emplogin)
        # print("name=",allinone["name_staff_li"][index2])
        # print("date of birth=",allinone["dob_staff_li"][index2])
        print("your attendace has been marked:", allinone["name_staff_li"][index2])
        allinone["attendance"].append(emplogin)
        time.sleep(1)
    
    elif member==5:
        print("1. Keep Quiet")
        print("2. Don't damage any property belonging to library")
        print("3. Keep your Mobile Phone on silent")
        print("4. Reference books(Encyclopedias, Handbook, Dictionary) cannot be issued")
        time.sleep(3)
    
    elif member>=6 or member<=0:
        fh2=open("Dictionery.txt","w")
        fh2.write("%s"%(allinone))
        fh2=open("Dictionery.txt","r")
        print("Project By:")
        print("2210990751 Rydhampreet Singh Gindra")
        print("2210990749 Rupesh Singla")
        print("2210990783 Sanchit Prashar")
        time.sleep(1)
        print("Exiting")
        time.sleep(2)
        exit("Thank you for using our Library Management System!")
    