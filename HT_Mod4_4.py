
dict_tel = {}  # створюємо пустий словник з іменами і телефонами

def change_contact(fh[0], fh[1], tel_number):
    match fh[0]:
            case ["add"]:
                print("add")
                if True != fh[1].isalpha(): # перевіряємо правильність імені
                    # if True == fh[2].isdigit():
                        dict_tel.update({"name":fh[1], "tel_number":fh[2]})
                        print(f"Contact {fh[1]} added: {fh[2]}") 
            case ["change"]:   
                print("change")
                pass # show_oll()
    return




print(":")
comand_in = input()
fh =str(comand_in) 
print(type(fh))
fh = fh.split()
print(len(fh))
print(f"  fh[0] = {fh[0]}")
if True != fh[0].isalpha():
    print("Incorrect data entry")
else:
    if len(fh) == 1:
        match fh:
            case ["hello"]:
                print("How can I help you?:") 
            case ["all"]:
                print("all")
                pass # show_oll()
            case ["close"]:
                print("Close. Good bye!")
            case ["exit"]:
                print("eExit. Good bye!")
    elif len(fh) == 2:
        print(f"phone number {fh[0]}: {fh[1]}")

    elif len(fh) == 3:
        change_contact(fh[0], fh[1], fh[2])

    else:
        print("Uncorrect")


# match comand_in:
#     case "hello":
#         print("How can I help you?\n")
#     case :
#         print("Input greetings or comand:\n")


