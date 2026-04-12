# Megan McCaw
# April 12, 2026
# P4HW1
# This program will take a user input of scores, drop the lowest score, and calculate the average of the remaining scores and print the letter grade.

# Ask user how many scores they will be entering
number_of_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list to store the scores
score_list = [] 

# For loop to get score input and make sure the score is valid (between 0 and 100)
for i in range(number_of_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    # While loop to keep asking for a valid score until the user enters a score between 0 and 100
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input(f"Re-enter score #{i + 1}: "))
# Use append method to add valid scores to the list
    score_list.append(score)

# Find the lowest score in the list
lowest_score = min(score_list)

# Symbol for result formatting
sym = "-"

# Print the results
print(f"{sym * 14}Results{sym * 14}")
print(f"{'Lowest score':15}: {lowest_score:.1f}")

# Remove the lowest score from the list
score_list.remove(lowest_score)

# Print the modified list of scores, calculate the average, and determine the letter grade
print(f"{'Modified List':15}: {score_list}")
average_score = sum(score_list) / len(score_list)
print(f"{'Scores Average':15}: {average_score:.2f}")

# If-elif-else statement to determine letter grade based on average score
if average_score >= 90:
    print(f"{'Grade':15}: A")
elif average_score >= 80:
    print(f"{'Grade':15}: B")
elif average_score >= 70:    
    print(f"{'Grade':15}: C")
elif average_score >= 60:    
    print(f"{'Grade':15}: D")
else:
    print(f"{'Grade':15}: F")

print(f"{sym * 35}")

