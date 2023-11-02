# Gregory Chernyavskiy             <09/14/2022>
# Assignment2

print("Welcome to the Magic 9 Ball...")
print()

print("By: Gregory Chernyavskiy")
print("[COM S 127 B]")
print()

print("\nWhat would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print()



if choice.lower() == "c":
    list = ("[+], [-], [*], [/], [%], [**]")
    choice_c = input("Enter one of the choices: \n[+], [-], [*], [/], [%], [**]")
    if choice_c == "+":
        print("Enter two numbers that you want to use for addition.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a + b
        print(" When you add {0} with {1} it will equal to {2}".format(a,b,c))
    elif choice_c == "-":
        print("Enter two numbers that you want to use for subtraction.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a - b
        print(" When you subtact {1} with {0} it will equal to {2}".format(a,b,c))
    elif choice_c == "*":
        print("Enter two numbers that you want to use for multiplication.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a * b
        print(" When you multiply {0} with {1} it will equal to {2}".format(a,b,c))
    elif choice_c == "/":
        print("Enter two numbers that you want to use for multiplication.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a / b
        print(" When you divide {0} from {1} it will equal to {2}".format(a,b,c))
    elif choice_c == "%":
        print("Enter two numbers that you want to use for modulus.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a % b
        if b <= 0:
            print("The second value cannot be 0 or less than zero! Please restart the program.")
        else:
            print(" When you mod {1} from {0} it will equal to {2}".format(a,b,c))
    elif choice_c == "**":
        print("Enter two numbers that you want to use for exponent.")
        a = int(input("a: "))
        b = int(input("b: "))
        c = a ** b
        print(" When you raise {0} to {1} power it will equal to {2}".format(a,b,c))
    else:
        print("Plese enter the signs from the list:" ,list,)



elif choice.lower() == "p":

    AnswerList = ["100% yes", "100% no", "May be", "May be not", "Absolutely", "Absolutely not", 
    "Could be", "Never", "Might not", "Sure"]

    print("\nWhat is your question?")

    question = str(input("Question: "))
    Value = len(question) % len(AnswerList)

    if 0 <= Value <= 10:
        print("\nThe answer to your question -" ,question, "- is: " ,AnswerList[Value],)
    else:
        print("Error. Please restart the program!")



elif choice.lower() == "q":
    print("May be next time... See you later!")



else:
    print("ERROR. Please restart the program and enter the letters from the list (c, p or q).")