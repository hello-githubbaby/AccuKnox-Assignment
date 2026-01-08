import requests
import sqlite3

# Step 1: API URL
API_URL = "https://openlibrary.org/subjects/programming.json?limit=5"

# Step 2: Send GET request
response = requests.get(API_URL)

# Step 3: Check if request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()

    print("Books fetched from API:\n")

    # Step 4: Display book details
    for book in data.get("works", []):
        title = book.get("title", "N/A")
        authors = book.get("authors", [])
        author_names = ", ".join([a.get("name", "Unknown") for a in authors])
        year = book.get("first_publish_year", "N/A")

        print(f"Title : {title}")
        print(f"Author: {author_names}")
        print(f"Year  : {year}")
        print("-" * 40)

    # Step 5: Connect to SQLite database
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Step 6: Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)

    # Step 7: Insert book data into table
    for book in data.get("works", []):
        title = book.get("title", "N/A")
        authors = book.get("authors", [])
        author_names = ", ".join([a.get("name", "Unknown") for a in authors])
        year = book.get("first_publish_year", None)

        cursor.execute(
            "INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
            (title, author_names, year)
        )

    conn.commit()
    conn.close()

    print("\nBook data successfully stored in SQLite database.")

else:
    print("Failed to fetch data from API")
# Step 8: Read data back from the database
print("\nBooks read from SQLite database:\n")

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("SELECT title, author, publication_year FROM books")
rows = cursor.fetchall()

for row in rows:
    title, author, year = row
    print(f"Title : {title}")
    print(f"Author: {author}")
    print(f"Year  : {year}")
    print("-" * 40)

conn.close()
