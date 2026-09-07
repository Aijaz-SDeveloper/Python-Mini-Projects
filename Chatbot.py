#Rule Based AI Python Chatbot
import datetime
import time
name = input("Please enter your name: ")
present_time = datetime.datetime.now().hour

if present_time < 11:
    print(f"Good Morning {name}!")

elif present_time < 17:
    print(f"Good Afternoon {name}!")
elif present_time < 20:
    print(f"Good Evening {name}!")
else:
    print(f"Good Night {name}!")

print("Hi! Welcome to Rule Based Chatbot")
print("You can ask me basic question, Type 'Bye' to exit from the chat bot")

#Chatbot Memory - Dictionary
responses={
    "hello":"Hello! welcome How can I help you?",
    "how are you":"I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "You are capable of amazing things. Believe in yourself and keep pushing forward!",
    "what is your name": "I am a Rule Based Chatbot",
    "happy": "Happiness is a choice. Focus on the positive and find joy in the little things.",
    "what is function": "A function is a block of organized, and reusable...",
    "bye": "Goodbye! Have a great day!"
}

while True:
    #Take user input
    userinput = input("Please ask me your question: ").lower()

    if userinput in responses:
        print(responses[userinput])
    else:
        print("I'm sorry, I don't understand that.")

    if userinput == "exit":
        break