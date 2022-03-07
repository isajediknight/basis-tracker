import datetime

class Solana_Ledger:

    def __init__(self, solana_address=None, currencies=['USDC','Basis','rBasis']):
        self.solana_address = solana_address
    
        self.amount = {}
        for i in currencies:
            self.amount[i] = []

    # Not supplying a timestamp assumes the current timestamp is when the data was captured
    def add_data(self,crypto=None, amount=None):
        self.amount[i].append(Attributes(crypto, amount))

    def add_data_with_timestamp(self,crypto=None, amount=None,timestamp=None):
        self.amount[i].append(Attributes(crypto, amount, timestamp))

    class Attributes:
        def __init__(self, crypto=None, amount=None, timestamp=datetime.datetime.now()):
            self.crypto = crypto
            self.amount = amount
            self.timestamp = timestamp

        def get_crypto(self):
            return self.crypto

        def get_amount(self):
            return self.amount

        def get_timestamp(self):
            return self.timestamp