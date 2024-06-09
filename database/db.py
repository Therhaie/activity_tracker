import sqlite3

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
    except sqlite3.Error as e:
        print(e)

def add_activity(conn, activity):
    sql = ''' INSERT INTO activities(name, start_time, end_time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (activity.name, activity.start_time, activity.end_time))
    conn.commit()
    return cur.lastrowid

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