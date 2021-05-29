import sys
import time
import os
import setup
import homescreen
import cooker
import profile_manager

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def bypass():
    bypass = input("The install verification file failed. do you want to install the program, or do you want to pass? \n type [1] to pass and launch the program, type [2] to reinstall \n")

    if bypass == "1":
        homescreen.welcome()
    elif bypass == "2":
        setup.setup()
    else:
        print("input error. stoping...")
        time.sleep(1)
        sys.exit()

def install_checker():
    setup_file = open('setup.txt', 'r')
    true_strings = ['setup completion =\n', ' true\n', ' Version 0.1']
    false_strings = ['setup completion = false \n', '\n', ' Version 0.1']

    lines = setup_file.readline()

    def readline(lines):
        if lines in true_strings:
            return True
        if lines in false_strings:
            return False
        else:
            return "err"

    with open('setup.txt', 'r') as setup_file:
        for lines in setup_file:
            if readline(lines) == True:
                print('installed. launching...')
                welcome()
                usr_input()
                break
            elif readline(lines) == False:
                print('not installed. installing...')
                setup.setup()
                break
            else:
                pass

    setup_file.close()

def welcome():
    account_file = open("Account.txt","r")
    account_file_read = account_file.readlines()
    account_name = account_file_read[1]
    full_name = account_file_read[2:3]
    first_name = account_file_read[2]
    last_name = account_file_read[3]
    email = account_file_read[4]

    print("logging into account",account_name,"...")
    time.sleep(0.5)
    buffering()
    print("----------------------------------------------------")
    print("Welcome",first_name)
    print("loaded v0.1")
    account_file.close()

def buffering():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

def usr_input():

    def cooker_handler():
        cooker.main()

    def profile_handler():
        profile_manager.profile_list()

    def settings_handler():
        print("to profile file")

    print("what do you want to do?")
    question = input(" \n type [1] to cook, \n type [2] to view/edit your profiles, \n type [3] to edit your settings. \n \n $")

    handlers = {
        '1': cooker_handler,
        '2': profile_handler,
        '3': settings_handler
    }

    if question in handlers:
        handlers[question]()
    else:
        print("Unknown choice", question)




path = os.getcwd()
name = "setup.txt"

for root, dirs, files in os.walk(path):
    if name in files:
        install_checker()
        break
    else:
        setup.setup()
        break

