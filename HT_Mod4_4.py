

print(":")
comand_in = input()
fh =str(comand_in) 
print(type(fh))
fh = fh.split()
print(len(fh))
print(f"  fh = {fh}")
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
    print(f"Contact {fh[1]} added: {fh[2]}")

else:
    print("Uncorrect")
# match comand_in:
#     case "hello":
#         print("How can I help you?\n")
#     case :
#         print("Input greetings or comand:\n")


