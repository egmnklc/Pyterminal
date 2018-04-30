import os,sys,shutil
def terminal():
    answer = input("~VASETERMINAL~: ")
    commands = ["crdir","mkdir","rmdir","cd","ls","clear","cp","ls a"]#All comments will be added here and will be checked if exists or not.
    info_commands = ["info crdir","info mkdir","info rmdir","info cd","info ls","info clear","info ls a"]
    if answer == "":
        print(empty())
#    elif answer.split()[0] and answer.split()[1] == "":
#        print("You didn't type in anything.")
#        print(terminal())
    elif answer.split()[0] == "help":
        print("To get more information about the command, type info (command).\n"  + "\n" + " crdir\n " + "mkdir\n" + " rmdir\n" + " cd\n " + "ls\n " + "clear\n " + "ls a\n") #" cp\n"#)
        print(terminal())
    elif answer == "exit":
        print(exitApp())
    elif answer.split()[0] == "crdir": #Space problem fixed.
        crdir = os.getcwd()
        print(crdir)
        return(terminal())
#       print(currentDir())
    elif answer == "mkdir":
        print("Wrong usage, for more information type info mkdir.")
        print(terminal())
    elif answer == "rmdir":
        print("Wrong usage, for more information, type info rmdir.")
        print(terminal())
    elif answer.split()[0] == "mkdir":
        if answer.split():
            try:
                if os.path.exists(answer.split()[1]) == False:
                    os.mkdir(answer.split()[1])
                    print("File " + answer.split()[1] + " successfully created.")
                    print(terminal())
                if os.path.exists(answer.split()[1]) == True:
                    print("File cannot be created, already exists.")
                    print(terminal())
            except IndexError:
                print("")##DUZELTILDI
        print(terminal())
#        elif os.path.isdir(answer.split()[1]) == False:
#            os.mkdir(answer.split()[1])
#            print("File " + answer.split()[1] + " successfully created.")
#            print(terminal())
#        elif os.path.exists(answer.split()[1]) == True:
#            print("The path " + answer.split()[1] + " already exists.")
#            print(terminal())
#       print(makeDir())
    elif answer == "rmdir":
        print("Wrong usage, for more information type: info rmdir.")
        print(terminal())
    elif answer.split()[0] == "rmdir":
        #print("To cancel, just type c.")
        try:
            if os.path.isdir(answer.split()[1]) == True:
                os.rmdir(answer.split()[1])
                print("File " + answer + " successfully deleted.")
                print(terminal())
            elif answer.split()[1] == "":
                print("wolo")
            elif os.path.isdir(answer.split()[1]) == False:
                print("File " + answer.split()[1] + " does not exists, returning.")
                print(terminal())
        except IndexError:
            print("Illegal usage. Type info rmdir for detailed information")
            print(terminal())
        #elif os.path.isdir()
        #print("To cancel, just type c.")
    elif answer.split()[0] == "ls":
        print(listDir())
    elif answer.split()[0] == "clear":
        print(clearShell())
    elif answer == "cp":
        print(copyFile())
#    elif answer == "sl":
#        print(singleLine())
    elif answer.split()[0] == "info" and (answer.split()[1] == "mkdir"):#info mkdir CHECK
        print(infomakeDir()) 
    elif answer == "info rmdir":#info rmdir CHECK
        print(inforemoveDir())
    elif answer.split()[0] == "info" and answer.split()[1] == "crdir":#info crdir CHECK
        print(infocurrentDir())
    elif answer == "info cd":#info cd
        print(infodirtoCd())
    elif answer == "info ls":#info ls
        print(infolistDir())
    elif answer == "info clear":#info clear
        print(infoclearShell())
    elif answer == "info ls a":#info ls a
        print("Displays current directories in present pathway.")
        print(terminal())
    elif answer == "ls a":
        if (answer.split()[0]) == "ls" and (answer.split()[1] == "a"):
            print(next(os.walk(os.getcwd()))[1])
            print(terminal())
        #print(lsall())
    elif answer == "cd":
        print("Wrong usage, for more information type: info " + answer + " .")
        print(terminal())
    elif answer.split()[0] == "cd":#TRY AND EXCEPT METHODS HAVE ADDED.
        #print("To cancel, just type c.")
        try:
            if os.path.isdir(answer.split()[1]) == True:
                os.chdir(answer.split()[1])
                print("You are currently in " + os.getcwd() + " .")
                print(terminal()) 
            elif os.path.isdir(answer.split()[1]) == False:
                print("Path: " + answer.split()[1] + " does not exists, returning.")
                print(terminal())
        except IndexError:
            print("The following command:" +  answer + " does not exist. Type in help for more information.")
            print(terminal())
        except None:
            print("Illegal Syntax. Type help for more information.")
    else:
        print("Syntax error, for further information type help.")
        print(terminal())
