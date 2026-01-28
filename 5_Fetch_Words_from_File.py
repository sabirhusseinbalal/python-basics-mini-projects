from pathlib import Path
import string, collections
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


    filtered = {}

    show_all = input("Show only repeated words? (y/n): ").lower() == 'y'
    if show_all:
        for word, count in counter.items():
            if count > 1: 
                filtered[word] = count
    else:
        filtered = dict(counter)



    data = pd.DataFrame({
        "Word": filtered.keys(),
        "Count": filtered.values()
    }).sort_values(by="Count", ascending=False).reset_index(drop=True)

    print(data)




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


