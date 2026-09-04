print("Welcome to ai assistant")

message = ["Hello! How can I help you?","How are you!","I'm Terminal AI"]

while True:
    user = input().lower()
    if user == "hello":
        print(message[0])
    elif user == "how are you":
        print(message[1])
    elif user == "what is your name":
        print(message[2])
    elif user == "exit":
        print("Good Bye")
        break
    else:
        print("I dont understand that yet")
        continue
     


    
        