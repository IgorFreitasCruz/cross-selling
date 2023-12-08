import pyodbc


class SQLServerDatabase:
    def __init__(self, configuration):
        self.connection_string = 'DRIVER={{ODBC Driver 17 for SQL Serve}};SERVER={},{};DATABASE={};UID={};PWD={};TrustServerCertificate=True'.format(
            configuration['MSSQL_HOSTNAME'],
            configuration['MSSQL_PORT'],
            configuration['MSSQL_DB'],
            configuration['MSSQL_USER'],
            configuration['MSSQL_PASSWORD'],
        )
        import sys

        print(
            '*' * 20,
            __name__,
            ': line',
            sys._getframe().f_lineno,
            '*' * 20,
            flush=True,
        )
        print(self.connection_string, flush=True)

    def connect(self):
        try:

            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()

            print('Connected to SQL Server')
        except Exception as e:
            print(f'Error connecting to SQL Server: {e}')

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f'Error executing query: {e}')
            return None

    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print('Disconnected from SQL Server')
        except Exception as e:
            print(f'Error disconnecting from SQL Server: {e}')


# Example usage:
# Replace the placeholder values with your actual SQL Server connection details
db = SQLServerDatabase(
    server='localhost',
    database='YourDatabaseName',
    username='sa',
    password='YourStrongPassword',
    port=1433,
)

db.connect()

# Example query
query = 'SELECT * FROM YourTableName'
result = db.execute_query(query)

if result:
    for row in result:
        print(row)

db.disconnect()
