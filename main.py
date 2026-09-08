import ollama



model = "qwen2.5:7b"
message_list =[]
while True:

    write = input("You: ")
    message_list.append(write)

    if write.lower() == "exit":
        break


    response = ollama.chat(
        model = model,
        messages=[
            
            {
                {
                    "role":"user",
                    "content": write
                }
            }
        ]
    )

    print("AI: ",response.message.content)