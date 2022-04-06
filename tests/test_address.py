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

from account import *
# < --- End Custom Classes Import --- >

begin_time = Benchmark()

whale_addresses = ['5YtjjpckNFvNjvWJPXc9p2UbHzAi5u5UYMwKyaaHLXUN','6Gtd3eYnwn53uE84oSoyTkEPT9UxjZNtJHPvPYZZB6jy','2mEv59w75C59U7SD9fjSkVQmTFi1pCxXP6WP3VPS9Xi9','FHjzq9tbc5HXX4FmwTL1B9yEFt2RJ7GPxfRqheSVgX96']
account_addresses = ['addr1','addr2','addr3','addr4']

a = Accounts(account_addresses)
a.add_data(account_addresses[0],whale_addresses[0],'USD Coin',100)
a.add_data(account_addresses[1],whale_addresses[1],'USD Coin',200)
a.add_data(account_addresses[2],whale_addresses[2],'USD Coin',300)
a.add_data(account_addresses[3],whale_addresses[3],'USD Coin',400)

a.add_data(account_addresses[3],whale_addresses[3],'rBasis',400000)

a.add_data(account_addresses[1],whale_addresses[1],'basis',200000)
a.add_data(account_addresses[1],whale_addresses[1],'basis',300000)
a.add_data(account_addresses[1],whale_addresses[1],'basis',200000)
a.add_data(account_addresses[1],whale_addresses[1],'basis',0)

a.print_data(account_addresses[1],0)
a.print_data(account_addresses[1],1)
a.print_data(account_addresses[1],2)
a.print_data(account_addresses[1],3)

print("Comparing")
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',2883674)))
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',0)))
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',1)))
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',2)))
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',100)))
print(str(a.add_data_compare_to_previous(account_addresses[1],whale_addresses[1],'basis',0)))

begin_time.stop()
print("\n Runtime: " + begin_time.human_readable_string())