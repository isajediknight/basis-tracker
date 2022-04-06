
import datetime


def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

def add_commas(string):
    negative_found = False
    if('-' == string[0]):
        negative_found = True
        string = string[1:]

    length = len(string)

    counter = 0
    fixed_string = ''
    for char in reversed(string):
        fixed_string += char
        counter += 1
        if counter == length:
            pass
        elif counter % 3 == 0:
            fixed_string += ','

    new_string = ''
    for char in reversed(fixed_string):
        new_string += char

    if(negative_found):
        new_string = '-' + new_string

    return new_string

class Accounts:

    def __init__(self,accounts=None,currencies=['USDC','basis','rBasis','USD Coin']):

        self.accounts = {}
        self.currencies = currencies

        if type(accounts) == type(''):
            comma_count = len(list(find_all(accounts,',')))
            for account in list(find_all(accounts)).split(','):
                self.accounts[account] = []
        elif type(accounts) == type([]):
            for account in accounts:
                self.accounts[account] = []
        elif type(accounts) == type({}):
            for account in list(accounts.keys()):
                self.accounts[account] = []

    def add_data(self,account,address,currency,amount):
        self.accounts[account].append(Account(account,address,currency,amount))

    def add_data_current_timestamp(self,account,address,currency,amount):
        self.accounts[account].append(Account(account,address,currency,amount))

    def add_data_current_timestamp_compare_previous(self,account,address,currency,amount):
        self.accounts[account].append(Account(account,address,currency,amount))

        previous = 0

        if len(self.accounts[account]) > 1:
            previous = self.accounts[account][-2].get_amount(account)

        return (amount - previous)

    def add_data_compare_to_previous(self,account,address,currency,amount):
        self.accounts[account].append(Account(account,address,currency,amount))

        previous = 0

        if len(self.accounts[account]) > 1:
            previous = self.accounts[account][-2].get_amount()

        return (amount - previous)

    def add_data_add_timestamp(self,account,address,currency,amount,timestamp):
        self.accounts[account].append(Account(account,address,currency,amount,timestamp))

    def add_data_add_timestamp_compare_previous(self,account,address,currency,amount,timestamp):
        self.accounts[account].append(Account(account,address,currency,amount,timestamp))

        previous = 0

        if len(self.accounts[account]) > 1:
            previous = self.accounts[account][-2].get_amount()

        return (amount - previous)

    def get_currency(self,account,index):
        return self.accounts[account][index].get_currency

    def get_amount(self,account,index):
        return self.accounts[account][index].get_amount

    def get_timestamp(self,account,index):
        return self.accounts[account][index].get_timestamp

    def get_address(self,account,index):
        return self.accounts[account][index].get_address

    def get_account(self,account,index):
        return self.accounts[account][index].get_account
    
    def print_data(self,account,index):
        out_string = "Account: " + account + '\tCurrency: ' + self.accounts[account][index].get_currency() + '\tAmount: ' + str(self.accounts[account][index].get_amount())
        out_string += '\tAddress: ' + self.accounts[account][index].get_address() + '\tTimestamp: ' + self.accounts[account][index].get_timestamp().strftime("%m/%d/%Y %I:%M:%S %p")
        print(out_string)

class Account:
    def __init__(self,account=None,address=None,currency=None,amount=None,timestamp=datetime.datetime.now()):
        self.currency = currency
        self.amount = amount
        self.timestamp = timestamp
        self.address = address
        self.account = account

    def get_currency(self):
        return self.currency

    def get_amount(self):
        return self.amount

    def get_timestamp(self):
        return self.timestamp

    def get_address(self):
        return self.address

    def get_account(self):
        return self.account