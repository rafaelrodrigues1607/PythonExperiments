def connect_to_database(db_url):
    import sqlite3
    connection = sqlite3.connect(db_url)
    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    connection.commit()
    return cursor

def fetch_all_results(cursor):
    return cursor.fetchall()

def close_connection(connection):
    connection.close()