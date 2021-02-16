import ccxt
import time
import matplotlib.pyplot as pyplot
# from Keys import Key1


def run():
    list_of_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LTCBTC', 'ETHBTC']
    micro_cap_coins = ['ICXBNB', 'BRDBNB', 'NAVBNB', 'RCNBNB']

    print("---------------------------")
    print("Hello World. I am a crypto trading bot made by John.\n")
    print("It's time to make some money\n")

    time.sleep(5)
    try:
        # Get status of Exchange & Account
        print("\n List of Available Exchanges: \n")
        print(ccxt.exchanges)

        for exch1 in ccxt.exchanges:
            exch = getattr(ccxt, exch1)

            print("\n Exchange: ", exch.id)
            print("\n Set Exchange Info (Limits): ", exch.rateLimit)
            print("\n Load Market: ", exch.load_markets)

            symbols = exch.symbols
            if symbols is None:
                print("\n No Symbols Loaded \n")
            else:
                print("Number of Symbols: ", len(symbols))
                print("\n Symbols: ")
                print(exch.id, symbols)
                currencies = exch.currencies
                print("Currencies: ", currencies)
                time.sleep(5)

    except():
        print("\n ATTENTION: NON-VALID CONNECTION WITH CRYPTO BOT \n")
        pass


run()
