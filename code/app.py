print("📱 Mobile Learning App Evaluation System")

def evaluate():
    try:
        app_name = input("\nEnter app name: ")
        
        ease = int(input("Ease of use (1-5): "))
        content = int(input("Content clarity (1-5): "))
        engagement = int(input("Student engagement (1-5): "))
        distraction = int(input("Low distraction (1-5): "))
        support = int(input("Learning support (1-5): "))

        avg = round((ease + content + engagement + distraction + support) / 5, 2)

        print("\nApp Name:", app_name)
        print("Average Score:", avg)

        if avg >= 4:
            result = "Very Good for Learning"
        elif avg >= 3:
            result = "Good for Learning, but can be improved!"
        else:
            result = "Needs Improvement"

        print("Evaluation Result:", result)

        # Save only after full successful input
        f = open("data.txt", "a")
        f.write(app_name + " - " + str(avg) + " - " + result + "\n")
        f.close()

        print("Data saved successfully!")

    except:
        print("❌ Invalid input or program exited! Record NOT saved.")

def show_history():
    print("\n📜 Previous Evaluations:\n")
    try:
        f = open("data.txt", "r")
        print(f.read())
        f.close()
    except:
        print("No history found!")


def delete_history():
    confirm = input("Are you sure you want to delete all history? (yes/no): ")
    if confirm.lower() == "yes":
        f = open("data.txt", "w")
        f.close()
        print("✅ History deleted successfully!")
    else:
        print("Delete cancelled.")


def recommend_best():
    try:
        f = open("data.txt", "r")
        lines = f.readlines()
        f.close()

        if len(lines) == 0:
            print("No records found!")
            return

        best_app = ""
        best_score = 0

        for line in lines:
            parts = line.strip().split(" - ")
            name = parts[0]
            score = float(parts[1])

            if score > best_score:
                best_score = score
                best_app = name

        print("\n🏆 Best Recommended Learning App")
        print("App Name:", best_app)
        print("Score:", best_score)

    except:
        print("No history found!")


while True:
    print("\n===== MENU =====")
    print("1. Evaluate New App")
    print("2. View History")
    print("3. Delete History")
    print("4. Recommend Best App")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        evaluate()
    elif choice == "2":
        show_history()
    elif choice == "3":
        delete_history()
    elif choice == "4":
        recommend_best()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
