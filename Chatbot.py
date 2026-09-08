#Rule Based AI Python Chatbot
import datetime
import time
#Chatbot Memory - Dictionary to store user input and responses
from DataDictionary import responses

name="Dear User"
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

while True:
    #Take user input
    userinput = input("Please ask me your question: ").lower().strip()

    if userinput in responses:
        print(responses[userinput])
    else:
        print("I'm sorry, I don't understand that.")

    if userinput == "exit":
        break
