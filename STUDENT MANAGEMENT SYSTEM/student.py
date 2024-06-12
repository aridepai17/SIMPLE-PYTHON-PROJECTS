import os
import platform

global liststudent
liststudent= []

def managestudent():
    x = "#" * 30
    y = "-" * 28
    global bye
    bye = print("Goodbye!")
    
    
    print(""" 

    --------------------------------------------------------
    |======================================================| 
    |======== Welcome To Student Management System ========|
    |======================================================|
    --------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")
    
    try:
        userinput = int(input("Enter Your Choice : "))
    except ValueError:
        exit("Please Enter Valid Number")
    else:
        print("\n")
        
    if (userinput == 1):
        print("LIST OF STUDENTS\n")
        for students in liststudent:
            print("=> {}".format(students))
            
    elif (userinput == 2):
        newstudent = input("STUDENT TO ADD:")
        print("ADD NEW STUDENT: ")
        if (newstudent in liststudent):
            print("{} is already in the database".format(newstudent))
        else:
            liststudent.append(newstudent)
            print("{} has been added to the database".format(newstudent))
            for students in liststudent:
                print("=> {}".format(students))
                
    elif (userinput == 3):
        srcstudent = input("STUDENT TO SEARCH:")
        if (srcstudent in liststudent):
            print("\n=> Record Found Of Student {}".format(srcstudent))
        else:
            print("\n=> No Record Found Of Student {}".format(srcstudent))
            
    elif (userinput == 4):
        rmvstudent = input("STUDENT TO REMOVE:")
        if (rmvstudent in liststudent):
            liststudent.remove(rmvstudent)
            print("\n=> Record Removed Of Student {}".format(rmvstudent))
            for students in liststudent:
                print("=> {}".format(students))
        else:
            print("\n=> No Record Found Of Student {}".format(rmvstudent))
            
    else:
        print("INVALID CHOICE")
        
managestudent()

def runagain():
    runagn = int(input("Enter 1 to run again or 0 to exit: "))
    if (runagn == 1):
        if(platform.system() == "Windows"):
            print(os.system('cls')) 
        else:
            print(os.system('clear'))
        managestudent()
        runagain()
    else:
        quit(bye) 

runagain()
    