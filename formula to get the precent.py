# Get user input for the total number of items
total_numbers = int(input("Enter the total number of items: "))

# Iterate over the range starting from 100% down to 0%
for i in range(total_numbers, -1, -1):
    current_percentage = int((i / total_numbers) * 100)
    print(f"Number: {i}, Percentage: {current_percentage}%")
    # Your code logic here
