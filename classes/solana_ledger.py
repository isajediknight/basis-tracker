import datetime

class Solana_Ledger:

    def __init__(self, solana_address=None, currencies=['USDC','basis','rBasis']):
        self.solana_address = solana_address
    
        self.amount = {}
        for i in currencies:
            self.amount[i] = []

    # Not supplying a timestamp assumes the current timestamp is when the data was captured
    def add_data(self,crypto=None, amount=None):
        self.amount[crypto].append(Attributes(crypto, amount))

    def add_data_with_timestamp(self,crypto=None, amount=None,timestamp=None):
        self.amount[crypto].append(Attributes(crypto, amount, timestamp))

    # Default {index} to -1 so it will combine the last amount to the second to the last amount
    def calc_compare_to_previous_amount(self,crypto,index = -1):
        # (index == 0 or index == -1) and
        if(len(self.amount[crypto]) < 2):
            return 0
        else:
            return self.amount[crypto][index].get_amount() - self.amount[crypto][index-1].get_amount()

    def get_amount(self,crypto,index = -1):
        return self.amount[crypto][index].get_amount()

    def get_timestamp(self,crypto,index = -1):
        return self.amount[crypto][index].get_timestamp()

class Attributes:
    def __init__(self, crypto=None, amount=None, timestamp=datetime.datetime.now()):
        # Default timestamp to the current timestamp this method was called at
        self.crypto = crypto
        self.amount = amount
        self.timestamp = timestamp

    def get_crypto(self):
        return self.crypto

    def get_amount(self):
        return self.amount

    def get_timestamp(self):
        return self.timestamp