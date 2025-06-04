# pattern_drawing.py

# Ask user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
