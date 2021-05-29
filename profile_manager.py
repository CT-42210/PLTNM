import os
import easter_eggs

def profile_list():
    parent_dir = os.getcwd()
    created_dir = r"\Profiles"
    script_dir = parent_dir + created_dir
    checklist_path = os.path.join(script_dir, "Profiles.txt")

    try:
        checklist_file = open(checklist_path, "r")
        profile_list = checklist_file.read()
        print(profile_list)
        user_input()
    except IndexError:
        print("err")

def user_input():

    def edit_handler():
        profile_editor()
    def exec_handler():
        print("yay 2")

    def import_handler():
        importer()

    def troll_handler():
        easter_eggs.troll()
        user_input()

    def floppa_handler():
        easter_eggs.floppa()
        user_input()

    print("what do you want to do?")
    question = input(" \n type [1] to view/edit/create profiles, \n type [2] to execute a profile, \n "
                     "type [3] to import/export profiles. \n \n $")

    handlers = {
        '1': edit_handler,
        '2': exec_handler,
        '3': import_handler,
        'troll': troll_handler,
        'floppa': floppa_handler
    }

    if question in handlers:
        handlers[question]()
    else:
        print("Unknown choice", question)

def viewer():
    parent_dir = os.getcwd()
    created_dir = r"\Profiles"
    script_dir = parent_dir + created_dir
    profiles_path = os.path.join(script_dir, "Profiles.txt")
    try:
        with open(profiles_path, "r") as profile_file:
            profile_list = profile_file.read()
        print(profile_list)
    except IndexError:
        print("err")
    opening_question = input("please type the name of the profile you would like to enter. (case sensitive) \n \n $")

    file_name = opening_question
    file_extension = ".txt"
    file_dir = file_name + file_extension
    profile_list_dir = os.path.join(script_dir, file_dir)

    with open(profiles_path, 'r'):
        if opening_question in profile_list:
            with open(profile_list_dir) as open_file:
                read_file = open_file.read()
                print(read_file)
        else:
            print("Unknown choice", opening_question)

def profile_editor():

    def view_handler():
        viewer()
    def edit_handler():
        print("yay 2")

    def create_handler():
        print("to profile file")

    def troll_handler():
        easter_eggs.troll()
        profile_editor()

    def floppa_handler():
        easter_eggs.floppa()
        profile_editor()

    print("what do you want to do?")
    question = input(" \n type [1] to view a profile, \n type [2] to edit a profile, \n "
                     "type [3] to create/delete profiles. \n \n $")

    handlers = {
        '1': view_handler,
        '2': edit_handler,
        '3': create_handler,
        'troll': troll_handler,
        'floppa': floppa_handler()
    }

    if question in handlers:
        handlers[question]()
    else:
        print("Unknown choice", question)

