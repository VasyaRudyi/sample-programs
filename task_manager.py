import os
from datetime import datetime, date

# create two class type User and Task
DATETIME_STRING_FORMAT = "%Y-%m-%d"

class User():
    '''class User create template which can be used to store the name and it's password and also empty list 
    to store assign task as an objects. '''
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.obj_tasks = []
        
    def get_user(self) -> str:
        z = ""
        for i in self.obj_tasks:
            z = z + f"{i}\n"
        return f"{self.name} {self.password}\n{z}"
        
    def add_user_task(self, object):
        self.obj_tasks.append(object)
    
    def get_obj_tasks(self):
        return self.obj_tasks

    def __str__(self) -> str:
        z = ""
        for i in self.obj_tasks:
            z = z + f"{i}\n"
        return f"{self.name} {self.password}\n{z}"
    
class Task():
    ''' class Task create tamplate which can be used to store the the relevant information. '''
    tCounter = 0
    def __init__(self, title, description, due_date, assign_date = date.today(), complited = "No" ) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assign_date = assign_date
        self.complited = complited
        
    def get_task (self) -> str:
        return f"{self.title} {self.description}"
         
    def __str__(self) -> str:
        return f"{self.title} {self.description} {self.due_date} {self.assign_date} {self.complited}"
    
    def edit_due_date(self):
         while True:
            try:
                task1_due_date = input("Enter your new due date of task (YYYY-MM-DD): ")
                if self.complited == "No":
                    self.due_date = datetime.strptime(task1_due_date, DATETIME_STRING_FORMAT).date()
                else:
                    print ("The task is complited. You can not edit due date.")
                break
            except ValueError:
                print("Invalid datetime format. Please use the format YYYY-MM-DD")
    def edit_complite(self):
        self.complited = "Yes"


def statistic ():
     #The total number of tasks that have been generated and tracked
        t_number = 0
        for i in users_obj_list:
            for y in i.obj_tasks:
                t_number += 1
        tc_number = 0 # total number of completed tasks
        tu_number = 0 # total number of uncompleted tasks
        to_number = 0 # total number of tasks that are overdue
        date_now = date.today()
        u_t_number = 0 # total number of tasks of relevant user
        u_tc_number = 0 # total number of completed tasks of relevant user
        u_tu_number = 0 # total number of uncompleted tasks of relevant user
        u_to_number = 0 # total number of tasks that are overdue
        u_number = len(user_names)
        user_overview = f"     The total number of users registered in the program - {u_number}.\n     The total number of tasks - {t_number}.\n"
        for i in users_obj_list: # in the following code generate the data to form the task_ and user_overview.txt files
            for y in i.obj_tasks:
                u_t_number += 1
                if y.complited == "Yes":
                    u_tc_number += 1
                elif y.complited == "No":
                    u_tu_number += 1
            for z in i.obj_tasks:
                if type(z.due_date) == str:
                    if z.complited == "No" and (date_now > datetime.strptime(z.due_date, DATETIME_STRING_FORMAT).date()):
                        u_to_number += 1
                else:
                    if z.complited == "No" and (date_now > z.due_date):
                        u_to_number += 1
            try:  
                task_rate = round((u_t_number/t_number)*100,2)
                task_complete_rate = round((u_tc_number/u_t_number)*100,2)
                task_uncomplete_rate = round((u_tu_number/u_t_number)*100,2)
                task_overdue_rate = round((u_to_number/u_t_number)*100,2)
            except ZeroDivisionError as e:
                print (f"Error: {e}")
            raw_overview = f'''     {i.name} has {u_t_number} tasks
    The percentage of these tasks is {task_rate}%
    The percentage of completed tasks is {task_complete_rate}%
    The percentage of uncompleted tasks is {task_uncomplete_rate}%
    The percentage of tasks that are overdue is {task_overdue_rate}%\n'''
            tc_number += u_tc_number
            tu_number += u_tu_number
            to_number += u_to_number
            user_overview += raw_overview
            raw_overview = ""             
            u_t_number = 0
            u_tc_number =0
            u_tu_number = 0
            u_to_number = 0
            task_rate = 0
            task_complete_rate = 0
            task_uncomplete_rate = 0
            task_overdue_rate = 0
        try:
            rate_overdue = round((to_number/t_number)*100, 2)
            rate_uncomplite = round((tu_number/t_number)*100, 2)
        except Exception as error:
            print(f"Error: {error}")
        gr_tofile = f'''   The total number of tasks that have been generated is - {t_number}.
    The total number of completed tasks is - {tc_number}.
    The total number of uncompleted tasks is - {tu_number}.
    The total number of tasks that haven't been completed and are overdue - {to_number}.
    The percentage of incomplete tasks - {rate_uncomplite}%.
    The percentage of tasks that are overdue - {rate_overdue}%.'''
        return(gr_tofile, user_overview)
        

