# First we import datetime.
# datetime is not a data type but a module which is imported.

from datetime import date, datetime


# We used keyword def to define the first function.
# Which is called def reg_user().
# We use the with open statemtents.
# This will open a resource/textfile.
# Guarantee that will be closed when completed.
# Then we create the name we want to open the file as.
# We then create a variable for the user to input the username
# We test/Check the input using a while loop.
# We use while not as it will return the opposite.
# The writelines() will write the items to the file.
# We there call upon our dedicated file name username_password.
# Then write the first line with an escape character next line(\n).
# Then add the new username, seperate it with (', ') and write the password.


def reg_user():
    with open('user.txt','a+') as username_password:

        new_username = input('Please enter new username: \n')
        while new_username in userDic:
            new_username = input('Username already exists:\nPlease enter another username: ')

        new_password = input('Please enter new password: \n')
        confirm_password = input("Please confirm password you just entered: ")
        while confirm_password != new_password:
            confirm_password = input('''Password does not match,
            Please confirm password you just entered: ''')
        
        username_password.writelines('\n')
        username_password.writelines(new_username)
        username_password.writelines(', ')
        username_password.writelines(confirm_password)
    

# We used keyword def to define the first function.
# Which is called def add_task().
# We use the with open statemtents.
# This will open a resource/textfile.
# 'a' for Adding a task 
# if else the user choose's 'a' which is open to admin and any-user
# We also follow the steps of opening a file.
# Then we create a variable for user who will be assigned a task.
# The variables created are title,description and due date.
# We then use datetime for formatting date objects into readable strings
# The strftime() takes one parameter.
# Then we use %d - Day of the month.
# Then we use %b - Month name in short version e.g Jan
# Then we use %Y - Year in full version 2022
# We therefore add the task by at the end using our .formart and writelines().


def add_task():
    with open('tasks.txt','a+') as username_password:
        assigned_username = input('''Please enter,
        Username you would like to assigned task to: ''')
        title_task = input('''Please enter the
        The title of the task: ''')
        description_task = input('''Please enter the
        The description of the task: ''') 
        due_date = input('''Please enter the
        The due date of the task: ''')
        today = date.today()
        strdate = today.strftime("%d %b %Y")
        task_complete = 'No'
        username_password.writelines('\n')
        username_password.writelines(f'{assigned_username}, {title_task}, {description_task}, {strdate}, {due_date}, {task_complete}')
    

# 'va' to View all tasks
# First we open our list in the read format 
# we create a variable called task_items.
# We then create a strip any leading/spaces and tralling  characters 
# Then we split the string into a list (', ')
# We also create a for loop to to execute our statement.
# We create another for loop which calls each index in the task_items
# We print our tasks as indexs using [0][1][2][3][4]
# We use an escape \n to print in a readable formart and use tab to separate.


def view_all():
    
    with open('tasks.txt','r') as username_password:    
        tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
        
        for index in tasks_items:
            print(f'''

The Assigned user is:               {index[0]}\n
The title for the task is:          {index[1]}\n
The task was given on:              {index[3]}\n
The due date is:                    {index[4]}\n
Task Complete:                      {'No'}\n
The description of the task is:     {index[2]}\n''')



# 'vm' to view my task.
# We create a function for our vm.
# Then we create a counter and am open dictionary.
# The counter will count the sequence/itrrable of the objects.
# The dictionary will be used as our container.
# This will store mappings of unique keys to value.
# We open the text file we will be reading from. 
# We create a variable called tasks_items
# We will the remove any leading/trailing space with .strip
# We then split the where we encounter (', ')
# Create a for loop within this will be done for the entire tasks_items.
# for-loop : For each line in task_items
# Then use our counter. 
# Then convert into a disctonary 
# Where the task_disctionary will be our key and the [count_lines] our value.
# We set the dictionary to variable line.
# We therefore have index's which we can call upon. 


def view_mine():
    count_lines = 0
    task_dictionary = {}

    with open('tasks.txt','r+') as username_password:
        
        tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
        
        for line in tasks_items:
            count_lines += 1 
            task_dictionary[count_lines] = line
            if username == line[0]:
        
                print(f'''
Task Number:                        {count_lines}
The Assigned user is:               {line[0]}\n
The title for the task is:          {line[1]}\n
The task was given on:              {line[3]}\n
The due date is:                    {line[4]}\n
Task Complete:                      {'No'}\n
The description of the task is:     {line[2]}\n''')


