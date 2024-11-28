import random

# Initialize records
records = {
    "total_runs": 0,
    "highest_runs": 0,
    "games_played": 0,
    "total_50s": 0,
    "total_100s": 0,
    "total_ducks": 0,
    "total_balls": 0,  # To track total balls faced across all games
}


def view_records():
    print("\n--- Your Records ---")
    print(f"Total Runs Scored: {records['total_runs']}")
    print(f"Highest Runs in a Game: {records['highest_runs']}")
    print(f"Average Runs: {records['total_runs'] / records['games_played'] if records['games_played'] > 0 else 0:.2f}")
    print(f"Total 50s: {records['total_50s']}")
    print(f"Total 100s: {records['total_100s']}")
    print(f"Total Ducks: {records['total_ducks']}")
    print(f"Total Balls Faced: {records['total_balls']}")
    strike_rate = (records['total_runs'] / records['total_balls'] * 100) if records['total_balls'] > 0 else 0
    print(f"Overall Strike Rate: {strike_rate:.2f}\n")


def play_game():
    print("\n--- Game Started ---")
    score = 0
    balls_faced = 0

    while True:
        print("\nChoose your shot:")
        print("1. Defensive")
        print("2. Balanced")
        print("3. Aggressive")
        print("4. Brute")
        shot_choice = input("Enter your choice (1-4): ")

        if shot_choice == "1":
            outcome = random.choices(["0", "1", "2", "4", "6", "OUT"], weights=[40, 30, 20, 10, 5, 5])[0]
        elif shot_choice == "2":
            outcome = random.choices(["0", "1", "2", "4", "6", "OUT"], weights=[25, 35, 25, 20, 10, 10])[0]
        elif shot_choice == "3":
            outcome = random.choices(["0", "1", "2", "4", "6", "OUT"], weights=[10, 15, 20, 35, 25, 15])[0]
        elif shot_choice == "4":
            outcome = random.choices(["0", "1", "2", "4", "6", "OUT"], weights=[10, 10, 10, 40, 40, 30])[0]
        else:
            print("Invalid choice. Try again.")
            continue

        balls_faced += 1

        if outcome == "OUT":
            print(f"You are OUT! Final Score: {score} in {balls_faced} balls.")
            print(f"Strike Rate: {(score / balls_faced) * 100:.2f}")
            update_records(score, balls_faced)
            break
        else:
            runs = int(outcome)
            score += runs
            strike_rate = (score / balls_faced) * 100
            print(f"You scored {runs} runs. Current Score: {score}")
            print(f"Balls Faced: {balls_faced}, Strike Rate: {strike_rate:.2f}")
            if score in [50, 100, 150, 200]:
                print(f"Congratulations! You reached {score} runs!")


def update_records(score, balls_faced):
    records["games_played"] += 1
    records["total_runs"] += score
    records["total_balls"] += balls_faced
    records["highest_runs"] = max(records["highest_runs"], score)
    if score == 0:
        records["total_ducks"] += 1
    if score >= 50:
        records["total_50s"] += 1
    if score >= 100:
        records["total_100s"] += 1


def main():
    while True:
        print("\n--- Welcome to the Cricket Game ---")
        print("1. Start Game")
        print("2. View Records")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
