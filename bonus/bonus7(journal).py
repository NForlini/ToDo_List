date = input("Enter todays date (yyyy-mm-dd): ")
mood = input("How are you feeling today? 1-10, 10 being the best: ")
thoughts = input("Let the thoughts flow!\n")

with open(f'../journal/{date}.txt', 'w') as file:
    file.write(f"Day's mood: {mood}\n\n")
    file.write(thoughts)