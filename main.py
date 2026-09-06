from datetime import datetime   

print("Welcome to ai assistant")


while True:

    user = input().lower()
    if user == "hello":
        print("Hello! How can I help you?")
    elif user == "time":
        print(datetime.now().time())
    elif user == "date":
        print(datetime.now().date())
    elif user == "clear":
        print("clearing data...")
    elif user == "exit":
        print("Good Bye")
        break
    else:
        print("I dont understand that yet")
     


    
        