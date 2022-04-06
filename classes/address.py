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

class Addresses:
    def __init__(self,addresses=None,currencies=['USDC','basis','rBasis','USD Coin']):

        self.addresses = {}
        self.currencies = currencies

        if type(addresses) == type(''):
            comma_count = len(list(find_all(addresses)))
            for address in list(find_all(addresses)).split(','):
                self.addresses[address] = Address(address,currencies)
        elif type(addresses) == type([]):
            for address in addresses:
                self.addresses[address] = Address(address,currencies)
        elif type(addresses) == type({}):
            for address in list(adresses.keys()):
                self.addresses[address] = Address(address,currencies)

    def add_data(self,address,crypto=None, amount=None):
        self.addresses[address].add_data(crypto,amount)

    def add_data_with_timestamp(self,address,crypto=None, amount=None, timestamp=datetime.datetime.now()):
        self.addresses[address].add_data(crypto,amount,timestamp)

    def get_timestamp(self,address,crypto,index=0):
        return self.addresses[address].get_timestamp(crypto,index)

    def get_amount(self,address,crypto,index=0):
        return self.addresses[address].get_amount(crypto,index)

    def print_data(self,address,crypto,index=0):
        self.addresses[address].print_data(address,crypto,index)

    def add_data_compare_to_previous(self,address,crypto=None, amount=None):
        #print("Amount: " + str(amount) + "\t" + crypto)
        return self.addresses[address].add_data_compare_to_previous(crypto,amount)

