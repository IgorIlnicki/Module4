def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    print(f" cmd = {cmd} *args = {args}")
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
   
    return print(f"Contact {name} added phone: {phone}") 
    
def show_phone(args, contacts):
    name  = args
    phone = contacts[name]
    return print(f"Contact {name}: {phone}")

def main():
    contacts = {}  #  словник з іменем і номером телефону
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print(f" command = {command} *args = {args}")
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(args, contacts)
            # print(add_contact(args, contacts))
            # print(len(contacts))
            # print(f"Tel: {contacts}")

        elif command == "phone":
            print(show_phone(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()