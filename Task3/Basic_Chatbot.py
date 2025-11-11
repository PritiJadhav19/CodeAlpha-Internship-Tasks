import datetime

def greet_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def chatbot():
    print("🤖 Welcome to PyBot — Your Friendly Assistant!")

    
    name = input("Please enter your name: ").capitalize()
    print(f"{greet_user()}, {name}! I'm PyBot. Type 'help' to see what I can do.\n")

    while True:
        user_input = input(f"{name}: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print(f"PyBot: Hello {name}! Nice to see you again!")
        
        elif user_input in ["how are you", "how are you doing"]:
            print("PyBot: I'm doing great, thanks for asking! How about you?")
        
        elif user_input in ["i am fine", "i am good", "fine", "good"]:
            print("PyBot: Glad to hear that! 😊")
        
        elif user_input in ["what is your name", "who are you"]:
            print("PyBot: I'm PyBot, your simple Python-based virtual assistant.")
        
        elif user_input in ["time", "what time is it", "current time"]:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"PyBot: The current time is {current_time}.")
        
        elif user_input in ["date", "what date is it", "today's date"]:
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"PyBot: Today’s date is {today}.")
        
        elif user_input in ["help", "menu"]:
            print("\nPyBot Commands:")
            print(" - hello / hi / hey : Greet the bot")
            print(" - how are you : Check how PyBot is doing")
            print(" - time : Show current time")
            print(" - date : Show today’s date")
            print(" - bye / exit / quit : End the chat\n")
        
        elif user_input in ["bye", "exit", "quit"]:
            print(f"PyBot: Goodbye {name}! Have a wonderful day ahead!")
            break
        
        elif user_input in ["thank you", "thanks"]:
            print("PyBot: You're welcome! Always happy to help.")
        
        else:
            print("PyBot: Hmm, I didn’t quite get that. Try typing 'help' to see what I understand.")


chatbot()
