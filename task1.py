
tasks=[]

def addtask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"Task '{task}'added to list.")

def listtasks():
    if not tasks:
        print("no tasks available.")
    else:
        print("current task are:")
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")
def deletetask():
    listtasks()
    try:
        tasktodelete=int(input("Choose the #task to delete:"))
        if tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"task {tasktodelete} has been removed.")
        
        else:
            print(f"Task #{tasktodelete} was not found.")

    except:
        print("Invalid input.")

if __name__ == "__main__":
  print("Welcome to the do list app:)")
while True:
    print("\n")
    print("select one of the following options")
    print("----------------------------------")
    print("1.Add a new task")
    print("2.Delete a task")
    print("3.List tasks")
    print("4.Quit")

    choice=input("enter your choice:")

    if(choice=="1"):
        addtask()
    elif(choice=="2"):
        deletetask()
    elif(choice=="3"):
        listtasks()
    elif(choice=="4"):
        break
    else:
        print("try again later")
print("thank you")