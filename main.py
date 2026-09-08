from datetime import datetime   

print("Welcome to ai assistant")

def date():
    date = datetime.now().date()
    return date

def time():
    time = datetime.now().time()
    return time

def response(message):
    if message == "exit":
        return "good bye"
    else :
        return "i think you made wrong command"



def calculate():
    while True:
        try:
            num1 = int(input("End the first number"))
            num2 = int(input("End the second number"))

            sum =0
            while True:
                opr = input("-,/,*,+ --- select any")
                opr_list = ["-","*","/","+"]

                if opr not in opr_list:
                    continue
                else:
                    break

            if opr == "-":
                sum = num1 - num2 
            elif opr == "+":
                sum =num1 + num2
            elif opr == "/":
                sum =num1 / num2 
            elif opr == "*":
                sum =num1 * num2 

            return sum
            
        except ZeroDivisionError:
            print("cant devided by zero")
            continue
        except ValueError:
            print("Enterd wrong number")
            continue





while True:

    user = input().lower()
    if user == "hello":
        print("Hello! How can I help you?")
    elif user == "time":
        print(time())
    elif user == "date":
        print(date())
    elif user == "clear":
        print("clearing data...")
    elif user == "calculate":
        print(calculate())
    elif user == "exit":
        print(response(user))
        break
    else:
        print(response(user))
     


    
        