import os

def FileLen():
    if not os.path.exists("List.txt"):
        return 0
    with open("List.txt",) as f:
        lines = f.readlines()
        return len(lines)

def CreateTask():
    f = open("List.txt","at")
    print("<<<<Write>>>>")
    task = input(">>>")
    f.write(f"{task} []\n")
    f.close()


def CompleteTask(length):
    try:
        task = int(input("Enter the task number (If you dont know Read Tasks first.): "))
    except:
        print("Enter proper number.")
        return
    if task > length:
        print("Out of bound tasks.")
        return
    with open("List.txt","r") as fr:
        lines = fr.readlines()
        with open("List.txt","w") as fw:
            for line in lines:
                task -= 1
                if not task:    
                    fw.write(f"{line.replace("[]","[X]")}")
                else:
                    fw.write(line)
        fw.close()
    fr.close()
    return
    

def RemoveTask(length):

    print("Enter the task number you want to remove: (if you dont know first look at task list, Type: exit) \n")
    command = input("Enter command: ")
    if "exit" in command.lower():
        return
    else:
        try:
            number = int(command)
        except:
            print("Invalid entry.")
            pass
        confirm = input(f"Remove task number {number} (Y/n): ")
        if confirm.lower() == "n":
            return
        elif confirm.lower() == "y":
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
        else:
            print("Enter either Y for Yes or n for No.")

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
            return
        confirm = input(f"Update task number {number} (Y/n): ")
        if confirm.lower() == "n":
            return
        elif confirm.lower() == "y":
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
                                fw.write(f"{upTask} []\n")
                            else:
                                fw.write(line)
                    fw.close()
                fr.close()
            else:
                print("Index out of bound.")
        else:
            print("Enter either Y for Yes or n for No.")

def ReadTask():
    with open("List.txt") as f:
        for i, line in enumerate(f):
            print(str(i+1)+") "+line)
    f.close()

def CompletedTasks():
    count = 0
    with open("List.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.endswith("[X]\n"):
                count += 1
                print(f"{count}) {line}")
    f.close()
    if not count:
        print("No Completed Tasks.")
        return
    print(f"Completed Tasks: {count}.")

def RemainingTasks():
    count = 0
    with open("List.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.endswith("[]\n"):
                count += 1
                print(f"{count}) {line}")
    f.close()
    if not count:
        print("No Remaining Tasks.")
        return
    print(f"Remaining Tasks: {count}.")

def Search():
    target = input("Enter the word you wanna search: ")
    count = 0
    with open("List.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            if target.lower() in line.lower():
                count += 1
                print(f"{count}) {line}")
    if not count:
        print("No such word exist.")
        return
    print(f"Total count: {count}.")
    return

def main():

    while True:
        length = FileLen()

        print("="*10+"Choices"+"="*10)
        print("0.Close.")
        print("1.Create Task.")
        print("2.Mark Task Complete.")
        print("3.Remove Task.")
        print("4.Update Task.")
        print("5.Task List.")
        print("6.Tasks Completed.")
        print("7.Tasks Remaining.")
        print("8.Search a word.")
        print("9.Delete All Tasks.")
        print("="*27)

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Please enter the choice number!")
            continue

        if not (os.path.exists("List.txt")):
            with open("List.txt","w") as f:
                f.close()
        match choice:
            case 0:
                break

            case 1:
                CreateTask()

            case 2:
                if length == 0:
                    print("There are no tasks.")
                else:
                    CompleteTask(length)
                
            case 3:
                if length == 0:
                    print("There are no tasks.")
                else:
                    RemoveTask(length)

            case 4:
                if length == 0:
                    print("There are no tasks.")
                else:
                    UpdateTask(length)

            case 5:
                if length == 0:
                    print("There are no tasks.")
                else:
                    ReadTask()

            case 6:
                if length == 0:
                    print("There are no tasks.")
                else:
                    CompletedTasks()

            case 7:
                if length == 0:
                    print("There are no tasks.")
                else:
                    RemainingTasks()

            case 8:
                if length == 0:
                    print("There are no tasks.")
                else:
                    Search()
            case 9:
                os.remove("List.txt")
                

if __name__ == "__main__":
    main()