def reg_user():
    '''Add a new user to the user.txt file'''
        # - Request input of a new username
        
    new_username = input("New Username: ")
    while new_username in user_names: # loop is used to unable enter identical name.
        print (' '.join(user_names))
        new_username = input("This user name already exist. Enter other name, please: ")

        # - Request input of a new password
    new_password = input("New Password: ")

        # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
            # - If they are the same, add data to the user.txt file after apdating relevant lists
        try:
            user_names.append(new_username)
            user_passwords.append(new_password)
            raw_user = User(new_username, new_password)
            user_list.append(f"{raw_user}")
            users_obj_list.append(raw_user)
        except Exception as e:
            print (f"User did not added, {e}")
        with open("user.txt", 'w') as default_file:
            default_file.writelines(user_list)
        print ("New user added.")
    else:
        print("Passwords do no match\n")
    

def add_task():
    task_title = input("Title of Task: ")
    while task_title.count(" "): # loop that used to force input as a word. (For simplicity))
        task_title = input("Enter title as one word, please: ")
    task_description = input("Description of Task: ")
    while task_description.count(" "):
        task_description = input("Enter description as one word, please: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT).date()
            break
        except ValueError:
            print("Invalid datetime format. Please use the format YYYY-MM-DD")
    raw_task = Task(task_title, task_description, due_date_time) # create an object Task and update relevant lists. After update the tasks.txt file
    task_list.append(f"{raw_task}\n")
    task_obj_list.append(raw_task)
    with open("tasks.txt", "w") as default_file:
        default_file.writelines(task_list)
        
    print ("User names: ", ' '.join(user_names))
    task_username = input("Enter the names to whom the task need to be assigned. Or enter 'all' to assigned the task to all users: ")
    if task_username == "all":
        raw_input = user_names
    else:
        raw_input = task_username.strip().split(" ")
    for i in raw_input: # loop is used to check if entered name is in name list. If not just remind and print its names
        if i not in user_names:
            print(f"User {i} does not exist")
    user_list.clear() # clear user list and rewrite it after updeting relevant objects
    len_u = len(users_obj_list)
    for i in range(len_u):
        for y in raw_input:
            if users_obj_list[i].name == y:
                users_obj_list[i].add_user_task(raw_task)
    for i in range(len_u):
        user_list.append(users_obj_list[i].get_user())
    with open("user.txt", 'w') as f: # write updeted user list in the user.txt file
        f.writelines(user_list)
    print ("New task added.")

def view_all():
    for i, y in enumerate(task_obj_list):
        print(i, "-", y.get_task())

def view_mine():
    for i, y in enumerate(users_obj_list[user_number].get_obj_tasks()): # print all tasks that assigned to [user_number]'s user
        print (i, " - ", y)
    print() # in the following code ask the user to enter the number of task and give some option to adit that task
    while True:
        vm_menu = (input("To select your task enter its number or enter -1 to get to main manu: "))
        if vm_menu == "-1" or vm_menu == -1:
            break
        if not vm_menu.isdigit():
            continue
        vm_menu = int(vm_menu)
        if vm_menu > len(users_obj_list[user_number].obj_tasks)-1:
            continue
        elif users_obj_list[user_number].obj_tasks[vm_menu].complited == "Yes": # if chosen task already marked as completed prompt the user chose other task
            print ("This task is completed. You cannot edit the task.")
            continue
        else:
            print(f"You select: {users_obj_list[user_number].obj_tasks[vm_menu].title}")
            
            s_elect = input('''Enter
    date - to edit due date
    complete - to mark task as complete: ''').lower()
            if s_elect == "date":
                users_obj_list[user_number].obj_tasks[vm_menu].edit_due_date()
                print ("Due date is updated.")
            elif s_elect == "complete":
                users_obj_list[user_number].obj_tasks[vm_menu].edit_complite()
                print ("The task is marked as completed: ", users_obj_list[user_number].obj_tasks[vm_menu])
            else:
                print("Wrong choise. Enter date or complete to edit data in the task")
            user_list.clear() #rewrite the user list and write it in the user.txt file
            for i in users_obj_list:
                user_list.append(i.get_user())
            with open("user.txt", 'w') as f:
                f.writelines(user_list)

#users_ and task_obj_list store relevant objects. During the run of the program they are kept updated
users_obj_list = []
task_obj_list = []
# user_ and task_list are used to write data to the files and back. They are also kept updated befor writing to the files
user_list = []
task_list = []
# user_names and user_passoword keep relevant user names and passwords
user_names = []
user_passwords = []
# t1 and u1 are first objects that are writen to the files (user.txt and tasks.txt)
t1 = Task("Title", "Description", "2024-03-30")
u1 = User("admin", "password")
u1.add_user_task(t1)

user_list.append(f"{u1}")
task_list.append(f"{t1}\n")

        
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.writelines(user_list)
# Read in user_data
with open("user.txt", 'r') as user_file:
    user_list = user_file.readlines()


if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        default_file.writelines(task_list)
with open("tasks.txt", 'r') as task_file:
    task_list = task_file.readlines()
# variable count is used to track the unpacked date from the file (user.txt)
count = 0
for i in user_list:
    if len(i.strip().split(" ")) == 2:
        n,p = i.strip().split(" ")
        user_names.append(n)
        user_passwords.append(p)
        users_obj_list.append(User(n,p))
        count += 1

    elif len(i.strip("\n").split(" ")) == 5:
        q, w, e, r, t = i.strip().split(" ")
        e = datetime.strptime(e, DATETIME_STRING_FORMAT).date()
        r = datetime.strptime(r, DATETIME_STRING_FORMAT).date()
        if users_obj_list[count-1].name == n:
            users_obj_list[count-1].add_user_task(Task(q,w,e,r,t))

for y in task_list:
    q, w, e, r, t = y.strip().split(" ")
    task_obj_list.append(Task(q,w,e,r,t))

print("-"*50)


logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    # user_number (usernumber) is variable to store the sequence number of the user. Is used durint all program and track the user name is lists.
    user_number = 0
    if curr_user not in user_names:
        print("User does not exist")
        continue
    for i,y in enumerate(users_obj_list):
        if curr_user == y.name:
            user_number = i
    curr_pass = input("Password: ")
    if curr_pass != user_passwords[user_number]:
        print("Wrong user password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # make the separated menu option for the admin and users. So only admin can add users and tasks.
    if curr_user == "admin":
    # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following options below:
va - View all tasks
vm - View my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()
        
        
    if (menu == "r"or menu == "a") and user_number != 0: # condition that unable user users accept admin make "r" and "a" choice.
        print ("You are not admin.")
        continue

    if menu == 'r':
        reg_user()
            
    elif menu == 'a':
        add_task()

    elif menu == "va": # in this option use get_task method to retrive the information from list of objects
        print ("All tasks: ")
        view_all()
    
    elif menu == "vm":
        view_mine()

    elif menu == "gr":
        gr_tofile, user_overview = statistic()
        if not os.path.exists("task_overview.txt"):
            with open("task_overview.txt", "w") as default_file:
                default_file.write(gr_tofile)

        with open("task_overview.txt", 'w') as default_file:
            default_file.write(gr_tofile)

        if not os.path.exists("user_overview.txt"):
            with open("user_overview.txt", "w") as default_file:
                default_file.write(user_overview)

        with open("user_overview.txt", 'w') as default_file:
            default_file.write(user_overview)      
    elif menu == "ds":
        gr_tofile, user_overview = statistic()
        date_now1 = date.today()
        print ("="*50)
        print (f"Today is {date_now1}.")   
        print (gr_tofile)
        print ("="*50)
        print (user_overview)   

    elif menu == "e":
        break
    


