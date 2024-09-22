def chatbot_response(user_input):
    # Convert the input to lowercase to make matching easier
    user_input = user_input.lower()

    # Basic rule-based responses
    if "hey" in user_input or "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm Jacob a chatbot created to assist you with basic tasks."
    elif "time" in user_input:
        return "I don't know what time is it there, but hope you are fine."
    elif "how are you" in user_input or "how do you do" in user_input:
        return "I am all fine, hope its good for you too."
    elif "beautiful place" in user_input or "lovely place" in user_input:
        return "I havent been to the place but Earth is pretty beautiful!"
    elif "do you know" in user_input or "are you aware" in user_input:
        return "I just began my journey and still learning!!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Bye! Nice meeting you"    
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Jacob: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
