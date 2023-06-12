import os

# Function to clear the database
def clear_database(db_file):
    if os.path.exists(db_file):
        os.remove(db_file)
        print("Database cleared.")
    else:
        print("Database does not exist.")
