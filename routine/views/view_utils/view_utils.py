import os

def prompt_scenario(scenario):
    print(scenario)
    print("\n")

def execute_command(command):
    print()
    os.system(command)
    print()
    print()

def prompt_command_list(command_list):
    for i in command_list:
        print(i)
    print()