list_of_contact=[]

def add_contact(person_name,phone_number):
    list_of_contact.append([person_name,phone_number])
    print("|        SUCCESSFULLY ADDED        |")

def view_contact():
    print("NAME               PHONE NUMBER")
    for member in list_of_contact:
        print(member[0],"  \t\t",member[1])

def delete_contact(person_name):
    found=False
    for member in list_of_contact:
        if member[0]==person_name:
            found=True
            list_of_contact.remove(member)
            print("X--        DELETED SUCCESSFULLY    --X")
    if found==False:
        print("X--  PERSON NOT FOUND IN THE CONTACT BOOK  --X")
def update_contact(person_name):
        found=False
        for member in list_of_contact:
            if member[0]==person_name:
                found=True
                while(1):
                    print("|      1.UPDATE NAME          |")
                    print("|      2.UPDATE PHONE NUMBER  |")
                    print("|      3.EXIT                |")
                    choice=input("enter your choice:")
                    if choice not in ["1","2","3"]:
                        print("X--     INVALID CHOICE     --X")
                        continue
                    elif choice  in ["1","2","3"]:
                        break
                    elif choice=="3":
                        break
               
                if choice=="1":
                    member[0]=input("enter new name:").strip().lower()
                if choice=="2":
                    member[1]=int(input("enter new phone number:").strip())
                print("|        SUCCESSFULLY UPDATED        |")
                break
                
        if found==False:
            print("X--  PERSON NOT FOUND IN THE CONTACT BOOK  --X")
             
        
def search_contact(person_name):
    found=False
    for member in list_of_contact:
        if member[0]==person_name:
            found=True
            print("member founded in the contact book")
            print("NAME: ",member[0],"  \t\t","PHONE NUMBER: ",member[1])   
    if found==False:
        print("X--  PERSON NOT FOUND IN THE CONTACT BOOK  --X")    



print("|          CONTACT BOOK          |")
print("|          1.ADD CONTACT         |")
print("|          2.VIEW CONTACT        |")
print("|          3.DELETE CONTACT      |")
print("|          4.UPDATE CONTACT      |")
print("|          5.SEARCH CONTACT      |")
print("|          5.EXIT                |")
    
run=True
while(run):
    choice=input("enter your choice:")
    if choice not in ["1","2","3","4","5","6"]:
        print("X--     INVALID CHOICE     --X")
        continue
    if choice=="1":
        person_name=input("enter the name of the person  :").lower()
        phone_number=int(input("enter the phone number :"))
        add_contact(person_name,phone_number)
    elif choice=="2":
        view_contact()
    elif choice=="3":
        person_name=input("enter the name of the person  :").lower()
        delete_contact(person_name)
    elif choice=="4":
        person_name=input("enter the name of the person  :").lower()
        update_contact(person_name)
    elif choice=="5":
        person_name=input("enter the name of the person  :").lower()
        search_contact(person_name)
    elif choice=="6":
        print("|     EXITED FROM CONTACT BOOK       |")
        run=False
    print("-"*35)