from pathlib import Path
import string, collections, random
import pandas as pd


def uni(f):
    translator = str.maketrans('', '', string.punctuation)

    text = ""
    for line in f:
        text += line.lower().translate(translator)

    words = [w for w in text.split() if w.isalpha()]

    if not words:
        print("File is empty or contains no valid words.")
        return

    counter = collections.Counter(words)

    repeated_words = []

    for word, count in counter.items():
        if count > 1: 
            repeated_words.append(word)

    

    while True:
        result = input("Do you want to pick from repeated words only? [y/n] (or 'q' to quit): ")
        if result.lower()=='q':
            break
        elif result.lower()=='y':
            if not repeated_words:
                print("No repeated words found.")
            else:
                print(random.choice(repeated_words))
        elif result.lower()=='n':
            print(random.choice(words))
        else:
            print("Invalid choice, please enter 'y', 'n', or 'q'.")


while True:
    user_path = input("Enter full file path: (or 'q' to quit) ")
    if user_path.lower()=='q':
        break

    path = Path(user_path)
    if path.is_file():
        if path.suffix == ".txt":
            with path.open("r", encoding="utf-8") as f:
                uni(f)
        else:
            print("Invalid file type. Only .txt allowed")
    else:
        print("File not found")


