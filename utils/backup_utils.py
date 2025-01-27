import datetime
import csv

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

def write_backup(records):
    filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'data', 'date'])  # Adjust columns as needed
        writer.writerows(records)
    print(f"Backup written to {filename}")

def delete_old_records(conn, days):
    cursor = conn.cursor()
    query = """
    DELETE FROM records
    WHERE date < %s;
    """
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    cursor.execute(query, (cutoff_date,))
    conn.commit()
    cursor.close()
    print("Old records deleted")