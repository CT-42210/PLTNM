import sys
import time
import os

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def instalation_check():
    setup_file = open("setup.txt", "w")
    setup_file.write("setup completion = false \n")
    setup_file.write("\n Version 0.1")
    setup_file.close()

def log_creation():
    setup_log = open("setup_log.txt", "w")
    setup_log.write("logging setup at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()


def directory_setup():
    directory = "Profiles"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    directory_setup_complete()


def directory_setup_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("directory created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def profiles_file_setup():
    parent_dir = os.getcwd()
    created_dir = r"\Profiles"
    script_dir = parent_dir + created_dir
    profiles_path = os.path.join(script_dir, "Profiles.txt")

    profiles_file = open(profiles_path, "w")
    profiles_file.write("file test")
    profiles_file.close()

    profiles_file = open(profiles_path)
    content = profiles_file.read()

    if content == ("file test"):
        profiles_file.close()
        print("profiles file created succesfuly")
        profiles_file = open(profiles_path, "w")
        profiles_file.write("Profiles:\n")
        profiles_file.close()
        profiles_file_complete()
    else:
        profiles_setup_err()


def profiles_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("assignment text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def profiles_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("profiles text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    profiles_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass

def account_file_setup():
    account_file = open("Account.txt", "w")
    account_file.write("file test")
    account_file.close()

    account_file = open("Account.txt")
    content = account_file.read()

    if content == ("file test"):
        account_file.close()
        print("Account file created succesfuly")
        account_file = open("Account.txt", "w")
        account_file.write("Account:\n")
        account_file.close()
        account_file_complete()
    else:
        account_setup_err()


def account_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("account text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def account_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("account text file creation failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    account_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass

def settings_file_setup():
    settings_file = open("Settings.txt", "w")
    settings_file.write("file test")
    settings_file.close()

    settings_file = open("Settings.txt")
    content = settings_file.read()

    if content == ("file test"):
        settings_file.close()
        print("Settings file created succesfuly")
        settings_file = open("Settings.txt", "w")
        settings_file.write("Settings:\n")
        settings_file.close()
        settings_file_defaults()
    else:
        settings_setup_err()


def settings_file_defaults():
    settings_file = open("Settings.txt","a")
    settings_file.write("\n order of homescreen print: \n")
    settings_file.write("assignments \n")
    settings_file.write("checklists \n ")
    settings_file.write("custom text \n")
    settings_file.write("\n Custom Text: \n")
    settings_file.write("you have no custom text!")
    settings_file.close()

    settings_file_complete()

def settings_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("settings text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def settings_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("settings text file creation failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = 0
    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    settings_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass

def account_creation():
    print("Welcome! please create your account below.\n If you wish to start over, type [restart]. \n ")

    time.sleep(1)

    username = "enter the account username: \n $ "
    first_name = "enter your first name: \n $ "
    last_name = "enter your last name: \n $ "
    email = "enter an email. (this is optional.) \n $ "

    account_file = open("Account.txt", "w")
    account_file.write("Account:\n")
    account_file.write(input(str(username)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(first_name)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(last_name)))
    account_file.write("\n")
    time.sleep(1)
    account_file.write(input(str(email)))
    account_file.write("\n")
    time.sleep(1)
    account_file.close()

    print("are these cridentials correct? \n")
    account_file = open("Account.txt","r")
    confirmation = account_file.read()

    print(confirmation)

    if input(str("type [y] if they are correct, and [n] if they are not.")) == "y":
        account_file.close()

        setup_log = open("setup_log.txt", "a")
        setup_log.write("account set up sucessfuly at:")
        setup_log.write(current_time)
        setup_log.write("\n check [Account.txt] for cridentals. \n")
        setup_log.close()
    elif input == "n":
        setup_log = open("setup_log.txt", "a")
        setup_log.write("account set up restarted at:")
        setup_log.write(current_time)
        setup_log.write("\n credentials are as follows: \n", )
        setup_log.write(confirmation, )
        setup_log.write("\n")
        setup_log.close()
    else:
        print("invalid response,starting again...")
        time.sleep(3)
        account_creation()


def setup():
    instalation_check()
    log_creation()
    directory_setup()
    profiles_file_setup()
    settings_file_setup()
    account_file_setup()
    account_creation()

    setup_file = open("setup.txt","w")
    setup_file.write("setup completion = \n true")
    setup_file.write("\n Version 0.1")
    print("setup complete! please restart for the full aplication.")
    time.sleep(5)
