import sqlite3

print(sqlite3.sqlite_version)

db = sqlite3.connect('contacts.sqlite')

db.execute('CREATE TABLE IF NOT EXISTS Contact (name TEXT, phone TEXT, email TEXT)')
db.execute('INSERT INTO Contact (name, phone, email) VALUES ("KP", "0123456", "kp@email.com")')
db.execute('INSERT INTO Contact (name, phone, email) VALUES ("Tim", "6546792", "tim@email.com")')
db.execute('INSERT INTO Contact (name, phone, email) VALUES ("Brian", "7983274892", "brian@email.com")')

cursor = db.cursor()

cursor.execute('SELECT * FROM Contact') # Don't need a ;

# for row in cursor:
#     print(row)

# print(cursor.fetchall()) # fetches all of them in one list

# print(cursor.fetchone()) # returns first row in tuple form
# print(cursor.fetchone()) # returns second row in tuple form
# print(cursor.fetchone()) # returns third row in tuple form
# print(cursor.fetchone()) # returns None

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# Cursor has reached the end. So in order to restart the cursor, you would have to re-run the query again.

db.commit() # Do this in order to save your changes to the database

db.close()