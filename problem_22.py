# Step 1: Read the contents of the text file
with open("problem_22_names.txt", "r") as file:
    names = file.read().replace('"', '').split(",")

# Step 2: Sort the list of names into alphabetical order
names.sort()

# Step 3: Define a function to calculate alphabetical value for a name
def alphabetical_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

# Step 4: Calculate the name scores
total_score = 0
for i, name in enumerate(names, 1):
    score = alphabetical_value(name) * i
    total_score += score

# Step 5: Print the total of all name scores
print("Total of all name scores:", total_score)
