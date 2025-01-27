import os
import psycopg2
from dotenv import load_dotenv
import datetime

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# database connection
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Connected to the database successfully!")
except Exception as e:
    print(f"Error connecting to the database: {e}")


def query_old_records(conn, days):
    cursor = conn.cursor()
    query = """
    SELECT * FROM records
    WHERE date < %s;
    """
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    cursor.execute(query, (cutoff_date,))
    records = cursor.fetchall()
    cursor.close()
    return records