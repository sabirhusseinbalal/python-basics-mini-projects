import random
import time

def random_number():
    return random.randint(1, 100)

def main():
    heart = 5
    score = 0
    maxHints = 3
    hintCount = 0
    x = random_number()
    start_time = time.time()

    while True:
        try:
            if maxHints > 0:
                y = input(f"Guess Number (or 'q' to quit, 'h' for hint {maxHints} left): ")
            else:
                y = input("Guess Number (or 'q' to quit): ")

            if y.lower() == 'q':
                print("💔 Game Over")
                break

            if y.lower() == 'h':
                if maxHints <= 0:
                    print("No hints left 💔")
                else:
                    maxHints -= 1
                    hintCount += 1
                    if hintCount == 1:
                        print(f"The number is {'Even' if x%2==0 else 'Odd'}")
                    elif hintCount == 2:
                        high = x + random.randint(1,10)
                        low = x - random.randint(1,10)
                        print(f"The number is between {low} and {high}")
                    elif hintCount == 3:
                        print("Number is above 50" if x>50 else "Number is 50 or below")
                continue

            guess = int(y)
            if guess < 1 or guess > 100:
                print("Number must be between 1-100")
                continue

            if guess == x:
                print("🎉 Congrats! You guessed it!")
                score += 1
                heart = 5
                maxHints = 3
                hintCount = 0
                x = random_number()
            else:
                heart -= 1
                score -= 1
                print("❤ " * heart)
                if heart == 0:
                    print("💔 Out of hearts!")
                    again = input("Play again? (y/n): ").lower()
                    if again == 'y':
                        heart = 5
                        maxHints = 3
                        hintCount = 0
                        score = 0
                        x = random_number()
                        start_time = time.time()
                        print("Next Number...")
                    else:
                        break
        except ValueError:
            print("Invalid input. Enter a number!")

    elapsed = time.time() - start_time
    print(f"Total time played: {elapsed:.2f} seconds | Final Score: {score}")

print("Welcome! Guess the number between 1 and 100.")
main()
