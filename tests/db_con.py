import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname='elddwomh',
    user='elddwomh',
    password='skgUevkZBiCtyZndoLUMgKK_NPDC90aD',
    host='abul.db.elephantsql.com',
    port='5432'
)

try:
    # Test the connection by executing a query
    cursor = conn.cursor()
    cursor.execute('SELECT version()')
    server_version = cursor.fetchone()
    print('PostgreSQL server version:', server_version)
finally:
    # Close the connection
    conn.close()
