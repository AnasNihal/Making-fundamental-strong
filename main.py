print("Welcome to ai assistant")

message = ["Hello! How can I help you?","How are you!","I'm Terminal AI"]

while True:
    user = input()
    if user.lower() == "hello":
        print(message[0])
    elif user.lower() == "how are you":
        print(message[1])
    elif user.lower() == "what is your name":
        print(message[2])
     


    if user.lower() == "exit" :
        print("Good  bye")
        break
    else:
        continue

    
        