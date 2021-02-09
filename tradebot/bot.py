import MetaTrader5 as mt5 
from datetime import datetime

accnt = int(41153949)

mt5.initialize()
authorized=mt5.login(account)

if authorized:
    print("Connected: Connecting to MT5 Client")
else:
    print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))