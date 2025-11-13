# pattern_drawing.py
# Objective: Draw a square pattern using nested loops

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns (printing asterisks on the same line)
    for col in range(size):
        print("*", end="")
    # Move to the next line after one row
    print()
    # Increment row counter
    row += 1

