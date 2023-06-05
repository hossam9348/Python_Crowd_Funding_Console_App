import ast
print("----------------------------------------> Welcome in our Crowd-Funding stytem <----------------------------------------") #welcome message

flag = input('''to register press 1
to login press 2
--> ''')  

if(flag=='1'):                      #register
    firstName = input("please enter your first name: ")        #take user data with validation
    while len(firstName)<3:
            firstName = input("please enter your first name(at least 3 chracters): ")
    lastName = input("please enter your last name: ")
    while len(lastName)<3:
            lastName = input("please enter your last name(at least 3 chracters): ")
    flag=False      
    email = input("please enter your email: ")          
    file = open('users.txt', 'r')
    for line in file:
      if line != '\n':  
        if ast.literal_eval(line)[2] == email:
           flag=True
    file.seek(0)       
    file.close()       
    while flag or email.count('@') == 0:                 
            flag=False
            email = input("please enter your email(must contain '@' and not exists before): ")  
            file = open('users.txt', 'r')
            for line in file:
              if line != '\n': 
                if ast.literal_eval(line)[2] == email:
                      flag=True
            file.seek(0)
            file.close()          
    password = input("please enter your password: ")
    while len(password)<4:
            password = input("please enter your password(at least 4 chracters): ")
    confirmedPassword = input("please confirm password: ")
    while password != confirmedPassword:
            confirmedPassword = input("please enter a correct password: ")
    phoneNumber = input("please enter phone number: ")
    while len(phoneNumber)!=11 or phoneNumber.isdigit() != True:                 
            phoneNumber = input("please enter your phone number(must be 11 numbers): ")        

    user = []                             #store user data
    user.append(firstName); 
    user.append(lastName); 
    user.append(email); 
    user.append(password); 
    user.append(phoneNumber); 
    file = open('users.txt', 'a')
    file.seek(0)
    file.write(str(user)+'\n')
    file.seek(0)
    file.close()
    print('good job... try to login any time')
elif(flag=='2'):                                      #login and interaction
    loggedInUser = []                                      #login 
    email = input("please enter your email: ")                              
    password = input("please enter your password: ")
    flag=True   
    file = open('users.txt', 'r')
    for line in file:
      if line != '\n': 
        if ast.literal_eval(line)[2] == email and ast.literal_eval(line)[3] == password:
           flag=False
           loggedInUser = ast.literal_eval(line)
    file.seek(0)
    file.close()       
    while flag:                 
            email = input("email or password is wrong..try anthor email... or password: ") 
            password = input("password or email is wrong..try anthor password... or email: ") 
            file = open('users.txt', 'r')
            for line in file:
              if line != '\n':
                if ast.literal_eval(line)[2] == email and ast.literal_eval(line)[3] == password:
                      flag=False
                      loggedInUser = ast.literal_eval(line)
            file.seek(0)
            file.close()        
              
                                                   #interaction
    flag = input('''to create a project press 1
to view all projects press 2
to edit in a project press 3
to delete a project press 4
--> ''')                                  
    if flag == '1':                                    #take project date with validation
     projectTitle = input("please enter your project title: ")        
     while len(projectTitle)<5:
            projectTitle = input("please enter your project title(at least 5 chracters): ")
     projectDetails = input("please enter your project details: ")
     while len(projectDetails)<20:
            projectDetails = input("please enter your project details(at least 20 chracters): ")
     totalTarget = input("please enter your project total target: ")
     while len(totalTarget)<5:
            totalTarget = input("please enter your project total targer(at least 5 chracters... i.e 250 EGP): ")
     startDate = input("please enter your project start date... i.e 01/05/2023: ")
     while len(startDate) != 10:
            startDate = input("please enter your project start date(must be 10 chracters... i.e 01/05/2023): ")
     endDate = input("please enter your project end date... i.e 25/05/2023: ")
     while len(endDate) != 10:
            endDate = input("please enter your project end date(must be 10 chracters... i.e 25/05/2023): ")
    
     project = []                                         #store project date
     project.append(loggedInUser[2]);                         
     project.append(projectTitle); 
     project.append(projectDetails); 
     project.append(totalTarget); 
     project.append(startDate); 
     project.append(endDate); 
     file = open('projects.txt', 'a')
     file.write(str(project)+'\n')
     file.seek(0)
     file.close()
     print('Project was create successfully') 
    elif flag == '2':                      #view all projects
            print('All Projects: ')
            file = open('projects.txt', 'r')
            for line in file:
                print(ast.literal_eval(line))
            file.seek(0)    
            file.close()      
    elif flag == '3':                        #edit in a project
          project = []
          projectName = input("please enter a project name: ")
          file = open('projects.txt', 'r')
          for line in file:
                if ast.literal_eval(line)[0] ==  loggedInUser[2] and ast.literal_eval(line)[1] == projectName:
                     project = ast.literal_eval(line)
          file.seek(0)    
          file.close()

          if len(project) == 0:
               print('Project is not exists... try again')   
               quit()
          print('Project to edit: ')
          print(project)

          projectTitle = input("please enter your new project title: ")        #take  edited project date with validation
          while len(projectTitle)<5:
            projectTitle = input("please enter your new project title(at least 5 chracters): ")
          projectDetails = input("please enter your new project details: ")
          while len(projectDetails)<20:
            projectDetails = input("please enter your new project details(at least 20 chracters): ")
          totalTarget = input("please enter your new project total target: ")
          while len(totalTarget)<5:
            totalTarget = input("please enter your new project total targer(at least 5 chracters... i.e 250 EGP): ")
          startDate = input("please enter your new project start date... i.e 01/05/2023: ")
          while len(startDate) != 10:
            startDate = input("please enter your new project start date(must be 10 chracters... i.e 01/05/2023): ")
          endDate = input("please enter your new project end date... i.e 25/05/2023: ")
          while len(endDate) != 10:
            endDate = input("please enter your new project end date(must be 10 chracters... i.e 25/05/2023): ")
    
          editedProject = []                                  #store edited project date
          editedProject.append(loggedInUser[2]);                         
          editedProject.append(projectTitle); 
          editedProject.append(projectDetails); 
          editedProject.append(totalTarget); 
          editedProject.append(startDate); 
          editedProject.append(endDate); 

          updatedData = []
          file = open('projects.txt', 'r')
          for line in file:
               if project[1] != ast.literal_eval(line)[1]:
                    updatedData.append(line)
               else:
                    updatedData.append(str(editedProject)+'\n')   
          file.seek(0)            
          file.close()
          file = open('projects.txt', 'w')
          data =file.writelines(updatedData)
          file.seek(0)
          file.close()
          #what? functions?   
    elif flag == '4':                      #delete a project
          project = [] 
          projectName = input("please enter a project name: ")
          file = open('projects.txt', 'r')
          for line in file:
                if ast.literal_eval(line)[0] ==  loggedInUser[2] and ast.literal_eval(line)[1] == projectName:
                     project = ast.literal_eval(line)
          file.seek(0)    
          file.close()  

          if len(project) == 0:
               print('Project is not exists... try again')
               quit()


          print('Deleted Project: ')
          print(project)
         
          updatedData = []
          file = open('projects.txt', 'r')
          for line in file:
               if project[1] != ast.literal_eval(line)[1]:
                    updatedData.append(line)
          file.seek(0)          
          file.close()
          file = open('projects.txt', 'w')
          file.writelines(updatedData)
          file.seek(0)
          file.close()
          #what? functions?            
    else:
          print('invalid option... please try again')
else:
    print('invalid option... please try again')




