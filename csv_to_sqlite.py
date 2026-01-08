# Step 1: Import pandas library
import pandas as pd

# Step 2: Read CSV file into a DataFrame with proper encoding
df = pd.read_csv("users.csv", encoding="utf-8-sig")  # Handles BOM / Excel exports
# Step 3: Display the data to verify it is read correctly
print("User Data from CSV:\n")
print(df)

# Step 3: Import sqlite3 (built-in Python library)
import sqlite3

# Step 4: Connect to SQLite database (creates 'users.db' if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Step 5: Create 'users' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

# Step 6: Insert CSV data into the database
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (row['name'], row['email'])
    )

# Commit changes and close the connection
conn.commit()
conn.close()

print("\nCSV data successfully imported into SQLite database 'users.db'.")



