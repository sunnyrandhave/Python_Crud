import  json,os
file_name = "DATABASE.json"
empty = {}
if os.path.exists(file_name):    #just to open json file converted into dictionary if exists
    open_file = open("DATABASE.json",'r')
    file_data = open_file.read()
    main_data = json.loads(file_data)
else:
    json_data = json.dumps(empty,indent=5)  #if not exists it will create new file and Manupulate data according to operations performed
    with open(file_name, 'w') as main_data:
        main_data.write(json_data)
    open_file = open("DATABASE.json",'r')
    file_data = open_file.read()
    main_data = json.loads(file_data)

def create():   #Function to Create new user account and add to database(JSON)
    a = True
    while a==True:
        phone = input("please enter Your phone number here->")
        if phone.isnumeric()==True and len(phone)==10 and int(phone)>=0:
            if phone in main_data.keys():
                print("Account With number already Exists")
                a = False
            else:
                new_account = {"name":None,"Mail-id":None,"Password":None,"Phone_Number":phone}
                user_name = input("Please enter Your Name->")
                new_account["name"]=user_name
                while True:
                    user_mail = input("please enter your Mail id->").lower()
                    temp = user_mail.split("@")
                    if temp[-1]=="gmail.com":
                            new_account["Mail-id"] = user_mail
                            break
                    else:
                        print ("please Enter Valid Email Mail")
                while True:
                    sp_char = 0 
                    Up_char = 0
                    sm_char = 0
                    nm = 0
                    user_password = input("please Enter New Password->")
                    for i in user_password:
                        if 48<=ord(i)<=57:
                            nm = 1 
                        elif 65<=ord(i)<=90:
                            Up_char =1 
                        elif 97<= ord(i) <=122:
                             sm_char = 1 
                        else:
                            sp_char = 1 
                    if sp_char and Up_char and sm_char and nm:   
                        new_account['Password']=user_password
                        main_data[phone] = new_account
                        with open("DATABASE.json", 'w') as json_file:
                            json.dump(main_data, json_file, indent=4)
                        print("Account Created SuccessFully")
                        a = False
                        break
                    else:
                        print("Please Enter Valid Strong Password")
        else:
            print("please Enter valid phone number")

def Read():      #Function to Read existing User Data using user id and Password
    a = True
    while a==True:
        phone = (input("Please Enter your Phone Number->"))  
        if phone.isnumeric()==True and len(phone)==10:
            if phone in main_data.keys():
                while True:
                    password = input("Please Enter Your Account Password->\n")
                    if password==main_data[phone]["Password"]:
                        print(main_data[phone])
                        a = False
                        break                        
                    else:
                        print("Wrong Password Please try again")
            else:
                print("Sorry No account Exists with these number")  
                a = False     
        else:
            print("please Enter Valid phone Number->")

def update():        #Function to manipulate Existing User Data with use of User ID and Password
    a = True
    while a==True:        
        phone = (input("Please Enter your Phone Number\n->"))
        if phone.isnumeric()==True and len(phone)==10:
            if phone in main_data.keys():
                c = True
                while c==True:
                    password = input("Please Enter Your Account Password->")
                    if password==main_data[phone]["Password"]:
                        print("What do You Wanna Update?")
                        xyz = True
                        while xyz==True:
                            print("1:-number\n2:-Name\n3:-Mail-id\n4:-password")
                            action = (input("enter Here:-"))
                            if action=='1':
                                new_number = (input("Enter Here Your New Number->"))
                                if new_number in main_data.keys():
                                    print("Sorry Account Already exists With this Number")
                                else:
                                    main_data[phone]["Phone_Number"] = new_number
                                    main_data[new_number]=main_data[phone]
                                    print("Your Phone Number is Changed")
                                    del main_data[phone]
                                a = False
                                xyz = False
                                c = False
                            elif action=='2':
                                new_name = input("Enter New Name->")
                                main_data[phone]["name"]=new_name
                                print("Your Name has been Changed")
                                c = False
                                a = False
                                break
                            elif action=='3':
                                b = True
                                while b==True:
                                    new_mail = input("enter Your New Mail Id->").lower()
                                    temp = new_mail.split("@")
                                    if temp[-1]=="gmail.com":
                                        main_data[phone]["Mail-id"] = new_mail
                                        print("Your Mail-Id has been updated")
                                        b = False
                                    else:
                                        print("please Enter Valid Email Mail")
                                a = False
                                c = False
                            elif action=='4':
                                while True:
                                    sp_char = 0 
                                    Up_char = 0
                                    sm_char = 0
                                    nm = 0
                                    user_password = input("please Enter New Password->")
                                    for i in user_password:
                                        if 48<=ord(i)<=57:
                                            nm = 1 
                                        elif 65<=ord(i)<=90:
                                            Up_char =1 
                                        elif 97<= ord(i) <=122:
                                            sm_char = 1 
                                        else:
                                            sp_char = 1 
                                    if sp_char and Up_char and sm_char and nm:   
                                        # new_account['Password']=user_password
                                        main_data[phone]["Password"] = user_password
                                        with open("DATABASE.json", 'w') as json_file:
                                            json.dump(main_data, json_file, indent=4)
                                            print("Password Updated SuccessFully")
                                        xyz = False
                                        a = False
                                        c = False
                                        break
                                    else:
                                        print("Please Enter Valid Strong Password")
                                c = False
                                a = False
                            else:
                                print("Invalid Input")
                                # a = False
                                # break
                    else:
                        print("Wrong Password Please try again")
            else:
                print("Sorry No account Exists with these number")  
                a = False
        else:
            print("please Enter Valid phone Number\n->")
            # a = False
        json_data = json.dumps(main_data,indent=5)
        with open("DATABASE.json",'w') as file:
            file.write(json_data)

def Delete():        #Function to delete specific account from whole database
    a = True
    while a==True:
        phone = (input("Please Enter your Phone Number\n->"))
        if phone.isnumeric()==True and len(phone)==10:
            if phone in main_data.keys():
                while True:
                    password = input("Please Enter Your Account Password->\n")
                    if password==main_data[phone]["Password"]:
                        del main_data[phone]
                        print("Account deleted From Database")
                        a = False
                        break                        
                    else:
                        print("Wrong Password Please try again")
            else:
                print("Sorry No account Exists with these number")  
                a = False     
        else:
            print("please Enter Valid phone Number->")
    json_data = json.dumps(main_data,indent=5)
    with open("DATABASE.json",'w') as file:
        file.write(json_data)

def Database():       #Function to See whole Json File converted into python dictionary
    while True:
        password = input("Please Enter Admin Password->")
        if password=="Sam@randhave1":
            print(main_data)
            break
        else:
            print("Wrong Password! Permission Denied")
            break


#Function to Call all the Functions Specaifically made for operation
print("Welcome to CRUD with JSON")
while True:
    print("\n1.Create","\n2.Read","\n3.Update","\n4.Delete\n5.Exit the Program\n6.Open Database(Admin)\n")
    operation = (input("Which operation do You wanna Perform?\n:->"))
    if operation=="1":
        create()
    elif operation=="2":
        Read()
    elif operation=="3":
        update()
    elif operation=="4":
        Delete()
    elif operation=='5':
        print("Sorry To See You Go!")
        break
    elif operation=="6":
        Database()
    else:
        print("Please Enter Valid Input")
        continue


