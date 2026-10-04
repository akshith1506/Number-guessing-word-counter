import random
def number_guessing_game():
    secret_number=random.randint(1,100)
    attempts=0
    max_attempts=10
    won=False
    while attempts<max_attempts:
        guess=int(input("Enter your guess:"))
        attempts+=1
        if guess<secret_number:
            print("Too Low!")
        elif guess>secret_number:
            print("Too High!")
        else:
            print("Guess is Correct!")
            won=True
            score=(max_attempts - attempts + 1) *10
            print("Attempts used",attempts)
            print("Score:",score)
            break
    if not won:
        print("Game Over!")
        print("The Correct Number was",secret_number)

def word_counter():
    filename=input("Enter the text file name:")
    with open(filename,"r") as file:
        text=file.read()
    text=text.lower()
    words=text.split()
    total_words=len(words)
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word] = 1
    print("Total_words:",total_words)
    for word,count in word_frequency.items():
        print(word,":",count)

while True:
    print("===== NUMBER GUESSING & WORD COUNTING =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank You for using the program!")
        break
    else:
        print("Invalid choice!")
        print("Please enter 1,2 or 3")