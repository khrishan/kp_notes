import datetime
import pytz
import sqlite3

db = sqlite3.connect('accounts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS account (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)')
db.execute('CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))')

class Account(object):

    @staticmethod
    def _current_time():
        local_time = pytz.utc.localize(datetime.datetime.utcnow())
        return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute('SELECT name, balance FROM account WHERE (name=?)', (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print('Retrieved record for {}. '.format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute('INSERT INTO account VALUES(?, ?)', (name, opening_balance))
            cursor.connection.commit()

            print('Account created for {}. '.format(name), end='')
        
        self.show_balance()
        
    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            #self._balance += amount
            self._save_update(amount)

            print('{:.2f} deposited'.format(amount / 100))
        return self._balance / 100
    
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            #self._balance -= amount
            self._save_update(-amount)

            print('{:.2f} withdrawn'.format(amount / 100))
            return amount / 100
        else:
            print('The amount must be greater than zero and no more than your account balance!')
            return 0.0
    
    def show_balance(self):
        print('Balance on account {} is {:.2f}'.format(self.name, self._balance / 100))

    def _save_update(self, amount):
            new_balance = self._balance + amount
            deposit_time = Account._current_time()

            try:
                db.execute('UPDATE account SET balance = ? WHERE (name = ?)', (new_balance, self.name))
                db.execute('INSERT INTO history VALUES(?, ?, ?)', (deposit_time, self.name, amount))
            except sqlite3.Error:
                db.rollback()
            else:
                db.commit()
                self._balance = new_balance
                                

        
john = Account('John')
john.deposit(1010)
john.deposit(10)
john.deposit(10)
john.withdraw(30)
john.withdraw(0)
john.show_balance()

terry = Account('Terry')

graham = Account('Graham', 9000)

eric = Account('Eric', 7000)

db.close()