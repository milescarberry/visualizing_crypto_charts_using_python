import pandas_datareader as web

import matplotlib.pyplot as plt

import mplfinance as mpf

import datetime as dt

start = dt.datetime(2019, 12, 1)

end = dt.datetime.now()


crypto = ["ETH", "XRP"]

currency = "INR"        # How much INR/USD/EUR 1 ETH is for?


#crypto_data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)

#closing_data = crypto_data["Adj Close"].values



eth_data = web.DataReader(f"{crypto[0]}-{currency}","yahoo", start, end)

# eth_data is pandas DataFrame object.

xrp_data = web.DataReader(f"{crypto[1]}-{currency}", "yahoo", start, end)



eth_closing_data = eth_data["Adj Close"].values             # values is an attribute not a "method".


xrp_closing_data = xrp_data["Adj Close"].values









if __name__ == "__main__":

    #  Do Something


    #mpf.plot(crypto_data, type = "candle", volume = True, style = "yahoo")

    #mpf.show()


    plt.yscale("log")       # We are using "logarithmic scaling" on the y-axis.


    plt.title("ETH, XRP vs INR")



    plt.plot(eth_closing_data, label = "ETH")

    plt.plot(xrp_closing_data, label = "XRP")

    plt.legend(loc = "upper left")

    plt.show()
