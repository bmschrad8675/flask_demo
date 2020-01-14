# db_utils.py
import csv
import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.csv')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def populate_users():
    con = db_connect()
    cur = con.cursor()

    # Remove existing users table if exists
    cur.execute('DROP TABLE IF EXISTS users')

    # Create users table
    cur.execute("""
                CREATE TABLE users (
                    id integer PRIMARY KEY
                    , username text NOT NULL
                    , first_name text NOT NULL
                    , last_name text NOT NULL
                    , email text NOT NULL
                    , company_id integer NOT NULL
                    )
                """)

    # Template for inserting users
    users_sql = 'INSERT INTO users (username, first_name, last_name, email, company_id) VALUES (?, ?, ?, ?, ?)'

    # Loop through csv and insert
    with open(USERS_FILE, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            cur.execute(users_sql, (row[0], row[1],  row[2], row[3], row[4]))

    con.commit()
