secret_number =5
i=0
while i<=3:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You got it!")
        break
    else:
        print("Try again!")
        if secret_number>guess:
            print("go higher")
        else:
            print("go lower")
    i+=1
print("You have exhausted your chances!")