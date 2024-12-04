import time
import random
import os

for i in range(1, 4):
    time.sleep(1)
    os.system('cls')
    print("loading", "."*i)

print("***FILE MANAGING SYSTEM***")
diretory = "C:/System/System32/Windows"
file_list = ["Pookie", "Windows", "Cats", "Gotterdammerung"]
command_list = ["remove", "move", "add"]
available_files = ["hoi4", "roblox", "cs2", "adobepremier", "davinciresolve"]

while True: 
    print("Select a target File")
    Target = input(f"{diretory}: ")
    if Target == "showlist":
        os.system('cls')
        print(file_list)
    elif Target not in file_list:
        print("Error 404, Cant find the requested file")
    else:
        Command = input("Command: ")
        if Command not in command_list:
            print("Error, unknown command")
        else:
            if Command == "remove":
                file_list.remove(Target)
                os.system('cls')
                print(f"{Target}, has been successfully removed!")
            elif Command == "move":
                file_list.reverse
                os.system('cls')
                print("The list has been moved!")
            else: 
                new_file = random.choice(available_files)
                file_list.append(new_file)
                os.system('cls')
                print(f"A new file named {new_file} has been successfully added to the list!")

