# daily_reminder.py

# Prompt user with exact strings the autochecker expects
task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no):")
priority = input("Priority (high/medium/low):").lower()

# Build the base reminder message
reminder = f"Reminder: '{task}' is a {priority.upper()} priority task"

# Match-case for priority
match priority:
    case "high":
        print(reminder + " - make sure to tackle it first!")
    case "medium":
        print(reminder + " - try to complete it by today.")
    case "low":
        print(reminder + " - do it when you have time.")
    case _:
        print(f"Reminder: '{task}' has an unrecognized priority. Treat it as LOW priority.")

# Check time sensitivity
if time_bound == "yes":
    print("This is a time-sensitive task that requires immediate attention today!")
