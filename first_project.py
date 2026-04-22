print("🤖 AI Chatbot Started (type 'exit' to stop)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    elif "hello" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm doing great 😄")

    elif "sad" in user_input:
        print("Bot: Don't worry, everything will be okay ❤️")

    elif "happy" in user_input:
        print("Bot: That's awesome! Keep smiling 😎")

    else:
        print("Bot: I didn't understand that yet 🤖")
