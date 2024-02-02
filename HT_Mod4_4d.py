from pathlib import Path

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    # print(f" cmd = {cmd} *args = {args}")
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return print(f"Contact {name} added phone: {contacts[name]}") 

def change_to_file(args, contacts):
    file = open('Contacts_phone.txt', "rt")
    ss = str() # створюємо пустий список
    for s in file:
        s = s.rstrip()  # Забираємо останній символ '\n' з s
        # print("s = ", s) Вивести s для контролю
        contacts = s.split(":")
        if args[0] == contacts[0]: 
            contacts[1] = args[1]
            print(f" name: {contacts[0]} new (change) phone: {contacts[1]}") 
            s = str(contacts[0]) + ":" + str(contacts[1])
        else:
            print(f"Name {args[0]} is absent")
            break
        ss += s # додаємо до нашого списку рядок з іменем та телефоном
        ss += '\n' # додати символ нового рядка
    file.close()
    file = open('Contacts_phone.txt', "wt")
    file.write(ss)
    file.close()


def show_phone(args, contacts):
    name  = args[0]
    print(f"show_phone name: {name}")
    file = open('Contacts_phone.txt', "rt")
    contacts = {} # Створити пустий словник
    for lines in file: # Використовуєм ітератор файлу
    # Кожний підрядок lines - це елемент виду key:value
        strings = lines.split(':') # розбиваємо lines на 2 підрядки
        key = strings[0] # отримуємо ключ
        # print(f"key {key} name {name}")
        if key == name:
            value = strings[1].rstrip() # отримуємо значення без '\n'
            print(f"Phone {key} is: {value}") 
            contacts[key] = value # додаємо телефон до словника
            break
        else:
            print(f"Name {key} is absent")
    # print("contacts = ", contacts)  Вивести словник для контролю
    file.close()
    return contacts


def show_all(contacts):
    file = open('Contacts_phone.txt', "rt")
    # Для читання рядків використовується ітератор файлу
    for s in file:
        s = s.rstrip() # отримуємо значення без '\n'
        # print("s = ", s)  Вивести s для контролю
        contacts = s.split(":")  # розбиваємо lines на 2 підрядки
        print(f" name: {contacts[0]} phone: {contacts[1]}")  
    file.close()


def write_to_file(r1):
    # print(f" r1 = {r1}")
    # Відкриваємо текстовий файл для запису та дозапису
    file = open('Contacts_phone.txt', "a")
    # Сформуємо рядок виду key:value
    s = str(r1[0]) # взяти ключ як рядок
    s += ':' # додати символ ':'
    s += str(r1[1]) # додати значення value
    s += '\n' # додати символ нового рядка
    # print(f" s = {s}")
    file.write(s) 
    file.close()

def main():
    contacts = {}  #  словник з іменем і номером телефону
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        # print(f" command = {command} *args = {args}")
        # print(f" contacts = {contacts}")
        if command in ["close", "exit"]:
            print("Good bye!")
            #exit() завершує програму, але в ДЗ вказано break
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(args, contacts)
            write_to_file(args)

        elif command == "change":
            change_to_file(args, contacts)

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            show_all(contacts)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    try:
        file = open('Contacts_phone.txt', "rt")
    except IOError as e:
        print(f"Файл з таким ім'ям відсутній: {e}")
    else:
        with file:
            print("Welcome to the assistant bot!")
            main()


    