class Address:
    def __init__(self, address=None, currencies=['USDC','basis','rBasis','USD Coin']):
        self.address = address
        self.currencies = currencies

        # Catch All
        self.currency_unknown = {}

        if 'USDC' in self.currencies:
            self.currency_usdc = {}

        if 'basis' in self.currencies:
            self.currency_basis = {}
        
        if 'rBasis' in self.currencies:
            self.currency_rbasis = {}

        if 'USD Coin' in self.currencies:
            self.currency_usd_coin = {}

    # Not supplying a timestamp assumes the current timestamp is when the data was captured
    def add_data(self,crypto=None, amount=None):
        if 'USDC' == crypto:
            self.currency_usdc[len(self.currency_usdc)] = Attributes(crypto,amount)
        elif 'basis' == crypto:
            self.currency_basis[len(self.currency_basis)] = Attributes(crypto,amount)
        elif 'rBasis' == crypto:
            self.currency_rbasis[len(self.currency_rbasis)] = Attributes(crypto,amount)
        elif 'USD Coin' == crypto:
            self.currency_usd_coin[len(self.currency_usd_coin)] = Attributes(crypto,amount)
        else:
            self.currency_unknown[len(self.currency_unknown)] = Attributes(crypto,amount)

    def add_data_with_timestamp(self,crypto=None, amount=None,timestamp=None):
        if 'USDC' in currencies:
            self.currency_usdc[len(self.currency_usdc)] = Attributes(crypto, amount, timestamp)
        elif 'basis' in currencies:
            self.currency_basis[len(self.currency_basis)] = Attributes(crypto, amount, timestamp)
        elif 'rBasis' in currencies:
            self.currency_rbasis[len(self.currency_rbasis)] = Attributes(crypto, amount, timestamp)
        elif 'USD Coin' in currencies:
            self.currency_usd_coin[len(self.currency_usd_coin)] = Attributes(crypto, amount, timestamp)
        else:
            self.currency_unknown[len(self.currency_unknown)] = Attributes(crypto, amount, timestamp)

    # Not supplying a timestamp assumes the current timestamp is when the data was captured
    def add_data_compare_to_previous(self,crypto=None, amount=None):

        if 'USDC' == crypto:
            self.currency_usdc[len(self.currency_usdc)] = Attributes(crypto,amount)
            index = len(self.currency_usdc)
            if len(self.currency_usdc) > 1:
                return self.currency_usdc[index-1].get_amount() - self.currency_usdc[index-2].get_amount()
            else:
                return 0
        elif 'basis' == crypto:
            self.currency_basis[len(self.currency_basis)] = Attributes(crypto,amount)
            index = len(self.currency_basis)
            if len(self.currency_basis) > 1:
                return self.currency_basis[index-1].get_amount() - self.currency_basis[index - 2].get_amount()
            else:
                return 0
        elif 'rBasis' == crypto:
            self.currency_rbasis[len(self.currency_rbasis)] = Attributes(crypto,amount)
            index = len(self.currency_rbasis)
            if len(self.currency_rbasis) > 1:
                return self.currency_rbasis[index-1].get_amount() - self.currency_rbasis[index - 2].get_amount()
            else:
                return 0
        elif 'USD Coin' == crypto:
            self.currency_usd_coin[len(self.currency_usd_coin)] = Attributes(crypto,amount)
            index = len(self.currency_usd_coin)
            if len(self.currency_usd_coin) > 1:
                return self.currency_usd_coin[index-1].get_amount() - self.currency_usd_coin[index - 2].get_amount()
            else:
                return 0
        else:
            self.currency_unknown[len(self.currency_unknown)] = Attributes(crypto,amount)
            index = len(self.currency_unknown)
            if len(self.currency_unknown) > 1:
                return self.currency_unknown[index-1].get_amount() - self.currency_unknown[index - 2].get_amount()
            else:
                return 0

    # Default {index} to -1 so it will combine the last amount to the second to the last amount
    def calc_compare_to_previous_amount(self,crypto,index):

        if 'USDC' == crypto:
            if len(self.currency_usdc) > 1:
                return self.currency_usdc[index].get_amount() - self.currency_usdc[index-1].get_amount()
            else:
                return 0
        elif 'basis' == crypto:
            if len(self.currency_basis) > 1:
                return self.currency_basis[index].get_amount() - self.currency_basis[index-1].get_amount()
            else:
                return 0
        elif 'rBasis' == crypto:
            if len(self.currency_rbasis) > 1:
                return self.currency_rbasis[index].get_amount() - self.currency_rbasis[index - 1].get_amount()
            else:
                return 0
        elif 'USD Coin' == crypto:
            if len(self.currency_usd_coin) > 1:
                return self.currency_usd_coin[index].get_amount() - self.currency_usd_coin[index - 1].get_amount()
            else:
                return 0
        else:
            if len(self.currency_unknown) > 1:
                return self.currency_unknown[index].get_amount() - self.currency_unknown[index - 1].get_amount()
            else:
                return 0

    def get_amount(self,crypto,index = -1):
        if 'USDC' == crypto:
            return self.currency_usdc[index].get_amount()
        elif 'basis' == crypto:
            return self.currency_basis[index].get_amount()
        elif 'rBasis' == crypto:
            return self.currency_rbasis[index].get_amount()
        elif 'USD Coin' == crypto:
            return self.currency_usd_coin[index].get_amount()
        else:
            return self.currency_unknown[index].get_amount()

    def get_account(self,crypto,index = -1):
        if 'USDC' == crypto:
            return self.currency_usdc[index].get_account()
        elif 'basis' == crypto:
            return self.currency_basis[index].get_account()
        elif 'rBasis' == crypto:
            return self.currency_rbasis[index].get_account()
        elif 'USD Coin' == crypto:
            return self.currency_usd_coin[index].get_account()
        else:
            return self.currency_unknown[index].get_account()

    def get_timestamp(self,crypto,index = -1):
        if 'USDC' == crypto:
            return self.currency_usdc[index].get_amount()
        elif 'basis' == crypto:
            return self.currency_basis[index].get_amount()
        elif 'rBasis' == crypto:
            return self.currency_rbasis[index].get_amount()
        elif 'USD Coin' == crypto:
            return self.currency_usd_coin[index].get_amount()
        else:
            return self.currency_unknown[index].get_amount()

    def print_data(self,address,crypto,index):
        if 'USDC' == crypto:
            self.currency_usdc[index].print_data(address)
        elif 'basis' == crypto:
            self.currency_basis[index].print_data(address)
        elif 'rBasis' == crypto:
            self.currency_rbasis[index].print_data(address)
        elif 'USD Coin' == crypto:
            self.currency_usd_coin[index].print_data(address)
        else:
            self.currency_unknown[index].print_data(address)

class Attributes:
    def __init__(self, crypto=None, amount=None, account=None, timestamp=datetime.datetime.now()):
        # Default timestamp to the current timestamp this method was called at
        # account represents tokenAccount

        if type(crypto) == type(None):
            self.crypto = 'Unknown'
        else:
            self.crypto = crypto

        if type(amount) == type(None):
            self.amount = 0
        else:
            self.amount = amount

        if type(account) == type(None):
            self.account = 'Unknown'
        else:
            self.account = account

        if type(timestamp) == type(None):
            self.timestamp = datetime.datetime.now()
        else:
            self.timestamp = timestamp

    def get_crypto(self):
        return self.crypto

    def get_amount(self):
        return self.amount

    def get_account(self):
        return self.account

    def get_timestamp(self):
        return self.timestamp

    def print_data(self,address):
        print(address[0:4] + '...' + address[-5:-1]+"\tCrypto:"+self.crypto+'\t'+"Amount:"+add_commas(str(self.amount))+'\t'+"Timestamp:"+str(self.timestamp.strftime("%m/%d/%Y %I:%M:%S %p")))