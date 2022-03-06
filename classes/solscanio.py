import requests

class SolscanIO(object):
    """ Maintains a single session between this machine and TradeOgre.

    Specifying a key/secret pair is optional. If not specified, key and
    secret must be specified at the called method.

    Query responses, as received by :py:mod:`requests`, are retained
    as attribute :py:attr:`response` of this object. It is overwritten
    on each query.

    """
    def __init__(self, key=None, secret=None):
        """ Create an object with authentication information.

        :param key: (optional) key identifier for queries to the API
        :type key: str

        :param secret: (optional) actual private key used to sign messages
        :type secret: str

        :returns: None

        """
        self.key = key
        self.secret = secret
        self.uri = 'https://public-api.solscan.io'
        self.response = None
        return

    def getAccountTokens(self,sol_main_address):

        self.response = requests.get(self.uri + '/account/tokens?account=' + sol_main_address,headers = {"User-Agent": "Mozilla/5.0"})

        if(self.response.status_code == "200"):
            return self.response
        else:
            print(str(self.response.status_code))

    def getAccountTokensJSON(self, sol_main_address):
        self.response = requests.get(self.uri + '/account/tokens?account=' + sol_main_address,headers={"User-Agent": "Mozilla/5.0"})
        #print(self.response.json())
        #print(self.uri + '/account/tokens?account=' + sol_main_address)
        #self.response.close()
        if (self.response.status_code == "200" or self.response.status_code == 200):
            #print(self.response.text)
            return self.response.json()
        else:
            print(str(self.response.status_code))