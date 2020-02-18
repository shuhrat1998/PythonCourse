"""
INTL 550 - HW1
Name : Shukhrat Khuseynov
ID   : 0070495
"""

class Portfolio():
    def __init__(self):
        self.cash = 0.0
        self.stocks = []
        self.mfunds = []
        self.log = ["Transactions:"]
    def addCash(self, cash):
        self.cash += cash
        transaction = "%.2f$ are added to the portfolio." % cash
        self.log.append("%d. " % len(self.log) + transaction)
        print(transaction)
    def withdrawCash(self, cash):
        self.cash -= cash
        transaction = "%.2f$ are withdrawn from the portfolio." % cash
        self.log.append("%d. " % len(self.log) + transaction)
        print(transaction)
    def buyStock(self, shares, symbol):
        pass
    def buyMutualFund(self, shares, symbol):
        pass
    def sellMutualFund(self, symbol, shares):
        pass
    def sellStock(self, symbol, shares):
        pass

    def history(self):
        print("\n".join(self.log))
    def __str__(self):
        return "%s" %self.firstname

class FinInstrument(object):
    def __init__(self, price, symbol):
        self.symbol = symbol
        self.price = price
class Stock(FinInstrument):
    pass
class MutualFund(FinInstrument):
    def __init__(self, symbol):
        super().__init__(1, symbol)
class Bond(FinInstrument):
    pass

if __name__ == '__main__':
    portfolio = Portfolio() #Creates a new portfolio
    portfolio.addCash(300.50) #Adds cash to the portfolio
    s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
    portfolio.buyStock(5, s) #Buys 5 shares of stock s
    mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
    mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
    portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
    portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
    print(portfolio) #Prints portfolio
    #cash: $140.50
    #stock: 5 HFH
    #1
    #mutual funds: 10.33 BRT
     #2 GHT
    portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
    portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
    portfolio.withdrawCash(50) #Removes $50
    portfolio.history() #Prints a list of all transactions ordered by time
    
