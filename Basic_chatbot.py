def chatbot():
    """
    A simple rule-based chatbot that responds to specific user inputs.
    """
    print("Welcome to the simple chatbot! You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that. Please try saying 'hello', 'how are you', or 'bye'.")

# Start the chatbot
if __name__ == "__main__":
    chatbot()