import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def countdown(labels, times):
    finished = [False] * len(times)

    while True:
        clear()
        all_done = True

        for i in range(len(times)):
            if times[i] > 0:
                mins, secs = divmod(times[i], 60)
                print(f"{labels[i]} → {mins:02}:{secs:02}")
                times[i] -= 1
                all_done = False
            else:
                if not finished[i]:
                    print(f"⏰ {labels[i]} Time's up!")
                    finished[i] = True

        if all_done:
            print("\n✅ All timers finished!")
            break

        time.sleep(1)

def main():
    while True:
        try:
            nu = input(
                "Enter number of countdown timers (1–3)\n"
                "or press 'q' to quit: "
            ).strip()

            labels = []
            times = []

            if nu.lower() == 'q':
                print("\nExiting program. Goodbye!")
                break

            nu = int(nu)

            if nu < 1 or nu > 3:
                raise ValueError("Please choose a number between 1 and 3.")

            for i in range(nu):
                while True:
                    try:
                        label = input(f"\nTimer {i + 1} label: ").strip()
                        if not label:
                            raise ValueError("Label cannot be empty.")

                        seconds = input(
                            f"Countdown duration for '{label}' (in seconds): "
                        ).strip()

                        if not seconds.isdigit():
                            raise ValueError("Please enter a valid positive number.")

                        seconds = int(seconds)
                        if seconds <= 0:
                            raise ValueError("Time must be greater than zero.")

                        labels.append(label)
                        times.append(seconds)
                        break

                    except ValueError as e:
                        print(f"❌ {e}")

            print("\nStarting countdown...\n")
            countdown(labels, times)

            again = input("\nRun another countdown? (y/n): ").strip().lower()
            if again != 'y':
                print("\nThanks for using Countdown Timer.")
                break

        except ValueError as e:
            print(f"❌ {e}")
           
main()
