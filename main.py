import ollama



model = "qwen2.5:7b"
message_list =[]
while True:

    write = input("You: ")
    if write.lower() == "exit":
        break

    message_list.append({   
        "role":"user",
        "content":write
    })


    response = ollama.chat(
        model = model,
        messages=message_list,
    )

    message_list.append({
        "role":"assistant",
        "content":response.message.content
    })

    print("AI: ",response.message.content)