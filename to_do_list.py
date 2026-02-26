tasks={}
# Add Task

# View Tasks

# Mark Task as Completed

# Delete Task

# Exit

def add_task():
    task=input("enter your task:")
    task_id=len(tasks)+1
    tasks[task_id]=task
    return print(" task added successful ")

def view_task():
    print(tasks)

def mark_task():
    return
def delete_task():
    i=int(input("enter which number of task to be delete: "))
    del tasks[i]
    return print("task deleted successfully")
   

    
while True:
    print("1. add task")
    print("2. view tasks")
    print("3. mark task as completed")
    print("4. delete task")
    print("5. exit")

    user_input=int(input("enter your choice (1/2/3/4/5) :"))
    


    if user_input==1:
        add_task()
    elif user_input==2:
        view_task()
    elif user_input==3:
        mark_task()
    elif user_input==4:
        delete_task()
    elif user_input==5:
        break







