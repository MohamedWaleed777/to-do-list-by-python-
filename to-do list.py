print("LIGHTNING MCQUEEN'S TO-DO LIST")
print("")
print("       HELLO CHAMP! ")
print("   THERE IS YOUR TO-DO LIST")
print("")

tasks=[]# list to put the tasks in it 

def add_tasks():# func to add tasks
    TaskName = input("Enter task name : ")    
    task={
        "name":TaskName,
        "status" : False 
        }
    tasks.append(task) 
    print("")
    print("Task added successfully")
     
    
def view_list():# func for show tasks
    print("   Your to do list:")
    for i in range (len(tasks)):
        if tasks[i]["status"]:
            status ="   Done"
        else:
            status="   Pending"
        print(f"{i+1} - {tasks[i]['name']} {status}" )
    print("")    


def mark():#func to mark tasks 
    for i in range (len(tasks)):
        if tasks[i]["status"]:
                    status ="   Done"
        else:
                    status="   Pending"
        print (f"{i+1} - {tasks[i]['name'] } {status}")
    num=int(input("Enter Task Number ")) # to get the number not string 
    print("")
    if 1<= num <=len(tasks):
        tasks[(num-1)]["status"]=True
        print("Task is completed!  Keep going champ!")
        print("")
    else:
        print("Enter the correct number ")


def remove():# #func to removes tasks 
    for i in range (len(tasks)):
            if tasks[i]["status"]:
                                status ="   Done"
            else:
                                status="   Pending"
            print (f"{i+1} - {tasks[i]['name'] } {status}")

    num=int(input("Enter Task Number To Be Removed : " ))# to get the number not string 
    print("")
    if 1<= num <=len(tasks):
        del tasks[num-1]
        print("Removed ")
        print("")
    else:
         print("Enter the correct number")

import json
def SaveTasks(): # to save the to do list
      file =open ("tasks.json","w") 
      json.dump(tasks,file) # writes list in file 
      file.close()



while True :
    print ("1. Add a task")
    print ("2. View my to-do list")
    print ("3. Mark a task as done")
    print ("4. Remove a task")
    print ("5. Quit")
    choice =input ("Enter your choice: ")
    if choice=="1":
        add_tasks()
    elif choice=="2":
        view_list()
    elif choice=="3":
        mark()
    elif choice=="4":
        remove()
    elif choice== "5":
        SaveTasks()
        print("")
        print("Bye Bye LIGHTNING MCQUEEN ")
        print("")
        break;
    else : # as the wrong choice will make infinte loop
        print("")
        print("Enter valid number ")
        print("")
    