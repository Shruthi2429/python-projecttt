Shruthi.p/1AY24AI104/O sec
import random

def generate_flips(num_flips=100):
    return [random.choice(['H', 'T']) for _ in range(num_flips)]

def count_streaks(flips, streak_length=6):
    streaks = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                streaks += 1
        else:
            current_streak = 1

    return streaks

def main():
    total_streaks = 0
    experiments = 10000

    for _ in range(experiments):
        flips = generate_flips()
        total_streaks += count_streaks(flips)

    print(f"Total streaks of 6 in a row over {experiments} simulations: {total_streaks}")
    print(f"Chance of streak: {total_streaks / experiments * 100:.2f}%")

if __name__ == "__main__":
    main()
