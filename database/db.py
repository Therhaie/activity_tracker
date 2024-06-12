import sqlite3
from datetime import datetime


## Basic function
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_activities_table = """
    CREATE TABLE IF NOT EXISTS activities (
        id integer PRIMARY KEY,
        name text NOT NULL,
        start_time text NOT NULL,
        end_time text
    );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_activities_table)
        print("table created")
    except sqlite3.Error as e:
        print(e)

def add_activity(conn, activity):
    sql = ''' INSERT INTO activities(name, start_time, end_time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (activity.name, activity.start_time, activity.end_time))
    conn.commit()
    print("activity added")
    return cur.lastrowid

def delete_activity(conn, id, table_name = 'activities'):
    condition = f"id = {id}"
    query = f"DELETE FROM {table_name} WHERE {condition}"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

## Data handling function

def retrieve_data(conn, activity, table_name = 'activities'):
    # sql = ''' SELECT * FROM activities.db WHERE name = {activity} '''
    query = f"SELECT * FROM {table_name} WHERE name = ?"
    cur = conn.cursor()
    cur.execute(query,(activity,))
    rows = cur.fetchall()
    return rows

def retrieve_name_activities(conn,table_name = 'activities'):
    cur = conn.cursor()
    query = f"SELECT DISTINCT name FROM {table_name}"
    cur.execute(query) # need to specify the database in case of multiple
    names = cur.fetchall()
    return names

def retrieve_all_data_between(conn, benning_date, ending_date = datetime.now(), table_name = 'activities'):
    query = f"SELECT * FROM {table_name} WHERE (start_time > ? AND end_time < ?)"
    cur = conn.cursor()
    cur.execute(query, (benning_date, ending_date))
    data = cur.fetchall()
    return data