# Process on how a task is selected.
# We create a variable select_task.
# This will allow the user to select a specfic task or return to main menu.
# We set input to integar that it can only take numbers.
# Create an if statement when user selects -1. 
# This will then return to the main menu.
# We then create a variable called user_choice.
# This will allow the user to either complete or edit a task. 
# We use lower() to return the lowercased from the given string.

    while 1:
        select_task = int(input('''Enter a task number you would like to view or --> 
    Enter -1 to return to the main menu: \n'''))

    
        if select_task == -1:
            return
        
        else:
            user_choice = input('''Please choose what would you like to do on this task,
    Mark task as complete by choosing complete or 
    Edit the task by choosing edit.
    complete - mark as complete
    edit - edit the task
    ''').lower()



            if user_choice == "complete":
                task_dictionary[select_task][-1] = 'Yes'
            
            if task_dictionary[select_task][-1] == 'No' and  user_choice == 'edit':
                edit_choice = input('''Please choose one of the following edits :
    uc - Username Change
    dd - Due Date
    b  - Both\n''').lower()


# We give the user a options once they have chosen edit.
# We create string that the user can choose from.
# The user will be able to edit username, due date or both.
# We select the options by getting into our dictionary.
# We select the correct index and request input from user.

                if edit_choice == 'uc':
                    task_dictionary[select_task][0] = input('Please input new admin: ')
                if edit_choice == 'dd':
                    task_dictionary[select_task][-3]= input("Please enter the new due date:  ")
                if edit_choice == 'b':
                    task_dictionary[select_task][0] = input('Please input new admin: ')
                    task_dictionary[select_task][-3]= input("Please enter the new due date:  ")

        
            else:
                print("You have completed the task hence you can't edit")


# We create a variable for all our tasks.
# We join to take all the elements.
# This will join them into a single string, will return the joined string.

        all_task = '\n'.join([', '.join(t) for t in task_dictionary.values()])
       
        with open('tasks.txt','w') as username_password:
            username_password.write(all_task)



# We then define our task overview.
# We create locoal variables inside the function.
# The variable task_dictionary is our open {} dictionary.
# We create 4 counters, completed, incompleted tasks.
# We create another to count lines and one for tasks overdue.
        
def task_overview():
    task_dictionary = {}
    count_lines = 0
    completed_tasks = 0
    incompleted_tasks = 0
    tasks_overdue = 0
    
# with statements open our file, tast_overview.txt om writing(w)
# We also open task.txt in read mode.

    with open('task_overview.txt','w') as task_overview:
        with open('tasks.txt','r') as username_password:
            tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]


# We use the our control flow statement to execute the statements.
# Firstly we use counter count_lines.
# Counter_lines will keep track hoe many times equivalent values are added.
# This will iterate through our dictionary.
# We use our if stament to then validate whether a condition is true or false.
# We then go to the index's in line to validated the user input.
# Then use our completed task counter.
# else the counter will work for our incompleted tasks.
# To check due date.
# We create a variable called due_date. 
# We assign this variable to the index in our task dictionary.
# We then use our if statement to check if its true or false.

        for line in tasks_items:
            count_lines += 1 
            task_dictionary[count_lines] = line
            if line[-1].lower() == 'yes':
                completed_tasks +=1
            else:
                incompleted_tasks += 1
                
            due_date = task_dictionary[count_lines][4]
            
            if due_date > task_dictionary[count_lines][-3] and task_dictionary[count_lines][-1] == 'No':
                tasks_overdue += 1 
            
        if count_lines > 0:
            incomplete_tasks_percentage = round(((incompleted_tasks/count_lines)*100),2)
            overdue_tasks_percentage = round(((tasks_overdue/count_lines)*100),2)
        

# We the write to the file.
# The write method writes a string to our textfile.
# We use format method.
# This formarts specified values and insert them inside a string.

       
        task_overview.write(f'''The total number of task is {count_lines}
        The total Number of completed tasks are {completed_tasks}
        The total Number of incompleted tasks are {incompleted_tasks}
        The total Numbers of tasks that haven't been completed and are overdue are {tasks_overdue}
        The pecentage of tasks that are incomplete are {incomplete_tasks_percentage}%
        The percentage of the tasks that are overdue are {overdue_tasks_percentage}%\n''')



# We create a function for our user_overview.
# We then create our local variables inside the funtion.
# We then open the textfile we will be reading from.
# We use our for loop to count the admin lines.
# We know our user is index[0] in the list.

def user_overview():
    admin_dictionary = {}
    count_admin_lines = 0
    task_dictionary = {}
    count_lines = 0
  
    with open('user.txt', 'r') as username_password:
        tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
        
        for user in tasks_items:
            count_admin_lines += 1 
            admin_dictionary[count_admin_lines] = user
            # print(each_user(user[0]))
        
    with open('tasks.txt','r') as username_password:
            tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
        
    for line in tasks_items:
        count_lines += 1 
        task_dictionary[count_lines] = line
    
    with open('user_overview.txt','w') as username_password:
        username_password.write(f'''There are {count_admin_lines} users
There are also {count_lines} tasks''')
        username_password.write('\n')
        # username_password.write()
            
    
