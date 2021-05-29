import easter_eggs

def user_input():

    def edit_account_handler():
        print("yay")

    def edit_settings_handler():
        print("yay 2")

    def key_handler():
        print("yay3")

    def troll_handler():
        easter_eggs.troll()
        user_input()

    def floppa_handler():
        easter_eggs.floppa()
        user_input()

    print("what do you want to do?")
    question = input(" \n type [1] to view/edit your local account information, "
                     "\n type [2] to set default cooking settings (like rates, sizes, insta-run profiles etc.), "
                     "\n type [3] to manage your key \n \n $")

    handlers = {
        '1': edit_account_handler,
        '2': edit_settings_handler,
        '3': key_handler,
        'troll': troll_handler,
        'floppa': floppa_handler
    }

    if question in handlers:
        handlers[question]()
    else:
        print("Unknown choice", question)
