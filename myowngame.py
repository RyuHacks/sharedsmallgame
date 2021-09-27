print("You are inside an airplane, halfway through the flight. You planned to fly to Las Vegas for vacation. You check your watch, it shows 5:32 pm. You're in the window seat, there is no one on the aisle seat.")
print("You glance briefly at the window, there is no visibility to any cities, the airplane is high above the clouds.")
print("1. Stay in your seat.")
print("2. Go to the toilet to freshen up.")
firstselection = input("> ")

if firstselection == "1":
    print ("The watier approaches you and questions your drink selection.")
    print ("1. Orange Juice")
    print ("2. Coca-Cola")
    print ("3. Water")

    firstselectionone = input("> ")

    if firstselectionone == "1":
        print ("The waiter gives you cold tasty orange juice. Common choice of drink, your body feels refreshed after drinking this! ")
    elif firstselectionone == "2":
        print ("The waiter gives you cold tasty coca cola. The soda burns your tongue, your throat as you gulp it in.")
    elif firstselectionone == "3":
        print ("The waiter gives you plain cold water. Same old water you've been drinking since you were born, it's healthy and dull.")


elif firstselection == "2":
    print ("You arrive at the toilet.")
    print ("1. Wash your face.")
    print ("2. Wash your face, wash your glasses")

    firstselectiontwo = input("> ")

    if firstselectiontwo == "1":
        print ("Your face feels refreshed, however your gut starts to feel weird. You head back to your seat.")
    elif firstselectiontwo == "2":
        print ("Your face feels refreshed, your glasses are clear, your vision is great, however your gut tells you something's off. You head back to your seat.")
import time        
time.sleep(1)
print ("Your gut tells you something isn't right. There is just something that feels off, maybe its the smell of the airplane?")
print ("1. Check the time on your watch")
print ("2. Drink the water bottle you stored in your bag, maybe it's the only thing normal here?")
secondselection = input("> ")

if secondselection == "1":
    print ("Huh, strange, the time still shows 5:32 pm.")

elif secondselection == "2":
    print ("Didn't feel like anything, for some reason you're still thirsty. You glance on your watch, it shows 5:32 pm.")

print ("Perhaps your watch might be broken? You could try fixing it or using another clock.")
print ("1. Try to check the insides of the watch.")
print ("2. Use another clock somewhere.")
thirdselection =  input("> ")

if thirdselection == "1":
    print ("The watch seems to be perfectly fine, you can see the internals ticking and moving correctly.")

elif thirdselection == "2":
    print ("You glance at the watch of the person sleeping in front of you, it shows 5:32 pm as well.")
time.sleep(1)
print ("What?? This isn't possible right?")
time.sleep(1)
print ("The airplane smells of old building walls?? Smells weird here")
time.sleep(1)
print ("Everyone else seems asleep, it is still day time outside.")
time.sleep(1)
print ("Maybe I'm going crazy??")
time.sleep(1)
print ("1. Call for a flight attendant")
print ("2. Ask the person in front of you")
fourthselection = input ("> ")

if fourthselection == "1":
    time.sleep(1)
    print ("A flight attendant approaches you.")
    print ("1. When do we land?")
    print ("2. What time is it right now?")

    fourthselectionone = input ("> ")

    if fourthselectionone == "1":
        print ("The flight attendant seems to be grinning with tears running down his cheeks.")
        time.sleep(1)
        print ("Sir we are landing in an hour, it is currently 5:32 pm, we expect to be arriving on 6:30 pm")
        time.sleep(1)
        print ("The flight attendant leaves. He walks in a weird way. His movements feel off, it feels inhuman...")

    elif fourthselectionone == "2":
        print ("The flight attendant seems to be grinning with tears running down his cheeks.")
        time.sleep(1)
        print ("Sir it is currently 5:32 pm and we are landing in about an hour, we expect to be arriving on 6:30 pm")
        time.sleep(1)
        print ("The flight attendant leaves. He walks in a weird way. His movements feel off, it feels inhuman...")

if fourthselection == "2":
    time.sleep(1)
    print ("The person in front wakes up in a weird manner, her movements feel weird.")
    print ("1. Sorry to disturb you, but may I ask when do we land?")
    print ("2. Sorry to disturb you, but may I ask what time is it right now? I feel that my watch might be broken.")

    fourthselectiontwo = input ("> ")

    if fourthselectiontwo == "1":
        print ("Her eyes aren't moving together, her eyes stare behind you. You can tell her attention is on you.")
        time.sleep(1)
        print ("The flight lands around an hour, it is currently 5:32 pm, you can sleep or anything, it won't take that long.")
        time.sleep(1)
        print ("Her head turns around like its controlled by a DC motor. A reflection shows her eyes turn pale as if it switches off before closing her eyelid. Her back remains stiff.")

    elif fourthselectiontwo == "2":
        print ("Her eyes aren't moving together, her eyes stare behind you. You can tell her attention is on you.")
        time.sleep(1)
        print ("The time right now is 5:32 pm, there is nothing wrong with your watch. We're landing in about an hour.")
        time.sleep(1)
        print ("Her head turns around like its controlled by a DC motor. A reflection shows her eyes turn pale as if it switches off before closing her eyelid. Her back remains stiff.")
    
time.sleep(1)
print ("You glance outside the window again.")
time.sleep(1)
print ("A sense of Deja Vu runs up your spine, isn't this the same cloud formation you saw some time ago??")
time.sleep(1)
print ("Now you look at the bottle of water that you drank in the start of the flight, it's full??")
time.sleep(1)
print ("This doesn't make sense, feels like a glitch in the matrix.")
time.sleep(1)
print ("The smell of the plane is now starting to make you feel sick, you feel sleepy now.")
time.sleep(1)
print ("1. Fall asleep")
print ("2. Drink the bottle of water")

time.sleep(1)
fifthselection = input ("> ")

if fifthselection == "1":
    print ("Your eyelid closes, for a brief moment while closing, all the lights turn on to full brightness then off again.")

elif fifthselection == "2":
    print ("You drink the bottle of water, it taste like nothing, you feel as if nothing has happened.")
    time.sleep(1)
    print ("You check the bottle of water, you didn't drink it, it's still full.")
    time.sleep(1)
    print ("In fact, now you don't even remember you drank the water.")
    time.sleep(1)
    print ("Your eyelids close as if something forces it to, you fall asleep.")

print ("Thanks for playing part 1 of the game!")
    
    