def empty():
        print("You didn't type anything.")
        return terminal() 
def currentDir():
    crdir = os.getcwd()
#    except None:
#        print(currentDir())
    print(crdir)
    return terminal()
def infocurrentDir():
        print("Shows you current directory you are in.")
        return terminal()       
def makeDir():
        print("To cancel, just type c.")
        path = input("A path:")
        if path == "":
            print("Please type in something.")
            print(makeDir())
        elif path == "c":
            print("User brake detected, returning.")
            return terminal()
        elif os.path.exists(path) == True:
            print("The path" + path + " already exists.")
            print(makeDir())
        elif os.path.exists(path) == False:
            os.mkdir(path)
            print("Path: " + path + " created.")
            return terminal()
def infomakeDir():
        print("Creates a directory or a directory path in the path you are currently in.")
        return terminal()        
#def removeDir():
#            print("To cancel, just type c")
#            path = input("A path:")
#            if path == "c":
#                return terminal()
#                print(path)
#                os.rmdir(path)
#                print("Directory sucecsfully deleted.")
#                return terminal()
#            elif path == "":
#                print("Please type in something.")
#                print(removeDir())
#            elif os.path.exists(path) == False:
#                print("There is no such directory called: " + path + " Returning")
#                print(removeDir())
#            elif os.path.exists(path) == True:
#                os.rmdir(path)
#                print("Path: " + path + " is succesfully deleted.")
#            return terminal()
def inforemoveDir():
            print("Deletes an empty directory. Usage: rmdir filetodelete.")
            return terminal()
def infoclearShell():
        print("Clears the shell screen.")
        return terminal()
#def dirtoCd():
#    path0, path1 = input("Enter two numbers here: ")
#    if path0 == "cd":
#        os.chdir(path1)
#        print(os.getcwd())
#        return terminal()
#    elif os.path.exists(path1) == False:
#        print("It's not a dir.")
#        return dirtoCd()
#    elif path == "c":
#        print("User brake detected, returning.")
#        print(terminal())
#    elif path == "":
#        print("You didn't type anything. Please type in something. For help, type help.")
#        print(dirtoCd())
def infodirtoCd():
        print("Takes you into the filepath that you enter.")
        return terminal()
def listDir():
        print(os.listdir())
        return terminal()
def infolistDir():
        print("Shows you the current list of direcrories in the path you are present.")
        return terminal()
def exitApp():
        print("Thanks for using VASE IDE terminal, see you soon.")
        print(sys.exit())
        return terminal()
def clearShell():
        clear = "\n" * 100
        print(clear)
        return terminal()
def copyFile():
        print("To cancel, just type c.")
        path0 = input("Type in the filepath to copy: ")
        path1 = input("Type in the filepath to paste: ")
        if os.path.exists(path0) == True:
            print(path0 + path1)
            shutil.move(path0, path1)
            print("File in " + path0 + " is now present in " + path1)
            return terminal()
        elif path0 == "c":
            print("User brake detected.")
            return terminal()
        elif os.path.exists(path0) == False:
            print("Path " + path0 + " does not exists")
            print(terminal())
#def dirtoCd():
#    if os.path.exists(answer.split()[1]) == True:
#        os.chdir(answer.split()[1])
#        print(os.getcwd())
#    else:
#        print(terminal())
#def lsall():
#    print(os.getcwd())
#    next(os.walk('.'))[1]
print(terminal())
#print(terminal())
#print(os.path.isdir("path"))
