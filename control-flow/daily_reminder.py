# daily_reminder.py

# Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start with a base reminder
reminder = ""

# Match-case for priority handling
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"'{task}' has an unknown priority level."

# Modify if task is time-bound and not already low-priority
if time_bound == "yes" and priority in ["high", "medium"]:
    reminder += " that requires immediate attention today!"

# Final output
print("\n" + reminder)
