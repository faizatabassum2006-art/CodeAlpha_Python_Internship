# CodeAlpha Internship - Task 3
# Basic Chatbot

print("=" * 40)
print("          BASIC CHATBOT")
print("=" * 40)

print("Hello! I am a simple chatbot.")
print("You can say hello, ask how I am, or say bye.")
print("Type 'bye' to end the conversation.\n")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi! Nice to meet you!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")

print("\nThank you for chatting!")