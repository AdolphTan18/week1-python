#📋 Lists & Sorting
#1. The Sari-Sari Inventory You own a sari-sari store. You have this list of items:
#python

#inventory = ["Skyflakes", "Milo", "Tender Juicy", "Chippy", "C2", "Oishi", "Lucky Me"]
#Print the list in alphabetical order
#Print it in reverse alphabetical order
#Print only items whose names are longer than 4 characters
#I want to start with this first

#----------------------------------------------

#Understand
# TASK 1: Print the list in alphabetical order
# TASK 2: print it in reverse alphabetical order
# TASK 3: print only items whose names are longer than 4 characters

#Plan
# - Take inventory list
# - Sort it alphabetically and print

# - Take inventory list
# - Sort it in reverse alphabetical order and print

# - Take inventory list
# - if the item's name is longer than 4 chracters, print it

#Code

#Task 1
inventory = ["Skyflakes", "Milo", "Tender Juicy", "Chippy", "C2", "Oishi", "Lucky Me"]
for item in sorted(inventory):
    print(item)

#for item in inventory:
#    sorted_inventory = sorted(inventory)
#    print(sorted_inventory)


#Task 1.1
sorted_inventory = sorted(inventory)
print("")
print(sorted_inventory[0])
print(sorted_inventory[1])
print(sorted_inventory[2])
print(sorted_inventory[3])
print(sorted_inventory[4])
print(sorted_inventory[5])
print(sorted_inventory[6])
print("")

#Task 1.2
#None whatsoever

#Task 2
for item in sorted(inventory, reverse=True):
    print(item)
print("")

#Task 3
for item in inventory:
    if len(item) > 4:
        print(item)
print("")
