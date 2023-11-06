list_of_activities=[]

def add_an_activity():
    activity=input("enter the name of the activity:").strip()
    list_of_activities.append([activity,"  -  "])
    print("X--          Successfully Added        --X")

def remove_an_activity():
    found=False
    name_of_activity=input("enter the task to be deleted:").strip()
    for activity in list_of_activities:
        if activity[0]==name_of_activity:
            found=True
            list_of_activities.remove(activity)
            print("X--          Successfully deleted        --X")
    if found==False:
        print("X--          No Matches Found          --X")
def activity_completed():
    found=False
    name_of_activity=input("enter the task to be mark as completed:").strip()
    for activity in list_of_activities:
        if activity[0]==name_of_activity:
            found=True
            activity[1]="COMPLETED"
            print("X--          WELL DONE        --X")
    if found==False:
        print("X--          No Matches Found          --X")


def activity_status():


    print("\nTASK                       "+"STATUS")
    for activity,i in zip(list_of_activities,range(1,len(list_of_activities)+1)):
        print(i,".",activity[0],sep="",end="\t\t\t ")
        print(activity[1])
run=True
while(run):
    print("|           ----TO DO LIST----            |")
    print("|           1.ADD AN ACTIVITY             |")
    print("|           2.REMOVE AN ACTIVITY          |")
    print("|           3.VIEW ACTIVITY STATUS        |")
    print("|           4.TASK COMPLETION             |")
    print("|           5.EXIT                        |")

    user_choice=input("enter your choice:")
    if user_choice not in ["1","2","3","4","5"]:
        print("X--          invalid choice          --X")

    elif user_choice=="1":
        add_an_activity()

    elif user_choice=="2":
        remove_an_activity()

    elif user_choice=="3":
        activity_status()

    elif user_choice=="4":
        activity_completed()

    elif user_choice=="5":
        run=False

    print("-"*43)


    
     