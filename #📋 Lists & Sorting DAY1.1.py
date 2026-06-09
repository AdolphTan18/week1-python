# Github test
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
#TASK 3: Open the dictionary and print out the sales of the snack with the name that starts with the letter "C".
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

total = sum(sales.values())
average = total/len(sales)
sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)

print("TASK 1")
print("Take the sales dictionary")
print("Find the snack with the highest sales")
print("Print it")

top_snack = max(sales, key=sales.get)
print("Output:",top_snack, sales[top_snack]) # prints the top snack and its sales
print("")

print("TASK 2")
print("Take the sales dictionary")
print("Find the snack with the lowest sales")
print("Print it")

least_snack = min(sales, key=sales.get)
print("Output:",least_snack, sales[least_snack])
print("")

print("TASK 3")
print("Take the sales dictionary")
print("Search for the snack whose name starts with C")

# Print it and its sales
for snack in sales:
    if snack.startswith("C"):
        print("Output:",snack, sales[snack])
print("")

print("TASK 4")
print("Take the first 2 from the sorted order")

for snack, number in sorted_sales[:2]:
    print(f"Top 2 snacks: {snack} with {number} sales")
print("")

print("TASK 5")
print("Take the last 2 from the sorted order")

for snack, number in sorted_sales[-2:]:
    print(f"Bottom 2 snacks: {snack} with {number} sales")
print("")

print("TASK 6")
print("Average sales:")
print(average)
print("")

print("TASK 7")
print("Total sales:")
print(total)
print("")

print("TASK 8")
print("Take the snacks already sorted highest-to-lowest (shared setup)")
print("Print each snack in that order")

print("Higest to lowest")
for snack, number in sorted_sales[:10]:
    print(f" {snack} with {number} sales")
print("")

print("TASK 9")
print("Percentage of total sales:")
print("Use the total from the shared setup")
print("For each snack, divide its sales by the total to get its share")
print("Convert that share into a percentage and print it next to the snack's name")

for snack, number in sorted_sales:
    percentage = round(number/total*100, 2)
    #print(snack, percentage)
    print(f"{snack}: {percentage}%")
print("")

print("TASK 10")
# Use the average from the shared setup
# Check if any of the snacks matches the average sales number
# If it does match, print it out
# If none match, do not print anything

for snack, number in sorted_sales:
    if number==average:
        print(snack)
else:
    print("None")

