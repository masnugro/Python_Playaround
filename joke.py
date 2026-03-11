print("Welcome to Random Joke Teller! ")
print("Categories:")
print("  1. Random")
print("  2. Useless Facts")
print("  3. Dad Jokes\n")

import random
import urllib.request
import json

def random_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = urllib.request.urlopen(url, timeout=7)
        data = json.loads(response.read())
        return data["setup"], data["punchline"]
    except:
        return None, None
        
def useless_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        response = urllib.request.urlopen(url, timeout=7)
        data = json.loads(response.read())
        return data["text"]
    except:
        return "A group of flamingos is called a flamboyance"
        
def dad_joke():
    try:
        url = "https://icanhazdadjoke.com/"
        request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "PythonistaJokeApp"})
        response = urllib.request.urlopen(request, timeout=7)
        data = json.loads(response.read())
        return data["joke"]
    except:
        return "What have one leg and three eyes?...... A traffic light! 😂"
        
        
categories = {"1": "Random", "2": "Useless Facts", "3": "Dad Jokes"}

while True:
    choice = input("Pick a category: (1/2/3): ")
    
    if choice not in categories:
        print("Invalid choice! Please enter 1, 2 or 3")
    else:
        category = categories[choice]
        if category == "Random":
            setup, punchline = random_joke()
            if setup is None:
                print("Sorry, connection is error!")
            else:
                print(f"🙂‍↕️{setup}")
                input("Press enter to see Punchline 🤪")
                print(f"😂😂😂{punchline}")
        elif category == "Useless Facts":
            print("Useless Facts is coming")
            text = useless_fact()
            print(f"{text}")
            #if text is None:
                #print("Sorry, connection is error!")
            #else:
                #print(f"{text}")
        elif category == "Dad Jokes":
            print("Dad Jokes for laugh!")
            joke = dad_joke()
            print(f"{joke}")    
            #if joke is None:
                #print("Sorry, connection is error!")
            #else:
                #print(f"{joke}")
    
    again = input("addicted to another joke? (y/n): ")
    if again == "n":
        print("Really that's enough? 🤔 Ok, see you soon!")
        break
    print()
