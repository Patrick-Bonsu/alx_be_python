
# Prompt user for task information
task = input("Enter your task for today: ")
priority = input("Set the task priority (high, medium, low):").lower()
time_bound = input("Is the task time-bound? (yes or no):").lower()

# Reminder message base
reminder = f"Reminder: '{task}' is a {priority.upper()} priority task"

# Match-case based on priority
match priority:
    case "high":
        print(reminder + " - make sure to tackle it first!")
    case "medium":
        print(reminder + " - try to complete it by today.")
    case "low":
        print(reminder + " - do it when you have time.")
    case _:
        print("Unrecognized priority level. Defaulting to LOW.")
        print(f"Reminder: '{task}' is a LOW priority task - do it when you can.")

# Modify message if task is time-sensitive
if time_bound == "yes":
    print("This is a time-sensitive task that requires immediate attention today!")
