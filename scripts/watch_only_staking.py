import datetime,time,os,sys

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    MODULES_GITHUB_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\github\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    MODULES_GITHUB_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/github/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    sys.path.insert(0,'../classes/')
    sys.path.insert(0,MODULES_DIR)
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0,MODULES_DIR)

# < --- Begin Module Classes Import --- >
from discord_webhook import *
# < ---  End  Module Classes Import --- >

#from discord_webhook import DiscordWebhook
#webhook ID
#https://discord.com/api/webhooks/953101017556336660/942Mm_yoH4UAKEvib59ZsD51KPFw7ucgGOibhtU3G4gVfLwFJsikyt87Nl1EB0XgqGX5

# < --- Begin Custom Classes Import --- >
# Custom Colors for printing to the screen
from custom_colors import *

# Record time for all the things
from benchmark import *

# Interact with the Solana API
from solscanio import *

# Record amounts of crypto from addresses
from solana_ledger import *

from custom_string import *
# < --- End Custom Classes Import --- >



begin_time = Benchmark()

color_test = ColoredText(['datatype'], ['38;5;30m'])

first_api_call = SolscanIO()
second_api_call = SolscanIO()

# Hardcode Important Addresses to watch here - for easier trading out
ADDRESS_ORCA = '786ezhfHqkmJUBmjrWYGpzPnVWR8zhy2V71qNws7D89z'
ADDRESS_3S = 'HXCJ1tWowNNNUSrtoVnxT3y9ue1tkuaLNbFMM239zm1y'

address_1 = ADDRESS_3S # ''# '3sBX8hj4URsiBCSRV26fEHkake295fQnM44EYKKsSs51'#'HXCJ1tWowNNNUSrtoVnxT3y9ue1tkuaLNbFMM239zm1y'
#'2g4joCYzR3QA3SDypr6SJWzgnQX5xUpBF463rvJJfw78')
address_2 = ADDRESS_ORCA

addr_1_tracking = ''
if(address_1 == ADDRESS_ORCA):
    print('\n Tracking Orca Address: https://solscan.io/account/' + address_1 + '#tokenAccounts')
    addr_1_tracking = 'Orca'
elif(address_1 == ADDRESS_3S):
    print('\n Tracking 3S Address: https://solscan.io/account/' + address_1 + '#tokenAccounts')
    addr_1_tracking = '3S'

print("")

account_1 = Solana_Ledger(address_1)

watching = ['rBasis','basis','usdc']#'USD Coin'

for runs in range(0,5000):
    result_1 = first_api_call.getAccountTokensJSON(address_1)
    #print(result_1)
    api_benchmark = Benchmark()
    for i in range(len(result_1)):
        #print(result_1[i]['tokenName'])

        if result_1[i]['tokenName'] in watching:
            TOKEN_NAME = result_1[i]['tokenName']
            #print(result_1[i]['tokenName'] + ':' + str(int(result_1[i]['tokenAmount']['uiAmount'])))
            account_1.add_data(TOKEN_NAME,int(result_1[i]['tokenAmount']['uiAmount']))
            previous_difference = account_1.calc_compare_to_previous_amount(TOKEN_NAME)

            hours = str(datetime.datetime.now().hour)
            minutes = str(datetime.datetime.now().minute)
            seconds = str(datetime.datetime.now().second)

            previous_difference_str = Custom_String(previous_difference)
            previous_difference_str.add_commas()

            if(previous_difference > 0):
                print(' ' + color_test.cc(addr_1_tracking,'orange') + '\t' +  TOKEN_NAME + '\t' + hours + ':' + minutes + ':' + seconds + '\t' + color_test.cc(previous_difference_str.get_string(),'green'))
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/HIDDEN',content='+' + previous_difference_str.get_string())
                response = webhook.execute()
            elif(previous_difference < 0):
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/HIDDEN',content = previous_difference_str.get_string())
                response = webhook.execute()
                print(' ' + color_test.cc(addr_1_tracking,'orange') + '\t' + TOKEN_NAME + '\t' + hours + ':' + minutes + ':' + seconds + '\t' + color_test.cc(previous_difference_str.get_string(),'red'))

    api_benchmark.stop()

    #print(str(api_benchmark.get_runtime_seconds()))

    if(api_benchmark.get_runtime_seconds() >= 10):
        text = api_benchmark.human_readable_string()
        print(color_test.cc(' API Call took: ' + text,'yellow'))
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/HIDDEN',content='API Call took: ' + text)
        response = webhook.execute()
    elif(api_benchmark.get_runtime_seconds() < 10 and api_benchmark.get_runtime_seconds() > -1):
        time.sleep(10 - api_benchmark.get_runtime_seconds())

    #print(" Run: " + str(runs))

begin_time.stop()
print("\n Runtime: " + begin_time.human_readable_string())
