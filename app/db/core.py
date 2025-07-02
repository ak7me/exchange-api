import sqlite3 as sq

def get_connection():
    connection = sq.connect("/Users/ivan/Desktop/010.python-exchange/app/db/exchange.db")
    connection.row_factory = sq.Row
    return connection

def init_db() -> None:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Currencies (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Code TEXT NOT NULL UNIQUE,
        FullName TEXT NOT NULL,
        Sign TEXT NOT NULL                      
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExchangeRates (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        BaseCurrencyId INTEGER UNIQUE,
        TargetCurrencyId INTEGER UNIQUE,
        Rate REAL NOT NULL,
        FOREIGN KEY (BaseCurrencyId)  REFERENCES Currencies (ID),
        FOREIGN KEY (TargetCurrencyId)  REFERENCES Currencies (ID)
        )
        ''')

def get_all():
    with get_connection() as connection:
        cursor = connection.cursor()
        return cursor.execute("SELECT * FROM Currencies").fetchall()
    
# with get_connection() as connection:
#     cursor = connection.cursor()
#     print(cursor.execute("SELECT * FROM Currencies").fetchall())
#     print(cursor.execute(f"SELECT * FROM Currencies WHERE Code = 'USD'").fetchall())

# init_db()