def importer():

    def setup():
        question = input("please enter the directory of the .json file you want to import. \n "
                         "(this is the exact system directory, for example, [C:\<user_folders>\Downloads])\n "
                         "DO NOT INCLUDE THE FILE IN THIS DIRECTORY \n \n $")
        question2 = input("please enter the name of the file, including the .json extension. (for example, "
                          "[aycd.json])\n \n $")
        file_name = "\\" + question2
        file_name.strip()
        directory = question + file_name
        directory = directory.strip()

        def import_confirmation():
            import_conformation = input("type [y] to import, type [n] to cancel. \n \n $")
            if import_conformation == "y":
                print("transferring")
                convert()
            elif import_conformation == "n":
                print("canceling...")
                user_input()
            else:
                print("unknown answer:", import_conformation)


        profile_name = [2]


        with open(directory, 'r') as importing_file:
            for position, line in enumerate(importing_file):
                line = line.strip()
                if position in profile_name:
                    print("is this the name of the correct profile?")
                    print("------------------------------------------")
                    print(line)
                    print("------------------------------------------")
                    import_hotswap = open("import_hotswap.txt", "w")
                    import_hotswap.write(directory)
                    import_hotswap.close()
                    import_confirmation()
                else:
                    pass

    def convert():
        readline_profilename = [2]
        readline_billing_name = [6]
        readline_billing_email = [7]
        readline_billing_phone = [8]
        readline_billing_line1 = [9]
        readline_billing_line2 = [10]
        readline_billing_line3 = [11]
        readline_billing_postcode = [12]
        readline_billing_city = [13]
        readline_billing_country = [14]
        readline_billing_state = [15]
        readline_shipping_name = [18]
        readline_shipping_email = [19]
        readline_shipping_phone = [20]
        readline_shipping_line1 = [21]
        readline_shipping_line2 = [22]
        readline_shipping_line3 = [23]
        readline_shipping_postcode = [24]
        readline_shipping_city = [25]
        readline_shipping_country = [26]
        readline_shipping_state = [27]
        readline_card_name = [30]
        readline_card_type = [31]
        readline_card_number = [32]
        readline_card_expmonth = [33]
        readline_card_expyear = [34]
        readline_card_ccv = [35]
        readline_samebillingandshippingadress = [37]
        readline_onlycheckoutonce = [38]
        readline_matchnameoncardadress = [39]

        profile_name_question = input("what do you want to call this profile? (do not include the extension)\n \n $")

        parent_dir = os.getcwd()
        created_dir = r"\Profiles"
        script_dir = parent_dir + created_dir
        profiles_path = os.path.join(script_dir, "Profiles.txt")
        new_profile = profile_name_question + ".txt"
        new_profile = new_profile.strip()
        new_profile_path = os.path.join(script_dir, new_profile)
        import_hotswap = open("import_hotswap.txt", "r")
        importing_file_path = import_hotswap.read()
        import_hotswap.close()

        try:
            with open(profiles_path, "a") as profile_file:
                profile_file.write("\n"+ profile_name_question)
                profile_file.close()
            with open(profiles_path, "r") as profile_file:
                profile_list = profile_file.read()
                print(profile_list)
                profile_file.close()
        except IndexError:
            print("err")

        try:
            with open(importing_file_path, "r") as importing_file:
                for position, line in enumerate(importing_file):
                    line = line.strip()
                    if position in readline_billing_name:
                        billing_name = line
                    elif position in readline_billing_email:
                        billing_email = line
                    elif position in readline_billing_phone:
                        billing_phone = line
                    elif position in readline_billing_line1:
                        billing_line1 = line
                    elif position in readline_billing_line2:
                        billing_line2 = line
                    elif position in readline_billing_line3:
                        billing_line3 = line
                    elif position in readline_billing_postcode:
                        billing_postcode = line
                    elif position in readline_billing_city:
                        billing_city = line
                    elif position in readline_billing_country:
                        billing_country = line
                    elif position in readline_billing_state:
                        billing_state = line
                    elif position in readline_shipping_name:
                        shipping_name = line
                    elif position in readline_shipping_email:
                        shipping_email = line
                    elif position in readline_shipping_phone:
                        shipping_phone = line
                    elif position in readline_shipping_line1:
                        shipping_line1 = line
                    elif position in readline_shipping_line2:
                        shipping_line2 = line
                    elif position in readline_shipping_line3:
                        shipping_line3 = line
                    elif position in readline_shipping_postcode:
                        shipping_postcode = line
                    elif position in readline_shipping_city:
                        shipping_city = line
                    elif position in readline_shipping_country:
                        shipping_country = line
                    elif position in readline_shipping_state:
                        shipping_state = line
                    elif position in readline_card_name:
                        card_name = line
                    elif position in readline_card_type:
                        card_type = line
                    elif position in readline_card_number:
                        card_number = line
                    elif position in readline_card_expmonth:
                        card_expmonth = line
                    elif position in readline_card_expyear:
                        card_expyear = line
                    elif position in readline_card_ccv:
                        card_ccv = line
                    elif position in readline_samebillingandshippingadress:
                        samebillingandshippingadress = line
                    elif position in readline_onlycheckoutonce:
                        onlycheckoutonce = line
                    elif position in readline_matchnameoncardadress:
                        matchnameoncardadress = line
                    else:
                        pass


            with open(new_profile_path, "a") as new_profile:
                new_profile.write("shipping information: \/ ----------------------------------------------------\n")
                new_profile.write(profile_name_question + "\n")
                new_profile.write(billing_name + "\n")
                new_profile.write(billing_email + "\n")
                new_profile.write(billing_phone + "\n")
                new_profile.write(billing_line1 + "\n")
                new_profile.write(billing_line2 + "\n")
                new_profile.write(billing_line3 + "\n")
                new_profile.write(billing_postcode + "\n")
                new_profile.write(billing_city + "\n")
                new_profile.write(billing_country + "\n")
                new_profile.write(billing_state + "\n")
                new_profile.write("shipping information: /\ ----------------------------------------------------\n")
                new_profile.close()
                if samebillingandshippingadress == '"sameBillingAndShippingAddress": false,"':
                    new_profile = open(new_profile_path, "a")
                    new_profile.write("shipping information: \/ ----------------------------------------------------\n")
                    new_profile.write(shipping_name + "\n")
                    new_profile.write(shipping_email + "\n")
                    new_profile.write(shipping_phone + "\n")
                    new_profile.write(shipping_line1 + "\n")
                    new_profile.write(shipping_line2 + "\n")
                    new_profile.write(shipping_line3 + "\n")
                    new_profile.write(shipping_postcode + "\n")
                    new_profile.write(shipping_city + "\n")
                    new_profile.write(shipping_country + "\n")
                    new_profile.write(shipping_state + "\n")
                    new_profile.write("shipping information: /\ ----------------------------------------------------\n")
                    new_profile.close()
                elif samebillingandshippingadress == '"sameBillingAndShippingAddress": true,':
                    pass
                else:
                    print("error reading file: same billing and shipping adress is unclear. check importing file. "
                          "continuing anyway")
                if matchnameoncardadress == '"matchNameOnCardAndAddress": true':
                    new_profile = open(new_profile_path, "a")
                    new_profile.write("card information: \/ --------------------------------------------------------\n")
                    new_profile.write("card name:", billing_name + "\n")
                    new_profile.write(card_type + "\n")
                    new_profile.write(card_number + "\n")
                    new_profile.write(card_expmonth + "\n")
                    new_profile.write(card_expyear + "\n")
                    new_profile.write(card_ccv + "\n")
                    new_profile.write("card information: /\ --------------------------------------------------------\n")
                    new_profile.close()
                elif matchnameoncardadress == '"matchNameOnCardAndAddress": false':
                    new_profile = open(new_profile_path, "a")
                    new_profile.write("card information: \/ --------------------------------------------------------\n")
                    new_profile.write(card_name + "\n")
                    new_profile.write(card_type + "\n")
                    new_profile.write(card_number + "\n")
                    new_profile.write(card_expmonth + "\n")
                    new_profile.write(card_expyear + "\n")
                    new_profile.write(card_ccv + "\n")
                    new_profile.write("card information: /\ --------------------------------------------------------\n")
                    new_profile.close()
                else:
                    print("error reading file: match name on card and adress is unclear. check importing file. "
                          "continuing anyway")
                new_profile = open(new_profile_path, "a")
                new_profile.write("settings: \/ ------------------------------------------------------------------")
                new_profile.write(samebillingandshippingadress)
                new_profile.write(onlycheckoutonce)
                new_profile.write(matchnameoncardadress)
                new_profile.write("settings: /\ ------------------------------------------------------------------")
                new_profile.close()
        except IndexError:
            print("there was an error somewhere. "
                  "please check that your file is correctly formatted and has all 42 lines.")
    setup()
