# Imagine this is a seperate file

import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = 'anotherupdate@update.com'
phone = input('Please enter your phone number : ')

update_sql = 'UPDATE Contact SET email = ? WHERE phone = ?' # ? are placeholders, library looks after putting stuff in quotes
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone)) # this statement only allows to run one statement at a time.
print('{} rows updated.'.format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

# It is better to do it this way so that you keep your code compact.
# Also knows what code to commit, as you could have seperate connections.


for row in db.execute('SELECT * FROM Contact'): # how to connect to db without cursor
    print(row)

for name, phone, email in db.execute('SELECT * FROM Contact'): # how to connect to db without cursor
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# You'll get nothing printed!

# Nothing is made permanent until you 'commit'

# SELECT * FROM sqlite_master - gives you all the information about the tables in the sqlite db.

# Challenge

# How to pass one single variable in a tuple?
# (name, ) <-- this ensures that this is a tuple