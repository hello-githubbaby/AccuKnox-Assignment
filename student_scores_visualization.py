import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Simulated API response for student scores
# Assumption: API returns a list of students with name and score

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90},
    {"name": "Diana", "score": 78}
]
# Step 2: Display the fetched/simulated student scores
# - Prints each student's name and score to the console
print("Student Scores from API:\n")
for student in students:
    print(f"Name: {student['name']}, Score: {student['score']}")
# Step 3: Convert data to DataFrame
df = pd.DataFrame(students)

# Step 4: Calculate average score
average_score = df["score"].mean()

print("\nAverage Score:")
print(round(average_score, 2))
# Step 5: Create bar chart for student scores
plt.figure()
plt.bar(df["name"], df["score"])

plt.xlabel("Student Name")
plt.ylabel("Score")
plt.title("Student Test Scores")

plt.show()

