import random

best_score = None

while True:
    # Show best score before starting a new game
    if best_score is None:
        print("\nBest Score: No games completed yet.")
    else:
        print(f"\nBest Score: {best_score} guesses")

    # Generate random number
    secret = random.randint(1, 100)
    guesses = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! {guesses} guesses.")
            break

    # Update best score
    if best_score is None or guesses < best_score:
        best_score = guesses
        print("New best score!")

    # Ask to play again
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
