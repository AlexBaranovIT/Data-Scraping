# Import necessary libraries
import requests
import sqlite3

# Define constants
API_BASE_URL = "https://api.example.com"
DB_FILE = "data.db"


# Function to fetch data from the API
def fetch_data():
    try:
        response = requests.get(f"{API_BASE_URL}/data")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return []


# Function to create and initialize a SQLite database
def initialize_database():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value INTEGER
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")

# Function to store data in the database
def store_data(data):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        for item in data:
            cursor.execute("INSERT INTO data (name, value) VALUES (?, ?)", (item["name"], item["value"]))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error storing data in the database: {e}")

# Main function to run the program
def main():
    initialize_database()
    data = fetch_data()
    if data:
        store_data(data)
        print("Data successfully fetched and stored in the database.")
    else:
        print("No data fetched from the API.")

if __name__ == "__main__":
    main()
