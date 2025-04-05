import os

scenario = "testing 3 different values to check which user this is !"

def input_a_command(scenario):
    os.system("clear")
    while True:
        print(scenario)
        print("\n")
        command = input("q to quit :\n\n")
        os.system("clear")
        if command == "q":
            success = input("Did you successfully solved the described problem? (Y/n)\n").lower()
            if success == "y":
                print("congrats")
            else:
                print("sad :'")
            break
        print()
        os.system(command)
        print()
        print()


input_a_command(scenario)