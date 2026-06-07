
sales = {
    "Skyflakes": 12,
    "Milo": 5,
    "Tender Juicy": 8,
    "Chippy": 20,
    "C2": 3,
    "Oishi": 15,
    "Lucky Me": 7
}

#Understand
#TASK 1: Open the dictionary and print out the sales of the most popular snack.
#TASK 2: Open the dictionary and print out the sales of the least popular snack.
#TASK 3: Open the dictionary and print out the sales of the snack with the name
#         that starts with the letter "C".
#TASK 4: Print out the the top 2
#TASK 5: Print out the the bottom 2
#TASK 6: Print out the average sales of all the snacks.
#TASK 7: Print out the total sales of all the snacks.
#TASK 8: Print the snacks sorted by sales, highest to lowest
#TASK 9: Print what percentage of total sales each snack represents (e.g., Chippy: 28.6%)
#TASK 10: Find out if any snack sold exactly the average amount

#Plan

# SHARED SETUP (computed once, reused by several tasks below)
# - Add up all the sales to get the total      -> used by Tasks 6, 7, 9, 10
# - Divide that total by the number of snacks
#   to get the average                          -> used by Tasks 6, 10
# - Sort the snacks by sales, highest to lowest -> used by Tasks 4, 5, 8

# TASK 1
# Take the sales dictionary
# Find the snack with the highest sales
# Print it

# TASK 2
# Take the sales dictionary
# Find the snack with the lowest sales
# Print it

# TASK 3
# Take the sales dictionary
# Search for the snack whose name starts with "C"
# Print it and its sales

# TASK 4
# Take the snacks already sorted highest-to-lowest (shared setup)
# Take the first 2 from that sorted order
# Print them

# TASK 5
# Take the snacks already sorted highest-to-lowest (shared setup)
# Take the last 2 from that sorted order
# Print them

# TASK 6
# Use the average from the shared setup
# Print it

# TASK 7
# Use the total from the shared setup
# Print it

# TASK 8
# Take the snacks already sorted highest-to-lowest (shared setup)
# Print each snack in that order

# TASK 9
# Use the total from the shared setup
# For each snack, divide its sales by the total to get its share
# Convert that share into a percentage and print it next to the snack's name

# TASK 10
# Use the average from the shared setup
# Check if any of the snacks matches the average sales number
# If it does match, print it out
# If none match, do not print anything