# We create a function for each user.
# Create local variables we will be using inside our function.

def each_user(specific_user):
    user_total_tasks = 0
    completed_task_percentage = 0
    incompleted_task_percentage = 0
    total_number_of_tasks = 0
    task_completed = 0
    task_dictionary = {}
    task_incomplete = 0
    tasks_overdue = 0
    overdue_task_percentage = 0


# We then open our textfile in read mode.
# We use the for loop to to get the total number of tasks.
# Use our counter to increase by one.
    with open('tasks.txt', 'r') as username_password:
        tasks_items = [tasks_items.strip().split(', ') for tasks_items in username_password]
        for totaltask in tasks_items:
            total_number_of_tasks += 1 
            task_dictionary[total_number_of_tasks] = totaltask
            
# We create a for loop for our task_items.
# We use our index points to call out each task for each user.

        for task in tasks_items:
           
            if task[0] == specific_user:
                
                user_total_tasks += 1
            
                if task[-1].lower() == 'yes':
                    task_completed += 1
                
                else:
                    task_incomplete += 1

                    due_date = task[4]
                    if due_date > task[-3]:
                        tasks_overdue += 1 


        if user_total_tasks != 0:
            completed_task_percentage = round(((task_completed/user_total_tasks)*100),2)
            incompleted_task_percentage = round(((task_incomplete/user_total_tasks)*100),2)
            overdue_task_percentage = round(((tasks_overdue/user_total_tasks)*100),2)


        return f'''The user is {specific_user}
        ==============================
        The total number of tasks are                   {user_total_tasks}
        The number of tasks completed are               {task_completed}
        The number of tasks incomplete are              {task_incomplete}
        The percentage of tasks complete are            {completed_task_percentage}%
        The percentage of tasks incompleted are         {incompleted_task_percentage}%
        The percentage of tasks that are overdue are    {overdue_task_percentage}\n '''
    
            


# Create a function for generate reports.
# We call the task over view and user overview.

def generate_reports():
    task_overview()
    user_overview()
    

# Then we create a variable for our in the dictionary named userDisc.
# We give access to the file user.txt by opening it.
# We open it by calling function with open and input the reading method.
# We use function readlines().
# Which reads all the lines of the text file and returns a list of strings.
# We now introduce our for loop which will execute a group of statements.
# We pass two variables in our for loop.
# User name and password whch will be stored as a dictionary.

userDic = {}

with open('user.txt','r') as username_password:
    data_inside_file = username_password.readlines()

    for item in data_inside_file:
        username, password = item.strip('\n').split(', ')
        userDic[username] = password

# We then create a variable for the user to input the username
# We test/Check the input using a while loop.
# We use while not as it will return the opposite. 
        
username = input('Please enter username: ')
while not username in userDic:
    username = input('Wrong user:\nPlease enter username: ')


# Then we also create a variable for our userpassword for the user to input.
# A while will execute the statements within until its false
# We say while the username is not equal to the password assigned to the Value.
# It will request the user to input a valid password.

userpassword = input("Password: ")
while userDic[username] != userpassword:
    userpassword = input('Wrong Password:\nPlease enter correct Password: ')

# Now we enter into our main program 
# We start off by creating a while loop
# While loop is True it will run without any conditions until the break statements is executed.
# We therefore incorparate our statements.
# Firstly the we use the if statement to check if the user name is admin. 
# else we provide the user with a different menu. 
# The else menu does not have an option to register a user. Only admin can register user.


while True:
    if username == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a User
a - Adding a Task
va - View All Tasks
vm - View My Task
gr = Generate Reports
s - Show Statistics
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()


# 's' to View Statistics
# We proceed with the elif statement
# This will only execute if username is equal to admin.
# We call our generate reports function.
# We open the file as a read format. 
# Create a for loop where each line in our file named username_password

    if menu == 's' and username == 'admin':
        generate_reports()
        with open('user_overview.txt', 'r') as username_password:
            for each_line in username_password:
                print(each_line)
        
        with open('task_overview.txt','r') as username_password:
            for line in username_password:
                print(line)
            

# We therefore call our function from below. 

    if menu == 'r' and username == 'admin':
        reg_user()
        

    elif menu == 'a':
        add_task()
        
    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
        
    elif menu == 'gr':
        generate_reports()
        
    

