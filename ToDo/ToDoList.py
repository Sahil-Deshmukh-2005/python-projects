import os

def FileLen():
    if not os.path.exists("List.txt"):
        return 0
    with open("List.txt",) as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
        return i

def CreateTask():
    f = open("List.txt","at")
    print("<<<<Write>>>>")
    task = input(">>>")
    f.write(task+"\n")
    f.close()

def RemoveTask(length):

    print("Enter the task number you want to remove: (if you dont know first look at task list, Type: exit) \n")
    command = input("Enter command: ")
    if "exit" in command.lower():
        pass
    else:
        try:
            number = int(command)
        except:
            print("Invalid entry.")
            pass
        if number <= length:
            with open("List.txt") as fr:
                lines = fr.readlines()
                i = 1
                with open("List.txt", "w") as fw:
                    for line in lines:
                        if i != number:
                            fw.write(line)
                        i += 1
                fw.close()
            fr.close()
        else:
            print("Index out of bound.")

def UpdateTask(length):

    print("Enter the task number you want to update: (if you dont know first look at task list, Type: exit) \n")
    command = input("Enter command: ")
    if "exit" in command.lower():
        pass
    else:
        try:
            number = int(command)
        except:
            print("Invalid entry.")
            pass
        if number <= length:
            print("Enter updated task: ")
            upTask = input(">>> ")
            with open("List.txt") as fr:
                lines = fr.readlines()
                i = 0
                with open("List.txt", "w") as fw:
                    for line in lines:
                        i += 1
                        if i == number:
                            fw.write(upTask+"\n")
                        else:
                            fw.write(line)
                fw.close()
            fr.close()
        else:
            print("Index out of bound.")

def ReadTask():
    with open("List.txt") as f:
        for i, line in enumerate(f):
            print(str(i+1)+") "+line)
    f.close()

def main():

    while True:
        length = FileLen()

        print("-"*10+"Choices"+"-"*10)
        print("1.Create Task.")
        print("2.Remove Task.")
        print("3.Update Task.")
        print("4.Task List.")
        print("5.Tasks Remaining.")
        print("6.Delete All Tasks.")
        print("7.Close.")

        choice = int(input("Enter your choice: "))
        if not (os.path.exists("List.txt")):
            with open("List.txt","w") as f:
                f.close()
        match choice:
            case 1:
                CreateTask()
                
            case 2:
                if length == 0:
                    print("There are no tasks.")
                else:
                    RemoveTask(length)

            case 3:
                if length == 0:
                    print("There are no tasks.")
                else:
                    UpdateTask(length)

            case 4:
                if length == 0:
                    print("There are no tasks.")
                else:
                    ReadTask()

            case 5:
                print(length,"tasks remaining.")

            case 6:
                os.remove("List.txt")
            
            case 7:
                break

if __name__ == "__main__":
    main()
