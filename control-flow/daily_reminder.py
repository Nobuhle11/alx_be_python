# daily_reminder.py

# Get task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide customized message based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == "yes":
            message = f"Note: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a medium priority task. Consider completing it when you have free time."
    case "low":
        if time_bound == "yes":
            message = f"Note: '{task}' is a low priority task that requires immediate attention today!"
        else:
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"'{task}' has an unknown priority level."

# Print the final reminder
print("\n" + message)
